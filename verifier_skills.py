#!/usr/bin/env python3
"""Vérificateur du corpus de skills de la Salle d'Armes.

Contrôle les règles de la maison sur chaque dossier de skills/ :
  1. SKILL.md, INSTRUCTIONS.md et TOOLS.md présents.
  2. Frontmatter de SKILL.md : name identique au dossier, version au format semver.
  3. INSTRUCTIONS.md autonome : aucune renvoi vers un autre fichier du dossier.
  4. Aucun tiret cadratin ni demi-cadratin, dans aucun fichier texte.
  5. Aucun chemin absolu de machine.
  6. Aucun nom d'éditeur de plateforme d'agent hors de la ligne de compatibilité.
  7. references/TEMPLATE.md présent (le livrable est structuré).

Avertissements, non bloquants :
  A. examples/ absent (exemple de sortie complète).
  B. description du frontmatter sans liste de déclencheurs entre guillemets.
  C. fichier non déclaré dans la section « Fichiers de référence » de SKILL.md.

Usage : python3 verifier_skills.py [chemin_du_dossier_skills]
Sortie : rapport lisible, code 1 si au moins une erreur bloquante.
"""

import os
import re
import sys

CADRATIN = "\u2014"
DEMI_CADRATIN = "\u2013"

# Noms d'éditeurs de plateformes d'agents. Ils ne sont fautifs que hors du bandeau de
# compatibilité, c'est-à-dire lorsqu'ils trahissent une dépendance et non une promesse
# d'agnosticité. Une ligne qui cite plusieurs environnements est un bandeau.
EDITEURS_AGENTS = [
    "Claude Code", "Cursor", "Windsurf", "n8n", "OpenAI Assistants",
    "GPT Store", "Copilot Studio", "LangChain", "CrewAI", "AutoGen",
]

# Marqueurs d'un bandeau de compatibilité (la skill annonce où elle tourne).
MARQUEURS_COMPATIBILITE = [
    "système de skills", "systeme de skills", "environnement d'agent", "agents avec",
    "ChatGPT", "Gemini", "Perplexity", "Copilot", "compatible", "selon votre agent",
    "automatis", "workflow",
]

# Clés admises dans le frontmatter de SKILL.md. Toute autre clé signale un format
# importé d'ailleurs (auteur, licence, plateformes, métadonnées d'un outil précis).
CLES_FRONTMATTER = {"name", "version", "description"}

# Fichiers de references/ : un prompt autonome ne peut pas les lire, donc il ne doit pas
# les citer. La mention de SKILL.md, elle, est légitime dans le bandeau d'en-tête.
FICHIERS_EXTERNES = ["references/", "TEMPLATE.md", "DOCTRINE.md", "RELEVE.md", "FORMAT.md"]
LIGNES_ENTETE = 12

# Chemins absolus de machine.
CHEMINS_ABSOLUS = [re.compile(r"(?<![\w.])/root/"), re.compile(r"(?<![\w.])/home/"),
                   re.compile(r"(?<![\w.])/Users/"), re.compile(r"[A-Z]:\\\\")]

FICHIERS_OBLIGATOIRES = ["SKILL.md", "INSTRUCTIONS.md", "TOOLS.md"]
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def fichiers_texte(dossier):
    out = []
    for racine, _, noms in os.walk(dossier):
        for n in sorted(noms):
            if n.lower().endswith((".md", ".txt", ".json", ".js", ".py", ".yml", ".yaml")):
                out.append(os.path.join(racine, n))
    return out


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


def bloc_frontmatter(contenu):
    m = re.match(r"^---\n(.*?)\n---\n", contenu, flags=re.S)
    return m.group(1) if m else None


