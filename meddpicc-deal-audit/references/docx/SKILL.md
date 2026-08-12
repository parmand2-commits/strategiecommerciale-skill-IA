# docx/SKILL.md — Génération du document .docx

> Fichier de référence pour le mode `output_format: document`.
> Ce fichier est lu uniquement lorsque ce mode est déclaré dans `TOOLS.md`.

## Spécifications de format

Le livrable `.docx` doit respecter l'identité visuelle strategiecommerciale.eu :

| Élément | Valeur |
|---------|--------|
| Fond de page | `#0d0c0a` (noir profond) |
| Accents / titres | `#b49840` (or) |
| En-tête | « Audit MEDDPICC — [NomCompte] — [Date] » |
| Corps | Texte clair sur fond sombre, lisible |
| Scoring RAG | Couleurs : vert / amber / rouge |
| Polices | Sans-serif sobre (Calibri ou équivalent) |

## Structure du document

1. **Page de titre** : en-tête, compte, secteur, stade, date, analyste.
2. **Tableau de scoring global** (8 dimensions + score global).
3. **Une section par dimension** : Signal, Corroboration, Confiance RAG (pastille couleur),
   Angle mort.
4. **Lecture Doctrinale** : terrain, biais, ligne, recommandations en encadré.
5. **Footer** : « Audit généré par le MEDDPICC Deal Audit Skill — strategiecommerciale.eu ».

## Génération

Préférer une génération via un outil de conversion Markdown → .docx disponible dans
l'environnement (pandoc, python-docx, ou la fonction d'export de l'agent).
Nom de fichier : `audit-meddpicc-[NomCompte]-[DateJour].docx`.
Sauvegarder dans le dossier `output_dir` déclaré dans `TOOLS.md` (défaut : dossier courant).
