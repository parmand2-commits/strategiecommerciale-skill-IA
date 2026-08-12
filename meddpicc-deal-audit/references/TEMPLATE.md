# TEMPLATE.md — Audit MEDDPICC : [NomCompte]

> **Note pour l'agent** : Ce fichier est le template de sortie. Remplir chaque champ annoté
> avec les informations collectées. Supprimer les annotations `[...]` dans le livrable final.
> Les champs vides doivent rester visibles (ne pas supprimer les en-têtes de dimension).

---

## En-tête

**Compte :** [NomCompte]
**Secteur :** [Secteur | Pays HQ]
**Stade du deal :** [Exploration | Validation | Négociation | Closing]
**Date de l'audit :** [JJ/MM/AAAA]
**Analyste :** [Nom du commercial ou "Généré par MEDDPICC Skill"]
**Sources externes consultées :** [Nombre de sources web | Outils MCP utilisés]

---

## Scoring Global

> Remplir après avoir complété toutes les dimensions.

| Dimension | Confiance | Criticité |
|-----------|-----------|-----------|
| M — Metrics | 🟢 / 🟡 / 🔴 | Haute |
| E — Economic Buyer | 🟢 / 🟡 / 🔴 | Critique |
| D — Decision Criteria | 🟢 / 🟡 / 🔴 | Haute |
| D — Decision Process | 🟢 / 🟡 / 🔴 | Haute |
| P — Paper Process | 🟢 / 🟡 / 🔴 | Moyenne |
| I — Identify Pain | 🟢 / 🟡 / 🔴 | Critique |
| C — Champion | 🟢 / 🟡 / 🔴 | Critique |
| C — Competition | 🟢 / 🟡 / 🔴 | Haute |

**Score global du deal :** 🟢 Solide | 🟡 À consolider | 🔴 À risque

> Règle de calcul : ≥2 dimensions critiques en ROUGE → deal À risque.
> ≥3 dimensions (toute criticité) en ROUGE → deal À risque.
> Aucun ROUGE sur les 3 dimensions critiques → deal Solide si les autres sont ≥ AMBER.

---

## M — Metrics
*Valeur quantifiée que le prospect cherche à atteindre. C'est la justification économique du projet.*

