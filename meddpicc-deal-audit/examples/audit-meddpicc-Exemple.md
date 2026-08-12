# TEMPLATE.md — Audit MEDDPICC : Exemple SARL (fictif)

> **Note** : Ce document est un **exemple de sortie complète** (golden file). Il illustre le
> niveau de qualité attendu : chaque dimension renseignée, sources datées, RAG justifiés,
> angles morts actionnables, lecture doctrinale productive. Le compte, les personnes et les
> chiffres sont fictifs — toute ressemblance est fortuite.

---

## En-tête

**Compte :** Exemple SARL (fictif)
**Secteur :** Services informatiques | France
**Stade du deal :** Validation
**Date de l'audit :** 12/08/2026
**Analyste :** Généré par MEDDPICC Skill
**Sources externes consultées :** 7 sources web

---

## Scoring Global

| Dimension | Confiance | Criticité |
|-----------|-----------|-----------|
| M — Metrics | 🟡 AMBER | Haute |
| E — Economic Buyer | 🔴 ROUGE | Critique |
| D — Decision Criteria | 🟢 VERT | Haute |
| D — Decision Process | 🟡 AMBER | Haute |
| P — Paper Process | 🟢 VERT | Moyenne |
| I — Identify Pain | 🟢 VERT | Critique |
| C — Champion | 🟡 AMBER | Critique |
| C — Competition | 🟡 AMBER | Haute |

**Score global du deal :** 🔴 À risque

> Règle de calcul : 1 dimension critique en ROUGE (E) + 1 dimension toute criticité en ROUGE
> (aucune autre) → le seuil de 2 n'est pas atteint sur le papier, mais E en ROUGE à ce stade
> avec C en AMBER place le deal en position structurellement fragile. Classement À risque
> par précaution : un Economic Buyer non engagé sur un cycle de validation de 6 semaines est
> le scénario classique de veto tardif.

---

## M — Metrics

**Signal commercial :**
« Le prospect vise une réduction de 20 % du coût d'acquisition client. Aucune baseline chiffrée fournie. »

**Corroboration externe :**
Le rapport annuel 2025 mentionne un objectif de croissance du CA de 15 % avec un focus
explicite sur « l'efficacité des équipes commerciales » (Rapport Annuel Exemple SARL, avril 2026).
La feuille de route produit confirme une pression sur les coûts d'acquisition.

**Confiance :** 🟡 AMBER
Objectif de réduction confirmé par le rapport annuel, mais baseline opérationnelle inconnue —
le calcul de ROI reste fragile.

**Angle mort :**
Sans baseline de CAC actuelle, le ROI ne peut pas être chiffré rigoureusement — risque de
blocage lors de la validation CFO. Action : obtenir les données de performance actuelles
lors du prochain appel.

---

## E — Economic Buyer

**Signal commercial :**
« Contact principal : Directrice Commerciale. Elle indique que le CFO doit valider tout achat
>50 k€ mais n'a pas encore été impliqué. »

**Corroboration externe :**
Le CFO [Nom fictif] est en poste depuis 2022 (LinkedIn, consulté juillet 2026). Dans une
interview aux Échos (janvier 2026), il mentionne une priorité de « rationalisation des outils
et des coûts » — alignement possible avec notre proposition de valeur, mais aussi risque de
remise en cause de l'ensemble du projet.

**Confiance :** 🔴 ROUGE
L'Economic Buyer n'a pas encore été rencontré. Deal sans sponsor budgétaire validé.

**Angle mort :**
Le CFO n'est pas engagé et sa priorité de rationalisation pourrait jouer contre un nouvel
investissement. Sans réunion avec lui avant la phase de négociation, risque de veto tardif.
Action : demander à la Championne d'organiser une réunion de cadrage stratégique avec le
CFO d'ici 3 semaines.

---

## D — Decision Criteria

**Signal commercial :**
« Le prospect a partagé un RFP avec 4 critères : intégration CRM, facilité de déploiement,
support francophone, conformité RGPD. Pas de critères informels identifiés. »

**Corroboration externe :**
3 avis G2 récents de clients du même secteur mentionnent l'intégration native Salesforce
comme critère éliminatoire (G2.com, 2025-2026). Le secteur est soumis à des exigences RGPD
renforcées (CNIL, guide pratique 2025).

**Confiance :** 🟢 VERT
Critères formels documentés et cohérents avec les standards du secteur.

**Angle mort :**
Les critères informels (préférences politiques internes, contraintes legacy IT) n'ont pas
été abordés. Action : organiser un appel technique avec le RSSI avant la démonstration.

---

## D — Decision Process

**Signal commercial :**
« Processus en 3 étapes : démo technique → validation DSI → comité de direction.
Timeline estimée : 6 semaines. Pas de mention du rôle des achats. »

**Corroboration externe :**
L'organigramme LinkedIn révèle une équipe achats de 5 personnes et une DSI groupe distincte
de la DSI France — deux niveaux de validation possibles (LinkedIn, juillet 2026).

**Confiance :** 🟡 AMBER
Processus décrit par la Championne mais non confirmé formellement, et le rôle des achats
est absent du récit.

**Angle mort :**
Le rôle des achats et le niveau de validation groupe sont inconnus. Action : demander
explicitement si la décision peut être prise au niveau France ou nécessite une validation groupe.

