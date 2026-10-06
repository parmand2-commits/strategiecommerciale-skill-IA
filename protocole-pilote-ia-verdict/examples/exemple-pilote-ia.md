# EXEMPLE COMPLET : pilote de préparation d'appel chez Nexaflow

> Exemple golden file : sortie de référence de la skill « Protocole de pilote IA et verdict ».
> Scénario fictif (éditeur SaaS B2B, 14 commerciaux). Les données sont fictives et illustrent la
> structure attendue : protocole, première revue, deuxième revue, application de la règle de coupe.

---

## LIVRABLE 1 : PROTOCOLE DE PILOTE IA (avant le jour 1)

**Organisation :** Nexaflow (fictif) · **Cas d'usage :** assistant IA de préparation d'appel · **Date :** 24/03/2026

| Élément | Valeur |
|---|---|
| Population pilote | 14 commerciaux (AE), une seule équipe |
| Métrique unique | taux de qualification à l'entrée du pipeline |
| Justification de la métrique | mesure la part des rendez-vous découverte convertis en étape qualifiée, objectif direct de l'assistant de préparation |
| Baseline (valeur) | 34 % |
| Baseline (fenêtre) | 12 semaines, du 01/01/2026 au 23/03/2026 |
| Baseline (source) | export CRM, rapport « conversion découverte vers qualification » |
| Baseline (date de mesure) | 23/03/2026 |
| Seuil de succès | 41 % (plus 20 % relatif sur la baseline, sur 12 semaines) |
| Plancher d'adoption | 60 % des licences avec un usage hebdomadaire (9 AE sur 14) |
| Périmètre gelé | 14 AE, cas d'usage préparation d'appel, durée 12 semaines |
| Date de lancement | 31/03/2026 |
| Date de la première revue | 30/06/2026 |
| Coût total connu | licences 18 000 euros par an, intégration 6 000 euros, supervision 4 h par mois, temps interne à estimer |

## Indicateurs avancés

| Indicateur | Où il se lit | Seuil de surveillance | Valeur au lancement |
|---|---|---|---|
| Adoption réelle | journal d'accès de l'outil | supérieure à 60 % (9 AE) | 0 % (avant lancement) |
| Temps moyen de mise à jour CRM | CRM | stable ou en baisse | 6 h |
| Taux de qualification à l'entrée | CRM | stable ou en hausse | 34 % (baseline) |
| Longueur de cycle | revenue intelligence | stable ou en baisse | 71 jours |

## Sources de friction à surveiller

- **Danger :** recommandation de préparation erronée vers un mauvais angle en rendez-vous, métrique dégradée.
- **Effort :** adoption qui retombe après deux semaines vers un usage réel sous le plancher, métrique illisible.
- **Incertitude :** données CRM incomplètes sur les comptes vers une préparation fondée sur des informations périmées.
- **Hasard :** réorganisation de l'équipe en cours de pilote vers un périmètre initial modifié.

## Critères de sortie

- Sous le seuil après deux revues consécutives : coupe, budget réaffecté.
- Compteur de revues sous le seuil : 0.

---

## LIVRABLE 2 : VERDICT DE CONSEIL DE GUERRE, REVUE 1 (2026-T2)

**Cas d'usage :** assistant IA de préparation d'appel · **Revue :** 2026-T2 · **Date de séance :** 30/06/2026 · **Participants :** direction commerciale, sales ops, deux AE

## 1. Adoption réelle

| Licences | Utilisateurs actifs | Part | Plancher | Écart |
|---|---|---|---|---|
| 14 | 8 | 57 % | 60 % | moins 3 points |

## 2. Métrique

| Métrique | Baseline | Valeur mesurée | Seuil | Écart |
|---|---|---|---|---|
| Taux de qualification | 34 % (23/03/2026) | 37 % | 41 % | moins 4 points |

## 3. Coût total