**Signal commercial :**
[Ce que le commercial a fourni. Reproduire fidèlement. Ex : "Le prospect vise 15 % d'amélioration
du taux de conversion des leads. Pas de baseline chiffrée fournie."]

**Corroboration externe :**
[Ce que les sources publiques confirment ou enrichissent. Toujours citer source + date.
Ex : "Le rapport annuel 2024 mentionne un objectif de croissance du CA de 12 % avec un focus
explicite sur l'efficacité commerciale (Rapport Annuel [NomCompte], mars 2025)."]

**Confiance :** 🟢 / 🟡 / 🔴
[Justification en une ligne. Ex : "AMBER — objectif de croissance confirmé mais baseline
opérationnelle inconnue, rendant le calcul de ROI fragile."]

**Angle mort :**
[Ce qui reste inconnu et l'implication tactique. Ex : "Sans baseline de conversion actuelle,
le ROI ne peut pas être chiffré rigoureusement — risque de blocage lors de la validation CFO.
Action : obtenir les données de performance actuelles lors du prochain appel."]

---

## E — Economic Buyer
*Le décideur budgétaire ultime. Celui qui peut dire oui indépendamment de toute autre approbation.*

**Signal commercial :**
[Ex : "Contact principal : Directeur Commercial. Il indique que le CFO doit valider tout achat
>50k€ mais n'a pas encore été impliqué."]

**Corroboration externe :**
[Rechercher le profil LinkedIn du CFO/CRO/CEO pressenti, sa durée en poste, ses prises de parole
publiques sur les priorités d'investissement. Ex : "Le CFO [Prénom Nom] est en poste depuis 2023
(LinkedIn, consulté juin 2026). Dans une interview aux Échos (jan. 2025), il mentionne une
priorité de « réduction des coûts d'acquisition client » — alignement possible avec notre valeur."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "ROUGE — L'Economic Buyer n'a pas encore été rencontré. Deal sans sponsor budgétaire validé."]

**Angle mort :**
[Ex : "Le CFO n'est pas engagé. Sans réunion avec lui avant la phase de négociation, risque de
veto tardif. Action : demander au Champion d'organiser une réunion de cadrage stratégique avec
le CFO d'ici 3 semaines."]

---

## D — Decision Criteria
*Les critères formels et informels sur lesquels le prospect évaluera les solutions en compétition.*

**Signal commercial :**
[Ex : "Le prospect a partagé un RFP avec 3 critères : intégration CRM, facilité de déploiement,
et support francophone. Pas de critères informels identifiés."]

**Corroboration externe :**
[Rechercher des avis sur G2/Gartner Peer Insights, des témoignages clients publics de l'entreprise,
des offres d'emploi mentionnant les outils ou compétences recherchés.
Ex : "3 avis G2 récents de clients du même secteur mentionnent l'intégration native Salesforce
comme critère éliminatoire (G2.com, 2025)."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "AMBER — Critères formels connus mais critères informels (préférences politiques internes,
contraintes legacy) non identifiés."]

**Angle mort :**
[Ex : "Les critères informels de l'IT (sécurité, souveraineté des données) n'ont pas été abordés.
Action : organiser un appel technique avec le RSSI avant la démonstration."]

---

## D — Decision Process
*Le processus interne de prise de décision : qui valide, dans quel ordre, avec quels jalons.*

**Signal commercial :**
[Ex : "Le prospect indique un processus en 3 étapes : démo technique → validation DSI → comité
de direction. Timeline estimée : 6 semaines. Pas de mention du rôle des achats."]

**Corroboration externe :**
[Rechercher la structure organisationnelle publique, les offres d'emploi en procurement/IT,
les informations sur la gouvernance IT dans les rapports annuels ou interviews.
Ex : "L'organigramme LinkedIn révèle une équipe achats de 8 personnes et un DSI groupe
distinct du DSI France — deux niveaux de validation possibles (LinkedIn, juin 2026)."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "AMBER — Process décrit par le Champion mais non confirmé formellement. Risque de surprises
à l'étape de validation groupe."]

**Angle mort :**
[Ex : "Le rôle du groupe (vs. entité France) dans la décision finale est inconnu. Action :
demander explicitement si la décision peut être prise au niveau France ou nécessite une validation
groupe."]

---

## P — Paper Process
*Le processus contractuel et administratif : legal, procurement, sécurité, compliance.*

**Signal commercial :**
[Ex : "Le prospect mentionne un délai de 3 semaines pour les revues légales standard.
Pas d'information sur les exigences de sécurité ou compliance."]

**Corroboration externe :**
[Rechercher les politiques d'achat ou de compliance publiées, les certifications exigées
(ISO 27001, SOC2, RGPD, secteur régulé), les avis clients mentionnant des délais de
contractualisation longs. Ex : "L'entreprise est cotée en bourse — les contrats >100k€
nécessitent probablement une validation conseil d'administration selon les statuts publics
(AMF, rapport gouvernance 2024)."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "AMBER — Délai legal annoncé mais exigences de sécurité et niveau de contractualisation
groupe non clarifiés."]

**Angle mort :**
[Ex : "Si l'entreprise est soumise à des audits de sécurité (secteur bancaire, santé, défense),
le processus de certification peut allonger le closing de 4 à 8 semaines. Action : envoyer
le questionnaire sécurité dès maintenant, ne pas attendre la phase de négociation."]

---

## I — Identify Pain
*La douleur critique qui rend le statu quo intenable. La raison pour laquelle ils doivent agir.*

**Signal commercial :**
[Ex : "Le Directeur Commercial se plaint d'un taux de rétention des commerciaux de 60 % et
d'un onboarding qui prend 6 mois. Pas de chiffrage financier de l'impact."]

**Corroboration externe :**
[Rechercher des signaux publics de la douleur : recrutements massifs en sales (turnover ?),
avis Glassdoor sur les conditions commerciales, mentions dans des interviews d'une priorité
liée au problème, couverture de la presse sur des difficultés sectorielles.
Ex : "12 offres d'emploi de commerciaux ouvertes simultanément sur LinkedIn (juin 2026) —
signal fort de turnover ou d'expansion rapide. Le PDG dans une interview CB News (fév. 2025)
évoque 'la nécessité de scaler l'équipe commerciale sans perdre en qualité'."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "VERT — Douleur confirmée par le commercial ET corroborée par des signaux publics
indépendants. Impact financier à quantifier."]

**Angle mort :**
[Ex : "L'impact financier annuel du turnover commercial n'a pas été calculé conjointement.
Sans ce chiffre, le ROI reste abstrait. Action : proposer un exercice de quantification
lors du prochain appel (coût de remplacement = 150 % du salaire annuel selon Gallup)."]

---

## C — Champion
*L'allié interne qui veut que vous gagniez, a accès à l'Economic Buyer, et peut influencer la décision.*

**Signal commercial :**
[Ex : "Contact principal : Responsable Sales Ops. Il est enthousiaste, partage régulièrement
du contenu en interne, mais son niveau d'influence sur le CFO est inconnu."]

**Corroboration externe :**
[Rechercher le profil LinkedIn du Champion : ancienneté dans l'entreprise, réseau avec le
comité de direction, prises de parole publiques, implication dans des décisions antérieures.
Ex : "Le Responsable Sales Ops [Nom] est en poste depuis 4 ans (LinkedIn, juin 2026).
Il a publié un article sur LinkedIn en mars 2025 sur 'l'optimisation du stack commercial'
— alignement idéologique avec notre proposition."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "AMBER — Champion identifié et engagé mais accès à l'Economic Buyer non confirmé.
Risque de Champion sans pouvoir réel."]

**Angle mort :**
[Ex : "Un Champion sans accès direct au CFO est un relais, pas un sponsor. Action : tester
son influence en lui demandant d'organiser une réunion stratégique avec le CFO — si il
ne peut pas, escalader la stratégie de sponsorship."]

---

## C — Competition
*Les alternatives évaluées par le prospect : concurrents directs, solutions internes, statu quo.*

**Signal commercial :**
[Ex : "Le prospect évalue 2 autres solutions. Il mentionne un concurrent direct (nom connu)
et une option de développement interne. Pas de détail sur le stade d'évaluation des concurrents."]

**Corroboration externe :**
[Rechercher des comparatifs publics (G2, Gartner Peer Insights), des signaux de partenariat
ou d'intégration existants entre le prospect et des concurrents, des offres d'emploi
mentionnant des outils concurrents, des commentaires d'anciens employés sur Glassdoor.
Ex : "Un ancien commercial de [NomCompte] mentionne '[Concurrent]' dans son profil LinkedIn
comme outil quotidien (LinkedIn, 2025) — signal d'un usage ou d'une intégration existante."]

**Confiance :** 🟢 / 🟡 / 🔴
[Ex : "AMBER — Concurrents identifiés mais stade de leur évaluation et critères de différenciation
du prospect inconnus."]

**Angle mort :**
[Ex : "Si le concurrent cité a déjà un pied dans l'entreprise (via une intégration existante),
la compétition est asymétrique. Action : identifier si une relation contractuelle ou technique
avec ce concurrent existe déjà avant la prochaine démonstration."]

---

## Lecture Doctrinale
*Traduction de l'état du deal dans le vocabulaire stratégique classique. Lire `references/DOCTRINE.md` avant de rédiger cette section.*

**Type de terrain (Sun Tzu — Neuf Terrains) :**
[Identifier le terrain correspondant à la position commerciale actuelle et ses implications.
Ex : "Terrain disputé — le prospect est activement sollicité par au moins deux concurrents.
Sur un terrain disputé, Sun Tzu recommande de ne pas s'attarder mais de forcer rapidement
la décision. Implication : raccourcir le cycle en obtenant un engagement de l'Economic Buyer
avant la prochaine revue de budget."]

**Risques de biais stratégiques :**
[Identifier les biais potentiels du commercial ou du management sur ce deal.
Ex : "Risque de Syndrome de Valmy — l'enthousiasme du Champion peut induire une sur-confiance
dans la qualification. Le deal affiche 3 dimensions en AMBER ; la posture doit rester
offensive mais rigoureuse, pas triomphante."]

**Ligne intérieure ou extérieure :**
[Indiquer si c'est un compte existant (ligne intérieure = avantage défensif à exploiter)
ou une conquête (ligne extérieure = nécessite une concentration de force et une fenêtre d'entrée).
Ex : "Ligne extérieure — conquête pure. Aucun historique de relation. L'approche indirecte
(Liddell Hart) recommande d'éviter l'affrontement frontal sur le prix et de concentrer
l'effort sur la création d'une asymétrie informationnelle : nous devons en savoir plus sur
leur situation que nos concurrents."]

**Recommandation stratégique :**
[Une à deux recommandations concrètes issues du raisonnement doctrinal.]
> **Action prioritaire :** [Description de l'action la plus urgente et sa justification doctrinale]
> **Action secondaire :** [Description de l'action suivante si applicable]

---

*Audit généré par le MEDDPICC Deal Audit Skill — strategiecommerciale.eu*
*Informations sourced de sources publiques datées de moins de 12 mois sauf mention contraire.*
*Si `anonymize: true` est déclaré dans TOOLS.md, remplacer tous les noms de comptes et contacts par des pseudonymes (ex : « Compte A », « Contact B »).*
