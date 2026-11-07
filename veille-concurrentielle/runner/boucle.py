#!/usr/bin/env python3
"""Boucle de collecte de la veille concurrentielle : détecte, ne juge pas.

Le partage est volontaire. Le code fait ce qui est déterministe et vérifiable :
il récupère les pages, calcule une empreinte, compare avec la veille précédente,
repère les changements, tient l'état et signale les sources cassées. Il ne note
pas l'importance d'un signal : c'est le travail de l'agent et de la grille.

Sortie : un dossier de faits par jour (out/<date>/evenements.json) que l'agent
lit pour qualifier, plus un squelette de brief hebdomadaire.

Usage :
    python3 boucle.py --config config.json [--state etat.json]
                    [--out ./out] [--dry] [--force] [--timeout 20]

Codes de sortie : 0 en marche normale, y compris avec une source en échec ; 2 si toutes les
sources tombent ; 1 sur erreur de configuration.

Dépendances : bibliothèque standard uniquement (urllib, hashlib, json, html, re).
"""
import argparse
import hashlib
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (compatible; veille-concurrentielle/1.0)"
# Poids d'irréversibilité par famille de source : ce qui coûte cher à défaire.
POIDS = {"tarifs": 3, "offre": 3, "recrutement": 2, "partenariat": 3,
         "communique": 2, "avis": 1, "brevets": 3, "produit": 2, "salon": 1}
# Une source est déclarée dégradée après trois échecs consécutifs.
SEUIL_ECHECS = 3


def charger(chemin, defaut):
    p = pathlib.Path(chemin)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return defaut


def ecrire_texte_atomique(chemin, texte):
    p = pathlib.Path(chemin)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(texte, encoding="utf-8")
    tmp.replace(p)


def ecrire_atomique(chemin, donnees):
    ecrire_texte_atomique(chemin, json.dumps(donnees, ensure_ascii=False, indent=1))


def sources_aplaties(config):
    """Une seule représentation des sources, quelle que soit la façon dont elles sont écrites.

    Une source peut être une simple URL ou un objet qui porte son propriétaire et sa criticité.
    Le propriétaire et la criticité ne sont pas décoratifs : le taux de couverture se calcule
    sur les sources déclarées critiques, et une URL sans propriétaire est une URL qui sera
    abandonnée sans que personne ne s'en aperçoive.
    """
    out = []
    for c in config.get("concurrents", []):
        defaut = c.get("proprietaire")
        for famille, entrees in c.get("sources", {}).items():
            for e in entrees:
                if isinstance(e, str):
                    s = {"url": e, "critique": True, "proprietaire": defaut}
                else:
                    s = {"url": e["url"], "critique": e.get("critique", True),
                         "proprietaire": e.get("proprietaire", defaut)}
                s.update({"famille": famille, "concurrent": c["nom"]})
                out.append(s)
    return out


def tableau_registre(config):
    """Registre lisible, dérivé de la configuration : jamais deux listes à tenir."""
    lignes = ["| Concurrent | Famille | Source | Propriétaire | Critique |",
              "|---|---|---|---|---|"]
    for s in sources_aplaties(config):
        lignes.append(f"| {s['concurrent']} | {s['famille']} | {s['url']} | "
                      f"{s['proprietaire'] or 'à nommer'} | {'oui' if s['critique'] else 'non'} |")
    return "\n".join(lignes)


def ajouter_source(chemin, concurrent, famille, url, proprietaire, critique):
    """Ajoute une source après contrôle, puis réécrit la configuration."""
    if famille not in POIDS:
        return f"famille inconnue : {famille}. Familles admises : {', '.join(sorted(POIDS))}"
    if not re.match(r"^https?://[^\s]+$", url):
        return "url invalide : une source doit commencer par http:// ou https://"
    config = charger(chemin, None)
    if not config:
        return f"configuration absente : {chemin}"
    deja = {s["url"] for s in sources_aplaties(config)}
    if url in deja:
        return f"source déjà présente : {url}"
    cible = next((c for c in config["concurrents"] if c["nom"] == concurrent), None)
    if cible is None:
        cible = {"nom": concurrent, "priorite": "surveille", "sources": {}}
        config["concurrents"].append(cible)
    cible.setdefault("sources", {}).setdefault(famille, []).append(
        {"url": url, "proprietaire": proprietaire, "critique": critique})
    ecrire_atomique(chemin, config)
    return ("source ajoutée : " + concurrent + " / " + famille + " / " + url
            + " (propriétaire : " + (proprietaire or "à nommer") + ")")


