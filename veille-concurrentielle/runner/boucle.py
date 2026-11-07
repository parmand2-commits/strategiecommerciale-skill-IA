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
    args = ap.parse_args()

    config = charger(args.config, None)
    if not config:
        print(f"config absente : {args.config}", file=sys.stderr)
        return 1
    reglages = config.get("reglages", {})
    # la ligne de commande l'emporte sur le fichier, dans cet ordre
    if args.pause is None:
        args.pause = reglages.get("pause_secondes", 1.0)
    if args.timeout is None:
        args.timeout = reglages.get("delai_max_secondes", 20)
    etat = {} if args.force else charger(args.state, {})
    jour = time.strftime("%Y-%m-%d")
    maintenant = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    evenements, echecs, par_famille = [], 0, {}
    for concurrent in config.get("concurrents", []):
        nom = concurrent["nom"]
        for famille, urls in concurrent.get("sources", {}).items():
            for url in urls:
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
        "sources_verifiees": len([u for c in config.get("concurrents", [])
                                 for urls in c.get("sources", {}).values() for u in urls]),
        "evenements": len(evenements), "echecs": echecs,
        "a_qualifier": [e for e in evenements if e["type"] in ("changement", "nouvelle_source")],
    }
    if args.dry:
        print(json.dumps(resume, ensure_ascii=False, indent=1)[:2000])
        return 2 if echecs and echecs >= resume["sources_verifiees"] else 0

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

    print(json.dumps({k: resume[k] for k in ("date", "sources_verifiees", "evenements",
                                             "evenements_du_jour", "echecs")},
                     ensure_ascii=False))
    # 2 seulement si toutes les sources tombent : une source cassée est un signal, pas une panne
    return 2 if echecs and echecs >= resume["sources_verifiees"] else 0


if __name__ == "__main__":
    sys.exit(main())
