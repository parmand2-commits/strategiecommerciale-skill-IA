# TEMPLATE.md : gabarit de sortie annoté

Deux livrables : le protocole de pilote (avant lancement) et le verdict de conseil de guerre (revue
trimestrielle). Recopier les titres et les colonnes telles quelles, remplacer les crochets,
supprimer les commentaires.

---

## LIVRABLE 1 : PROTOCOLE DE PILOTE IA (avant le jour 1)

<!-- En-tête du protocole. La date est celle de l'écriture, avant le lancement. -->
**Organisation :** [Nom] · **Cas d'usage :** [ex. assistant de préparation d'appel] · **Date :** [JJ/MM/AAAA]

<!-- Table d'identité du pilote, une ligne par élément. Aucun champ vide : « non mesuré » est une valeur. -->
| Élément | Valeur |
|---|---|
| Population pilote | [N commerciaux, rôles] |
| Métrique unique | [une seule métrique commerciale] |
| Justification de la métrique | [une phrase : objectif touché, décision éclairée] |
| Baseline (valeur) | [valeur] |
| Baseline (fenêtre) | [durée et période de référence] |
| Baseline (source) | [outil et requête, ou relevé manuel] |
| Baseline (date de mesure) | [JJ/MM/AAAA] |
| Seuil de succès | [valeur chiffrée, mode de comparaison à la baseline] |
| Plancher d'adoption | [% des licences avec un usage hebdomadaire] |
| Périmètre gelé | [population, cas d'usage, durée] |
| Date de lancement | [JJ/MM/AAAA] |
| Date de la première revue | [JJ/MM/AAAA] |
| Coût total connu | [licences, intégration, supervision, temps interne] |

<!-- Les indicateurs avancés, lus chaque semaine dans des outils déjà en place. -->

## Indicateurs avancés

| Indicateur | Où il se lit | Seuil de surveillance | Valeur au lancement |
|---|---|---|---|
| Adoption réelle | [outil / journal d'accès] | supérieure à [plancher] | [valeur] |
| Temps moyen de mise à jour CRM | [CRM] | stable ou en baisse | [valeur] |
| Taux de qualification à l'entrée | [CRM] | stable ou en hausse | [valeur] |
| Longueur de cycle | [revenue intelligence] | stable ou en baisse | [valeur] |

<!-- Les quatre sources de friction, nommées, chacune avec l'angle mort qu'elle crée. -->

## Sources de friction à surveiller

- **Danger :** [erreur qui coûte] vers [impact sur la métrique]
- **Effort :** [adoption qui retombe] vers [impact]
- **Incertitude :** [donnée CRM incomplète] vers [impact]
- **Hasard :** [événement imprévu] vers [impact]

<!-- Les règles de sortie, annoncées au lancement. -->

## Critères de sortie

- Sous le seuil après deux revues consécutives : coupe, budget réaffecté.
- Compteur de revues sous le seuil : [0]

---

## LIVRABLE 2 : VERDICT DE CONSEIL DE GUERRE (revue trimestrielle)

<!-- En-tête de la revue. Trimestre et date de séance. -->
**Cas d'usage :** [objet] · **Revue :** [AAAA-T1] · **Date de séance :** [JJ/MM/AAAA] · **Participants :** [rôles]

<!-- Bloc 1 : l'écart entre licences payées et usage réel. -->

## 1. Adoption réelle

| Licences | Utilisateurs actifs | Part | Plancher | Écart |
|---|---|---|---|---|
| [N] | [N] | [%] | [%] | [+/- points] |

<!-- Bloc 2 : la métrique contre le seuil. -->

## 2. Métrique

| Métrique | Baseline | Valeur mesurée | Seuil | Écart |
|---|---|---|---|---|
| [nom] | [valeur et date] | [valeur] | [seuil] | [+/-] |

<!-- Bloc 3 : le coût total contre la valeur constatée. Chaque ligne porte sa source et sa date. -->

## 3. Coût total

| Poste | Montant | Période | Source |
|---|---|---|---|
| Licences | [€] | [période] | [source, date] |
| Intégration | [€] | [période] | [source, date] |
| Supervision | [h ou €] | [période] | [source, date] |
| Temps interne | [h ou €] | [période] | [estimation, méthode, date] |

<!-- Bloc 4 : les indicateurs avancés et leur tendance depuis la revue précédente. -->

## 4. Indicateurs avancés

| Indicateur | Valeur précédente | Valeur actuelle | Tendance |
|---|---|---|---|
| Adoption réelle | [valeur] | [valeur] | [hausse / stable / baisse] |

<!-- La lecture croisée des trois sources de vérité du terrain. -->

## 5. Lectures croisées

- Conversation intelligence : [l'outil est-il utilisé en rendez-vous ?]
- CRM : [les données remontent-elles, à quelle vitesse ?]
- Revenue intelligence : [le pipeline bouge-t-il ?]

<!-- Le verdict : un seul des trois termes. Daté, avec un responsable unique. -->

## 6. Verdict

| Verdict | Revues sous le seuil | Responsable | Date de décision | Action |
|---|---|---|---|---|
| **Continuer** / **Ajuster** / **Couper** | [compteur] | [une personne] | [JJ/MM/AAAA] | [action et échéance] |

<!-- Si coupe : où va le budget libéré. Sinon : « sans objet ». -->
**Réaffectation du budget (si coupe) :** [destination, responsable, échéance]

---

*Gabarit de la skill « Protocole de pilote IA et verdict » (strategiecommerciale.eu). Un pilote qui
démarre sans baseline ne produit pas un ROI, il produit une anecdote.*