| Poste | Montant | Période | Source |
|---|---|---|---|
| Licences | 4 500 euros | T2 2026 | facture éditeur, 05/04/2026 (fictif) |
| Intégration | 6 000 euros | T2 2026 | facture intégrateur, 12/04/2026 (fictif) |
| Supervision | 12 h | T2 2026 | relevé interne, 30/06/2026 |
| Temps interne | 40 h | T2 2026 | estimation sales ops, méthode déclarative, 30/06/2026 |

## 4. Indicateurs avancés

| Indicateur | Valeur au lancement | Valeur actuelle | Tendance |
|---|---|---|---|
| Adoption réelle | 0 % | 57 % | hausse |
| Temps de mise à jour CRM | 6 h | 5 h | baisse |
| Longueur de cycle | 71 jours | 69 jours | baisse |

## 5. Lectures croisées

- Conversation intelligence : outil utilisé dans 12 des 30 rendez-vous enregistrés, usage concentré sur 5 AE.
- CRM : les comptes rendus remontent, le délai de mise à jour baisse de 6 h à 5 h.
- Revenue intelligence : pipeline stable, longueur de cycle en légère baisse.

## 6. Verdict

| Verdict | Revues sous le seuil | Responsable | Date de décision | Action |
|---|---|---|---|---|
| **Ajuster** | 1 | responsable sales ops | 30/06/2026 | formation ciblée de 4 AE, objectif d'adoption 9 AE au 10/08/2026, revue suivante le 30/09/2026 |

**Réaffectation du budget (si coupe) :** sans objet à cette revue.

---

## LIVRABLE 2 (suite) : VERDICT DE CONSEIL DE GUERRE, REVUE 2 (2026-T3)

**Cas d'usage :** assistant IA de préparation d'appel · **Revue :** 2026-T3 · **Date de séance :** 30/09/2026 · **Participants :** direction commerciale, sales ops, deux AE

## 1. Adoption réelle

| Licences | Utilisateurs actifs | Part | Plancher | Écart |
|---|---|---|---|---|
| 14 | 9 | 64 % | 60 % | plus 4 points |

## 2. Métrique

| Métrique | Baseline | Valeur mesurée | Seuil | Écart |
|---|---|---|---|---|
| Taux de qualification | 34 % (23/03/2026) | 38 % | 41 % | moins 3 points |

## 3. Coût total

| Poste | Montant | Période | Source |
|---|---|---|---|
| Licences | 4 500 euros | T3 2026 | facture éditeur, 04/07/2026 (fictif) |
| Intégration | 0 euro | T3 2026 | sans objet |
| Supervision | 10 h | T3 2026 | relevé interne, 30/09/2026 |
| Temps interne | 22 h | T3 2026 | estimation sales ops, méthode déclarative, 30/09/2026 |

## 4. Indicateurs avancés

| Indicateur | Valeur précédente | Valeur actuelle | Tendance |
|---|---|---|---|
| Adoption réelle | 57 % | 64 % | hausse |
| Longueur de cycle | 69 jours | 70 jours | stable |

## 5. Lectures croisées

- Conversation intelligence : usage élargi à 8 AE, mais la préparation débouche rarement sur un effet mesurable en rendez-vous.
- CRM : données à jour, délai stable.
- Revenue intelligence : longueur de cycle stable, aucun gain attribuable.

## 6. Verdict

| Verdict | Revues sous le seuil | Responsable | Date de décision | Action |
|---|---|---|---|---|
| **Couper** | 2 | direction commerciale | 30/09/2026 | arrêt du pilote au 15/10/2026, licences non renouvelées |

**Réaffectation du budget (si coupe) :** 4 500 euros par trimestre réaffectés vers la conversation intelligence, responsable sales ops, échéance 31/10/2026.

> La coupe n'est pas un échec : c'est la preuve que la discipline a fonctionné. Deux revues sous le
> seuil, un verdict daté, un budget réaffecté vers ce qui mesure.

---

*Exemple généré par la skill « Protocole de pilote IA et verdict » (strategiecommerciale.eu).
Anchoré sur l'article « La Friction de Clausewitz : mesurer le ROI de votre IA commerciale » (2026).
Données fictives.*
