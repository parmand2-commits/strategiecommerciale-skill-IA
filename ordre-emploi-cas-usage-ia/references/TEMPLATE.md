# TEMPLATE.md : Ordre d'emploi des cas d'usage IA : [Fonction commerciale]

> **Note pour l'agent** : gabarit de sortie. Remplir les champs annotés `[...]`, conserver les
> commentaires `<!-- -->` hors du livrable final, supprimer les annotations entre crochets.

---

## REGISTRE DES ORDRES D'EMPLOI

**Fonction :** [Direction commerciale]
**Date :** [JJ/MM/AAAA]
**Titulaire RevOps :** [fonction]
**Processus cadrés :** [N]
**Licences concernées :** [N]

<!-- En-tête obligatoire. Le titulaire RevOps est le gardien du registre et du tableau.
     Si personne n'est nommé, l'écrire explicitement : défaut de gardien. -->

---

## 1. ORDRES D'EMPLOI

<!-- Dupliquer le bloc ci-dessous une fois par processus. Un ordre d'emploi par page. -->

### Ordre d'emploi : [nom du processus]

<!-- Un processus se nomme par son déclencheur et sa fréquence, jamais par un thème. -->

| Champ | Contenu |
|---|---|
| **Tâche confiée** | [verbe + objet, jamais une catégorie] |
| **Rôle qui la porte** | [une fonction, jamais un service] |
| **Sortie attendue** | [format + délai] |
| **Contrôle qui la valide** | [qui vérifie, sur quoi, à quel moment] |
| **Propriétaire du résultat** | [fonction devant qui la sortie se défend en revue] |

<!-- Règle de coupe en amont : sans rôle consommateur nommé, l'outil n'est pas mis en service.
     Si la colonne « Rôle qui la porte » reste vide, ne pas autoriser la mise en service. -->

---

## 2. TABLEAU DE MESURE PAR RÔLE

<!-- Tenu par la fonction RevOps. Mis à jour chaque semaine, lu en comité chaque mois.
     Ne jamais confondre la colonne « Usage » (fréquence) avec le résultat (revue de pipeline).
     Un usage élevé sans effet sur le pipeline décrit une adoption, pas un gain. -->

| Rôle | Tâche | Output | Usage (par semaine) | Décision du trimestre |
|---|---|---|---|---|
| [fonction] | [reprise mot pour mot de l'ordre d'emploi] | [sortie produite + qui la consomme] | [N] | [Reconduite / Réaffectée / Coupée] |
| [fonction] | [mot pour mot] | [sortie + consommateur] | [N] | [verdict] |

<!-- La cinquième colonne est celle qui tranche. Trois verdicts possibles :
     Reconduite : la sortie est consommée par un rôle nommé et une décision en découle.
     Réaffectée : la sortie est utile à un autre rôle ; réécrire l'ordre d'emploi en conséquence.
     Coupée : aucun rôle nommé ne consomme la sortie ; la licence était une subvention à un éditeur.
     Le verdict tombe au trimestre suivant, jamais à l'échéance du contrat. -->

**Sources du tableau :** [conversation / tableaux de bord CRM / revue de pipeline]

---

## 3. MANDAT DE L'ÉTAT-MAJOR PERMANENT

| Élément | Valeur |
|---|---|
| **Composition** | [un responsable RevOps + un responsable sales enablement] |
| **Cadence** | [une heure par semaine] |
| **Point 1 : ce que la mesure a montré** | [chiffres de la semaine ou du mois, sans commentaire] |
| **Point 2 : la décision unique** | [une licence réaffectée, un ordre d'emploi réécrit, un processus arrêté] |
| **Point 3 : ce qui change pour le terrain** | [ordre d'emploi mis à jour + module de formation] |

<!-- Trois livrables sortent du cycle : l'ordre d'emploi mis à jour, la note de décision,
     le contenu de formation. -->

**Test de fin de trimestre :**
- Processus avec un ordre d'emploi à jour : [N] sur [N]
- Licences avec un rôle nommé qui consomme leur sortie : [N] sur [N]

---

## 4. VALEURS DE RÉFÉRENCE

<!-- Toute donnée chiffrée porte sa source et sa date. Une source de plus de douze mois
     est signalée « information non confirmée (plus de 12 mois) » ou écartée.
     Aucune déduction n'est présentée comme un fait. -->

| Donnée | Valeur | Source | Date |
|---|---|---|---|
| Entreprises qui utilisent l'IA | 90 % | Enquête HubSpot relayée par Forbes (John Koetsier) | 16 septembre 2026 |
| Entreprises à résultats transformateurs | 6 % | Enquête HubSpot relayée par Forbes (John Koetsier) | 16 septembre 2026 |
| Passage à l'échelle sur plusieurs business units | 22 % | Gartner (1 303 responsables interrogés) | 1er septembre 2026 |
| Responsables ignorant la dépense IA de leur fonction en 2025 | 11 % | Gartner (même enquête) | 1er septembre 2026 |
| Initiatives à retour positif là où le retour est suivi | 81 % | Gartner (même enquête) | 1er septembre 2026 |
| Initiatives dont le taux de retour est ignoré chez ceux qui suivent de loin | 29 % | Gartner (même enquête) | 1er septembre 2026 |
| Mise en production à l'échelle | 39 % | MIT Sloan Management Review (Davenport et Bean) | décembre 2025 |
| Projets d'IA générative abandonnés après la preuve de concept | au moins 50 % | Gartner (Chandrasekaran) | 26 janvier 2026 |

<!-- Périmètre : ces chiffres sont des mesures d'enquête, pas des prévisions. Les citer avec
     leur périmètre déclaré, sans les généraliser au-delà de l'échantillon de chaque enquête. -->

---

*Ordre d'emploi généré par la skill « Ordre d'Emploi » de la collection strategiecommerciale.eu.
Un ordre d'emploi sans rôle consommateur nommé n'autorise pas la mise en service de l'outil.*