def texte_normalise(brut):
    """Réduit une page à son texte utile, pour que l'empreinte ne bouge pas
    au moindre changement de menu ou de cookie."""
    sans_script = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", brut)
    sans_balise = re.sub(r"(?s)<[^>]+>", " ", sans_script)
    txt = html.unescape(sans_balise)
    txt = re.sub(r"\s+", " ", txt).strip().lower()
    return txt


def titre_page(brut):
    m = re.search(r"(?is)<title[^>]*>(.*?)</title>", brut)
    return html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else ""


def recuperer(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "fr,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        brut = r.read().decode(r.headers.get_content_charset() or "utf-8", "ignore")
        return brut, r.status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.json")
    ap.add_argument("--state", default="etat.json")
    ap.add_argument("--out", default="out")
    ap.add_argument("--timeout", type=int, default=None)
    ap.add_argument("--pause", type=float, default=None, help="délai entre deux requêtes")
    ap.add_argument("--dry", action="store_true", help="n'écrit ni l'état ni les sorties")
    ap.add_argument("--force", action="store_true", help="ignore l'état, tout est neuf")
    ap.add_argument("--registre", action="store_true",
                    help="affiche le registre des sources dérivé de la configuration")
    ap.add_argument("--ajouter-source", action="store_true",
                    help="ajoute une source après contrôle, avec son propriétaire")
    ap.add_argument("--concurrent", help="concurrent concerné par --ajouter-source")
    ap.add_argument("--famille", help="famille de source : " + ", ".join(sorted(POIDS)))
    ap.add_argument("--url", help="url de la source à ajouter")
    ap.add_argument("--proprietaire", help="fonction responsable de cette source")
    ap.add_argument("--non-critique", action="store_true",
                    help="la source ne compte pas dans le taux de couverture")
    args = ap.parse_args()

    config = charger(args.config, None)
    if not config:
        print(f"config absente : {args.config}", file=sys.stderr)
        return 1

    if args.registre:
        print(tableau_registre(config))
        return 0

    if args.ajouter_source:
        manquants = [n for n in ("concurrent", "famille", "url") if not getattr(args, n)]
        if manquants:
            print("arguments manquants pour --ajouter-source : " + ", ".join(manquants),
                  file=sys.stderr)
            return 1
        message = ajouter_source(args.config, args.concurrent, args.famille, args.url,
                                 args.proprietaire, not args.non_critique)
        print(message)
        return 0 if message.startswith("source ajoutée") else 1
    reglages = config.get("reglages", {})
    # la ligne de commande l'emporte sur le fichier, dans cet ordre
    if args.pause is None:
        args.pause = reglages.get("pause_secondes", 1.0)
    if args.timeout is None:
        args.timeout = reglages.get("delai_max_secondes", 20)
    etat = {} if args.force else charger(args.state, {})
    jour = time.strftime("%Y-%m-%d")
    maintenant = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    toutes = sources_aplaties(config)
    critiques = [s for s in toutes if s["critique"]]
    evenements, echecs, par_famille, ok, critiques_ok = [], 0, {}, 0, 0
    for concurrent in config.get("concurrents", []):
        nom = concurrent["nom"]
        for famille, entrees in concurrent.get("sources", {}).items():
            for entree in entrees:
                url = entree if isinstance(entree, str) else entree["url"]
                precedent = etat.get(url, {})
                try:
                    brut, status = recuperer(url, args.timeout)
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
                    echecs += 1
                    essais = precedent.get("echecs", 0) + 1
                    etat[url] = {**precedent, "echecs": essais, "dernier_essai": maintenant}
                    if essais >= SEUIL_ECHECS and not precedent.get("degrade"):
                        etat[url]["degrade"] = True
                        evenements.append({
                            "type": "source_degradee", "concurrent": nom, "famille": famille,
                            "url": url, "echecs": essais, "erreur": str(e)[:200],
                            "note": "couverture non assurée : le taux de couverture doit le voir",
                        })
                    continue

                ok += 1
                if any(c["url"] == url for c in critiques):
                    critiques_ok += 1
                empreinte = hashlib.sha256(texte_normalise(brut).encode()).hexdigest()
                type_evt = None
                if not precedent.get("empreinte"):
                    type_evt = "nouvelle_source"
                elif precedent["empreinte"] != empreinte:
                    type_evt = "changement"

                if type_evt:
                    evenements.append({
                        "type": type_evt, "concurrent": nom, "famille": famille, "url": url,
                        "statut_http": status, "titre": titre_page(brut),
                        "empreinte": empreinte,
                        "poids_irreversibilite": POIDS.get(famille, 2),
                        "vu_le": maintenant,
                        "premiere_vue": precedent.get("premiere_vue", maintenant),
                    })
                    par_famille[(nom, famille)] = par_famille.get((nom, famille), 0) + 1

                etat[url] = {
                    "empreinte": empreinte,
                    "premiere_vue": precedent.get("premiere_vue", maintenant),
                    "dernier_ok": maintenant,
                    "dernier_changement": maintenant if type_evt == "changement"
                    else precedent.get("dernier_changement"),
                    "echecs": 0,
                }
                if not args.dry:
                    time.sleep(args.pause)

    # spécificité : plusieurs pages d'une même famille bougent en même temps
    for evt in evenements:
        if evt["type"] in ("changement", "nouvelle_source"):
            n = par_famille.get((evt["concurrent"], evt["famille"]), 1)
            evt["pages_touchees_meme_famille"] = n
            evt["specificite_proposee"] = 3 if n >= 2 else 2

    dossier = pathlib.Path(args.out) / jour
    resume = {
        "date": jour, "genere_le": maintenant,
        "concurrents_suivis": len(config.get("concurrents", [])),
        "sources_declarees": len(toutes),
        "sources_ok": ok,
        "sources_critiques": len(critiques),
        "couverture_pourcent": round(100 * critiques_ok / len(critiques)) if critiques else None,
        "evenements": len(evenements), "echecs": echecs,
        "a_qualifier": [e for e in evenements if e["type"] in ("changement", "nouvelle_source")],
    }
    if args.dry:
        print(json.dumps(resume, ensure_ascii=False, indent=1)[:2000])
        return 2 if echecs and echecs >= resume["sources_declarees"] else 0

    # plusieurs passages par jour : on cumule, sans doublon (même page, même empreinte).
    # On distingue ce que ce passage a trouvé de ce que la journée contient déjà, sinon un
    # journal d'exécution ne dit pas si le réveil du jour a servi à quelque chose.
    nouveaux = len(resume["a_qualifier"])
    ancien = charger(dossier / "evenements.json", {}) if (dossier / "evenements.json").exists() else {}
    if ancien.get("a_qualifier"):
        vus = {(e["url"], e["empreinte"]) for e in resume["a_qualifier"]}
        for e in ancien["a_qualifier"]:
            if (e["url"], e["empreinte"]) not in vus:
                resume["a_qualifier"].append(e)
    resume["evenements"] = nouveaux
    resume["evenements_du_jour"] = len(resume["a_qualifier"])
    ecrire_atomique(dossier / "evenements.json", resume)
    ecrire_atomique(args.state, etat)

    # squelette de brief : l'agent le remplit, il ne part jamais d'une page blanche
    if resume["a_qualifier"]:
        lignes = [f"# Brief de veille, {jour}", "",
                  f"{len(resume['a_qualifier'])} changement(s) à qualifier, "
                  f"{echecs} source(s) en échec.", ""]
        for e in resume["a_qualifier"]:
            lignes += [f"## {e['concurrent']} / {e['famille']}", "",
                       f"- page : {e['url']}",
                       f"- titre : {e['titre']}",
                       f"- vu le : {e['vu_le']}",
                       f"- irréversibilité proposée : {e['poids_irreversibilite']}/3",
                       f"- spécificité proposée : {e['specificite_proposee']}/3",
                       "- impact : à qualifier (quelle décision nommée change ?)", ""]
        ecrire_texte_atomique(dossier / "brief-squelette.md", "\n".join(lignes))

    print(json.dumps({k: resume[k] for k in ("date", "sources_declarees", "sources_ok",
                                             "couverture_pourcent", "evenements",
                                             "evenements_du_jour", "echecs")},
                     ensure_ascii=False))
    # 2 seulement si toutes les sources tombent : une source cassée est un signal, pas une panne
    return 2 if echecs and echecs >= resume["sources_declarees"] else 0


if __name__ == "__main__":
    sys.exit(main())
