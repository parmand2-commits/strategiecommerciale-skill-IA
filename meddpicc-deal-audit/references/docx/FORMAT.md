# FORMAT.md : Génération du document .docx

> Fichier de référence pour le mode `output_format: document`.
> Ce fichier est lu uniquement lorsque ce mode est déclaré dans `TOOLS.md`.

## Spécifications de format

Le livrable `.docx` doit respecter la charte du site (fond clair, accents cuivre) :

| Élément | Valeur |
|---------|--------|
| Fond de page | blanc pur `#FFFFFF` |
| Texte courant | encre `#0C1B2E` |
| Accents, filets, titres | cuivre `#C98A4B` |
| En-tête | « Audit MEDDPICC · [NomCompte] · [Date] » |
| Scoring RAG | pastilles vert / amber / rouge, texte de justification en encre |
| Polices | sans-serif sobre (Calibri ou équivalent), titres en gras cuivre |

**Ne jamais produire de document à fond sombre.** Un .docx sur fond noir n'est pas imprimable,
n'est pas annotable, et Word ne gère le fond plein page que par une forme de couverture, ce qui
casse la mise en page dès qu'on modifie le texte. Le fond reste blanc, l'identité passe par les
titres, les filets et les encadrés.

## Structure du document

1. **Page de titre** : en-tête, compte, secteur, stade, date, mode d'exécution, analyste.
2. **Tableau de scoring global** (8 dimensions avec confiance et criticité, puis score global).
3. **Une section par dimension** : Signal, Corroboration, Criticité, Confiance RAG (pastille
   couleur), Angle mort.
4. **Section de mode** si applicable : tableau d'extraction avec verbatim et locuteur, brief
   pré-réunion, ou proposition de mise à jour CRM.
5. **Lecture Doctrinale** : terrain, biais, ligne, recommandations en encadré cuivre.
6. **Footer** : « Audit généré par le MEDDPICC Deal Audit Skill · strategiecommerciale.eu ».

## Génération

Préférer une génération via un outil de conversion Markdown → .docx disponible dans
l'environnement (pandoc, python-docx, ou la fonction d'export de l'agent).
Nom de fichier : `audit-meddpicc-[NomCompte]-[DateJour].docx`.
Sauvegarder dans le dossier `output_dir` déclaré dans `TOOLS.md` (défaut : dossier courant).