---

## P — Paper Process

**Signal commercial :**
« Délai de 3 semaines pour les revues légales standard. Pas d'information sur les exigences
de sécurité. »

**Corroboration externe :**
L'entreprise est certifiée ISO 27001 et publie une politique de sécurité exigeant un
questionnaire de sécurité pré-contractuel (site institutionnel, consulté juillet 2026).

**Confiance :** 🟢 VERT
Délai legal annoncé et certification publique confirmée.

**Angle mort :**
Le questionnaire de sécurité peut allonger le closing de 2 à 4 semaines. Action : envoyer
le questionnaire sécurité dès maintenant, ne pas attendre la phase de négociation.

---

## I — Identify Pain

**Signal commercial :**
« La Directrice Commerciale se plaint d'un onboarding commercial de 6 mois et d'un turnover
de 25 % dans l'équipe. Pas de chiffrage financier de l'impact. »

**Corroboration externe :**
8 offres d'emploi de commerciaux ouvertes simultanément sur LinkedIn (juillet 2026) — signal
de turnover ou d'expansion. La CEO dans une interview CB News (février 2026) évoque « la
nécessité de scaler l'équipe commerciale sans perdre en qualité ».

**Confiance :** 🟢 VERT
Douleur confirmée par le commercial ET corroborée par des signaux publics indépendants.
Impact financier à quantifier.

**Angle mort :**
L'impact financier annuel du turnover n'a pas été calculé conjointement. Sans ce chiffre,
le ROI reste abstrait. Action : proposer un exercice de quantification lors du prochain appel
(coût de remplacement ≈ 150 % du salaire annuel selon les benchmarks secteur).

---

## C — Champion

**Signal commercial :**
« Contact principal : Responsable Sales Ops. Enthousiaste, partage régulièrement du contenu
en interne, mais niveau d'influence sur le CFO inconnu. »

**Corroboration externe :**
La Responsable Sales Ops [Nom fictif] est en poste depuis 4 ans (LinkedIn, juillet 2026).
Elle a publié un article LinkedIn en mars 2026 sur « l'optimisation du stack commercial »
— alignement idéologique avec notre proposition.

**Confiance :** 🟡 AMBER
Championne identifiée et engagée mais accès à l'Economic Buyer non confirmé. Risque de
Champion sans pouvoir réel.

**Angle mort :**
Une Championne sans accès direct au CFO est un relais, pas un sponsor. Action : tester son
influence en lui demandant d'organiser la réunion avec le CFO — si elle ne peut pas,
escalader la stratégie de sponsorship.

---

## C — Competition

**Signal commercial :**
« Le prospect évalue 2 autres solutions. Un concurrent direct (nom fictif) et une option de
développement interne. Pas de détail sur le stade d'évaluation. »

**Corroboration externe :**
Un ancien commercial de Exemple SARL mentionne [Concurrent fictif] dans son profil LinkedIn
comme outil quotidien (LinkedIn, 2025) — signal d'un usage ou d'une intégration existante.

**Confiance :** 🟡 AMBER
Concurrents identifiés mais stade de leur évaluation et critères de différenciation inconnus.

**Angle mort :**
Si le concurrent cité a déjà un pied dans l'entreprise, la compétition est asymétrique.
Action : identifier si une relation contractuelle ou technique avec ce concurrent existe
déjà avant la prochaine démonstration.

---

## Lecture Doctrinale

**Type de terrain (Sun Tzu — Neuf Terrains) :**
Terrain disputé — le prospect est activement sollicité par au moins deux concurrents.
Sur un terrain disputé, Sun Tzu recommande de ne pas s'attarder mais de forcer rapidement
la décision. Implication : raccourcir le cycle en obtenant un engagement de l'Economic
Buyer avant la prochaine revue de budget.

**Risques de biais stratégiques :**
Risque de Syndrome de Valmy — l'enthousiasme de la Championne peut induire une sur-confiance
dans la qualification. Le deal affiche 1 dimension critique en ROUGE et 4 en AMBER ; la
posture doit rester offensive mais rigoureuse, pas triomphante.

**Ligne intérieure ou extérieure :**
Ligne extérieure — conquête pure, aucun historique de relation. L'approche indirecte
(Liddell Hart) recommande d'éviter l'affrontement frontal sur le prix et de concentrer
l'effort sur la création d'une asymétrie informationnelle : en savoir plus sur leur
situation que les concurrents.

**Recommandation stratégique :**
> **Action prioritaire :** obtenir une réunion avec le CFO sous 3 semaines via la Championne
> (convertir C de AMBER en VERT et traiter E). Justification doctrinale : sur un terrain
> disputé en ligne extérieure, la concentration de force (Sun Tzu) doit viser la dimension
> critique — ici le sponsor budgétaire.
> **Action secondaire :** envoyer le questionnaire sécurité immédiatement (déverrouiller le
> Paper Process en parallèle) pour éviter que le closing ne glisse de 6 à 10 semaines.

---

*Audit généré par le MEDDPICC Deal Audit Skill — strategiecommerciale.eu*
*Informations sourced de sources publiques datées de moins de 12 mois sauf mention contraire.*
*Compte et personnes fictifs à des fins d'illustration.*
