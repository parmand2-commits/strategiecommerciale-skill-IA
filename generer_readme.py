#!/usr/bin/env python3
"""Génère le README.md du dépôt public des skills à partir des frontmatters.

Usage : python3 generer_readme.py [dossier_des_skills] [fichier_de_sortie]

Le tableau des skills est reconstruit à chaque exécution : aucune ligne n'est saisie à la main,
ce qui garantit que le README ne dérive pas du corpus réel.
"""

import os
import re
import sys

EN_TETE = """# Salle d'Armes : les skills

Les armes IA de la [Salle d'Armes](https://strategiecommerciale.eu/salle-darmes-armurerie/),
la bibliothèque d'outils de [strategiecommerciale.eu](https://strategiecommerciale.eu) : la
stratégie militaire appliquée à la stratégie commerciale.

Chaque skill s'ancre sur un article publié du blog, produit un livrable nommé avec ses seuils
chiffrés, et fonctionne avec n'importe quel agent. Aucune dépendance entre skills : un dossier,
une arme.

## Installation

Une skill est un dossier autonome. Le chargeur de votre agent fait le reste.

| Environnement | Méthode |
|---|---|
| Agent avec système de skills | Copier le dossier de la skill dans le répertoire de skills de votre agent |
| Agent sans système de skills | Copier le contenu de `INSTRUCTIONS.md` comme prompt système |
| Agent conversationnel | Coller `INSTRUCTIONS.md` comme première instruction de la conversation |
| Automatisation | Brancher la sortie JSON, décrite dans `TOOLS.md`, sur votre orchestrateur |

Renseignez `TOOLS.md` avant le premier usage : profil de votre organisation, outils connectés,
langue et format de sortie. Sans ce fichier, la skill fonctionne en mode dégradé.

## Les skills

"""

PIED = """
## Ajouter une skill

Un dossier `kebab-case` par skill, quatre fichiers obligatoires :

```
<nom-kebab-case>/
├── SKILL.md                  orchestration, pour les agents qui lisent les skills
├── INSTRUCTIONS.md           le même contenu en prompt système autonome
├── TOOLS.md                  manifeste de configuration
├── references/TEMPLATE.md    gabarit de sortie annoté
└── examples/                 un exemple de sortie complète
```

Règles de la maison, contrôlées automatiquement à chaque proposition :

- la skill s'ancre sur un article publié du blog, cité dans le frontmatter ;
- le frontmatter de `SKILL.md` ne porte que `name`, `version` (semver) et `description` ;
- `name` est identique au nom du dossier ;
- `INSTRUCTIONS.md` est autonome : il ne cite aucun autre fichier du dossier ;
- aucun tiret cadratin ni demi-cadratin, dans aucun fichier ;
- aucun chemin absolu de machine ;
- aucune dépendance à une plateforme d'agent : les environnements ne sont cités que dans le
  bandeau de compatibilité ;
- toute donnée chiffrée porte sa source et sa date ;
- une ligne vide précède chaque titre markdown.

## Vérification

Le contrôle tourne dans le workflow d'intégration continue et peut être lancé localement :

```
python3 verifier_skills.py
```

Le code de sortie vaut 1 si une règle bloquante n'est pas respectée.

## Licence

MIT pour le code et les prompts, voir `LICENSE`. Les données produit citées dans les exemples
restent la propriété de leurs éditeurs.
"""


def lire_frontmatter(chemin_skill):
    with open(chemin_skill, encoding="utf-8") as f:
        contenu = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", contenu, flags=re.S)
    if not m:
        return None
    front = m.group(1)
    nom = re.search(r"^name:\s*(\S+)", front, flags=re.M)
    version = re.search(r"^version:\s*(\S+)", front, flags=re.M)
    desc = re.search(r"^description:\s*(?:>|[\|>])?\s*(.*?)(?=\n[A-Za-z_][\w-]*:|\Z)",
                     front, flags=re.S | re.M)
    if not (nom and version and desc):
        return None
    texte = " ".join(desc.group(1).split())
    return {"name": nom.group(1), "version": version.group(1).strip("\"'"), "description": texte}


def article(description):
    m = re.search(
        r"(?:Inspir[ée] de l['’]article|ancr[ée] (?:sur l['’]article|article))\s*«\s*([^»]+?)\s*»",
        description)
    return m.group(1) if m else "à déclarer"


def objet(description):
    texte = re.split(r"Déclencheurs\s*:", description)[0]
    texte = texte.strip()
    fin = texte.find(". ")
    return texte[: fin + 1] if fin > 60 else texte


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    sortie = sys.argv[2] if len(sys.argv) > 2 else "README.md"

    dossiers = sorted(
        d for d in os.listdir(base)
        if os.path.isdir(os.path.join(base, d)) and not d.startswith(".")
        and os.path.isfile(os.path.join(base, d, "SKILL.md")))

    lignes = ["| Skill | Version | Ce qu'elle produit | Article ancre |",
              "|---|---|---|---|"]
    for d in dossiers:
        meta = lire_frontmatter(os.path.join(base, d, "SKILL.md"))
        if not meta:
            print(f"Attention : frontmatter illisible dans {d}, ligne ignorée")
            continue
        lignes.append(f"| [`{meta['name']}`](./{d}/) | {meta['version']} | "
                      f"{objet(meta['description'])} | {article(meta['description'])} |")

    corps = EN_TETE + "\n".join(lignes) + "\n" + PIED
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(corps)
    print(f"{len(dossiers)} skill(s) écrites dans {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