def verifier_skill(dossier):
    erreurs, avertissements = [], []
    nom_dossier = os.path.basename(dossier.rstrip("/"))

    for f in FICHIERS_OBLIGATOIRES:
        if not os.path.isfile(os.path.join(dossier, f)):
            erreurs.append(f"fichier obligatoire absent : {f}")

    chemin_skill = os.path.join(dossier, "SKILL.md")
    front = None
    if os.path.isfile(chemin_skill):
        contenu = lire(chemin_skill)
        front = bloc_frontmatter(contenu)
        if front is None:
            erreurs.append("SKILL.md : bloc de frontmatter absent ou mal fermé")
        else:
            m = re.search(r"^name:\s*(\S+)", front, flags=re.M)
            if not m:
                erreurs.append("SKILL.md : clé name absente du frontmatter")
            elif m.group(1) != nom_dossier:
                erreurs.append(
                    f"SKILL.md : name « {m.group(1)} » différent du dossier « {nom_dossier} »")
            m = re.search(r"^version:\s*(\S+)", front, flags=re.M)
            if not m:
                erreurs.append("SKILL.md : clé version absente du frontmatter")
            elif not SEMVER.match(m.group(1).strip("\"'")):
                erreurs.append(
                    f"SKILL.md : version « {m.group(1)} » hors format semver x.y.z")
            declencheurs = re.findall(r"\"[^\"]{4,}\"|«[^»]{4,}»", front)
            if len(declencheurs) < 2:
                avertissements.append(
                    "SKILL.md : description sans liste de déclencheurs (2 minimum)")
            cles = set(re.findall(r"^([A-Za-z_][\w-]*):", front, flags=re.M))
            en_trop = sorted(cles - CLES_FRONTMATTER)
            if en_trop:
                erreurs.append(
                    "SKILL.md : frontmatter hors format maison, clé(s) en trop : "
                    + ", ".join(en_trop))
            manquantes = sorted(CLES_FRONTMATTER - cles)
            if manquantes:
                erreurs.append(
                    "SKILL.md : frontmatter incomplet, clé(s) manquante(s) : "
                    + ", ".join(manquantes))

    chemin_instructions = os.path.join(dossier, "INSTRUCTIONS.md")
    if os.path.isfile(chemin_instructions):
        lignes = lire(chemin_instructions).splitlines()
        for i, ligne in enumerate(lignes, start=1):
            for externe in FICHIERS_EXTERNES:
                if externe in ligne:
                    erreurs.append(
                        f"INSTRUCTIONS.md ligne {i} : cite {externe}, que l'agent qui reçoit "
                        f"ce prompt seul ne peut pas lire")
            if i > LIGNES_ENTETE and "TOOLS.md" in ligne:
                erreurs.append(
                    f"INSTRUCTIONS.md ligne {i} : cite TOOLS.md hors du bandeau d'en-tête, "
                    f"ce fichier doit être autonome")

    if not os.path.isfile(os.path.join(dossier, "references", "TEMPLATE.md")):
        erreurs.append("references/TEMPLATE.md absent (livrable structuré attendu)")
    if not os.path.isdir(os.path.join(dossier, "examples")):
        avertissements.append("examples/ absent (exemple de sortie complète attendu)")
    else:
        ex = [f for f in os.listdir(os.path.join(dossier, "examples")) if f.endswith(".md")]
        if not ex:
            avertissements.append("examples/ vide")

    for chemin in fichiers_texte(dossier):
        rel = os.path.relpath(chemin, dossier)
        contenu = lire(chemin)

        if CADRATIN in contenu or DEMI_CADRATIN in contenu:
            n = contenu.count(CADRATIN) + contenu.count(DEMI_CADRATIN)
            erreurs.append(f"{rel} : {n} tiret(s) cadratin ou demi-cadratin")

        for motif in CHEMINS_ABSOLUS:
            if motif.search(contenu):
                erreurs.append(f"{rel} : chemin absolu de machine détecté")

        if chemin.lower().endswith(".md"):
            lignes_md = contenu.splitlines()
            dans_bloc = False
            colles = []
            for i, ligne in enumerate(lignes_md, start=1):
                if ligne.strip().startswith("```"):
                    dans_bloc = not dans_bloc
                    continue
                if dans_bloc:
                    continue
                if ligne.startswith("#") and i > 1 and lignes_md[i - 2].strip() != "":
                    colles.append(i)
            if colles:
                erreurs.append(
                    f"{rel} : titre(s) collé(s) à la ligne précédente (ligne(s) "
                    + ", ".join(str(c) for c in colles[:8]) + "), une ligne vide est requise "
                    "avant un titre")

        corps = contenu
        if rel == "SKILL.md" and front is not None:
            corps = contenu.replace(front, "", 1)
        for num, ligne in enumerate(corps.splitlines(), start=1):
            if num <= LIGNES_ENTETE:
                continue
            if any(m in ligne for m in MARQUEURS_COMPATIBILITE):
                continue
            if sum(1 for e in EDITEURS_AGENTS if e in ligne) >= 2:
                continue
            for editeur in EDITEURS_AGENTS:
                if editeur in ligne:
                    erreurs.append(
                        f"{rel} : dépendance à une plateforme d'agent « {editeur} » "
                        f"hors bandeau de compatibilité")

    return erreurs, avertissements


def main():
    if len(sys.argv) > 1:
        base = sys.argv[1]
    elif os.path.isdir("skills"):
        base = "skills"
    else:
        base = "."
    if not os.path.isdir(base):
        print(f"Dossier introuvable : {base}")
        return 2

    if os.path.isfile(os.path.join(base, "SKILL.md")):
        dossiers = [base]
    else:
        # Les dossiers techniques (.git, .github) et les caches ne sont pas des skills. Tout
        # autre dossier en est un, même s'il est incomplet : c'est ainsi qu'un SKILL.md manquant
        # est signalé au lieu d'être ignoré.
        dossiers = sorted(
            os.path.join(base, d) for d in os.listdir(base)
            if os.path.isdir(os.path.join(base, d))
            and not d.startswith(".") and d != "__pycache__")

    total_erreurs = total_avertissements = 0
    lignes = []
    for dossier in dossiers:
        erreurs, avertissements = verifier_skill(dossier)
        total_erreurs += len(erreurs)
        total_avertissements += len(avertissements)
        nom = os.path.basename(dossier)
        etat = "OK" if not erreurs else f"{len(erreurs)} erreur(s)"
        lot = [f"{nom:<38} {etat}"]
        for e in erreurs:
            lot.append(f"    ERREUR        {e}")
        for a in avertissements:
            lot.append(f"    avertissement {a}")
        lignes.append("\n".join(lot))

    print("\n".join(lignes))
    print()
    print(f"{len(dossiers)} skill(s) analysée(s) : {total_erreurs} erreur(s), "
          f"{total_avertissements} avertissement(s)")
    return 1 if total_erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
