---
name: diagnostic-architecture-tarifaire
version: 1.0.0
description: >
  Conduire un diagnostic d'architecture tarifaire pour un éditeur de logiciel en trois questions
  argumentées : quelle part de la valeur existe sans usage intensif, quel risque d'exécution
  l'éditeur accepte de porter, et le modèle reste-t-il lisible. Le livrable est un rapport qui
  propose une architecture à trois étages (base réduite, variable d'usage plafonnée, contrat de
  résultat sous conditions strictes) ou qui justifie de conserver la grille en l'état.
  Déclencheurs : "diagnostic d'architecture tarifaire", "faut-il passer au prix à l'usage",
  "prix par siège ou prix au résultat", "quel modèle de tarification pour un logiciel",
  "doit-on quitter le prix par siège", "où placer la part variable". Inspiré de l'article
  « Pricing SaaS 2026 : le paradoxe 97/94 expliqué » : le prix définit le terrain de bataille, et
  l'asymétrie consiste à choisir son terrain plutôt qu'à livrer bataille sur celui de
  l'adversaire. Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système
  de skills, copier INSTRUCTIONS.md comme prompt système.
---

# Diagnostic d'architecture tarifaire

Diagnostique l'architecture de prix d'un éditeur de logiciel en partant de la forme de sa valeur,
puis propose une architecture à trois étages argumentée, question par question. Le livrable est un
rapport de diagnostic tarifaire : trois réponses chiffrées et sourcées, une recommandation
d'architecture, et la décision de mouvement à instrumenter.

> Principe doctrinal (article « Pricing SaaS 2026 : le paradoxe 97/94 expliqué ») : Sun Tzu,
> chapitre 6, « L'eau suit la forme du terrain », et chapitre 3, « Gagner sans combattre, c'est le
> sommet de l'art de la guerre ». Le prix définit le terrain. Facturer par siège, c'est désigner
> l'effectif du client comme unité de mesure ; facturer au résultat, c'est désigner son incertitude.
> Edward Luttwak nomme la conséquence : un avantage ne vaut que tant qu'il reste minoritaire, et
> l'asymétrie consiste à choisir un terrain que la foule ne peut pas copier vite. Le diagnostic
> tarifaire est l'acte par lequel on refuse de livrer bataille sur le terrain du prix par siège.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare : le profil de l'offre (typologie de produit,
structure de coûts, base installée), le format et la langue de sortie, la profondeur d'analyse, et
les connecteurs éventuels (facturation, analytics produit).

Si `TOOLS.md` est absent ou vide : mode dégradé gracieux, diagnostic mené par entretien dirigé,
sortie Markdown, français, profil générique. La méthode ne requiert aucun outil : elle s'appuie
sur la grille tarifaire en vigueur et sur ce que l'éditeur sait de sa propre valeur.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Valeur documentée** | Grille tarifaire, suivi d'usage, données de rétention fournis | Normaliser les mesures, puis diagnostiquer |
| **Connecteur déclaré** | Accès facturation et analytics produit opérationnel via `TOOLS.md` | Extraire la répartition base et usage, puis diagnostiquer |
| **Aucune donnée** | Rien de fourni | Reconstituer par entretien dirigé (Étapes 1 à 4) |

### 0c. Confirmer les entrées minimales

Demander (seulement si absent) : la grille tarifaire en vigueur (unité facturée, paliers, plafonds,
remises) ; la structure de coûts (part fixe et part variable par client) ; la part de valeur obtenue
sans usage intensif ; les capacités de l'éditeur (mesure des résultats, action sur ces résultats) ;
la typologie de clientèle et sa sensibilité à la prévisibilité, puis le canevas de facture actuel.

Si l'utilisateur dit « lance-toi » avec la grille tarifaire seule : procéder en mode Aucune donnée.

---

## Étape 1 : Cartographier la valeur

### 1a. Inventorier les composantes de valeur

Lister les composantes de valeur du produit, sans les confondre avec ses fonctionnalités. Une
composante de valeur est ce que le client obtient, pas ce que l'outil fait : socle de données,
reporting fiable, leads qualifiés, transactions traitées, économies réalisées, conformité.

### 1b. La grille de cartographie

Recopier et remplir ce tableau, une ligne par composante :

| Composante de valeur | Existe sans usage intensif | Mesure disponible | Unité facturable naturelle |
|----------------------|----------------------------|-------------------|----------------------------|
| Socle de données | Oui | Non requise | Abonnement à la plateforme |
| Reporting récurrent | Oui | Non requise | Abonnement à la plateforme |
| Leads qualifiés | Non | Oui, télémétrie produit | Résultat livré |
| Transactions traitées | Non | Oui, compteur d'événements | Volume d'usage |
| Économies réalisées | Non | Partielle, dépend du client | Part de résultat |

Si aucune mesure n'est disponible, reconstituer chaque ligne par entretien avec les équipes produit
et service client, en posant la question du test 80/20 (Étape 2a). Une estimation est acceptée et
**signalée comme estimation** ; elle n'est jamais présentée comme une mesure.

---

## Étape 2 : Première question, quelle part de la valeur existe sans usage intensif

### 2a. Le test 80/20

Question posée à l'éditeur : si un client n'utilise le produit qu'à 20 % de son usage habituel, quel
pourcentage du bénéfice perçu conserve-t-il ?

- Un client qui obtient **80 % du bénéfice avec 20 % de l'usage** : la valeur est principalement
  prévisible, et un prix à l'usage est un contresens. La base porte l'essentiel du prix.
- Un client qui obtient **moins de 50 % du bénéfice avec 20 % de l'usage** : la valeur est
  principalement variable, et une composante d'usage ou de résultat est légitime.

### 2b. Le seuil de répartition

| Part de valeur prévisible | Lecture | Implication |
|---------------------------|---------|-------------|
| 70 % et plus | Valeur de socle | La base porte l'essentiel du prix |
| Entre 50 % et 70 % | Valeur mixte | Architecture équilibrée, variable calibrée sur la part variable |
| Moins de 50 % | Valeur d'usage | La variable porte l'essentiel du prix |

Ces seuils sont ceux de la méthode. Ils se justifient par la structure de coûts et par la sensibilité
du client à la prévisibilité, ils ne sont pas des mesures de marché. Un seuil choisi autrement doit
être justifié par écrit dans le rapport.

Nommer le contresens s'il existe : si la valeur est prévisible et que la grille facture à l'usage,
le client paie une variation qu'il ne perçoit pas, et l'instabilité se paie en litiges.

---

## Étape 3 : Deuxième question, quel risque d'exécution l'éditeur accepte de porter

### 3a. Ce que le contrat de résultat transfère

Une composante facturée au résultat transfère le risque d'exécution du client vers l'éditeur. Si le
résultat n'est pas obtenu, l'éditeur n'est pas payé, même lorsque le produit a fonctionné. Ce
transfert n'est acceptable que s'il est accompagné de deux capacités.

### 3b. Les deux capacités obligatoires

| Capacité | Question de contrôle | Verdict si absente |
|----------|----------------------|--------------------|
| **Capacité de mesure** | Le résultat est-il mesuré automatiquement, de façon fiable et vérifiable par le client ? | Part au résultat invérifiable, donc contestable |
| **Capacité d'action** | L'éditeur a-t-il des leviers réels sur ce résultat, ou dépend-il de l'adoption et des données du client ? | Part au résultat qui est une remise déguisée |

Si l'une des deux capacités manque, le diagnostic écarte la composante au résultat. Une part au
résultat sans mesure ou sans action n'est pas un modèle, c'est une remise accordée sous un nom qui
la rend difficile à comptabiliser.

Le transfert se paie aussi côté client : une grille au résultat rend sa facture imprévisible, et un
client qui ne contrôle pas son résultat ne peut pas anticiper son coût. Évaluer le risque par segment.

---

## Étape 4 : Troisième question, le modèle reste-t-il lisible

### 4a. Les trois tests de lisibilité

| Test | Question posée | Seuil de méthode |
|------|-----------------|------------------|
| Prévisibilité | Le client peut-il anticiper sa facture du mois suivant ? | Écart de plus ou moins 10 % entre facture anticipée et facture reçue |
| Explicabilité | Le client peut-il citer les trois principaux facteurs de variation ? | Trois facteurs nommables sans assistance |
| Vérifiabilité | Le client peut-il vérifier lui-même les lignes déclencheuses ? | Chaque ligne déclencheuse consultable par le client |

Ces seuils sont ceux de la méthode : au-delà d'un écart de plus ou moins 10 %, la facture cesse
d'être anticipable, et une ligne déclencheuse invérifiable ouvre le litige.

### 4b. Le coût de l'illisibilité

Une facture incompréhensible fabrique des litiges et des désabonnements. Chiffrer ce coût avec les
données de l'éditeur : volume de réclamations de facturation sur les douze derniers mois, délai
moyen de résolution, taux de rétention des comptes ayant contesté une facture. Si ces données sont
absentes, le signaler et rester qualitatif, sans inventer de taux.

---

## Étape 5 : Proposer une architecture à trois étages

### 5a. Les trois étages

| Étage | Fonction | Calibrage | Garde-fou |
|-------|----------|-----------|-----------|
| **Base réduite** | Couvre l'accès au socle et les coûts fixes | Réduite par rapport à l'ancien prix par siège | Abaisser la barrière d'entrée sans perdre la couverture des coûts |
| **Variable d'usage plafonnée** | Capte la valeur réellement variable | Proportionnelle à l'exploitation réelle du produit | Plafond qui protège la prévisibilité du client |
| **Contrat de résultat** | Lie une part de la rémunération à des objectifs précis | Réservé à une poignée de comptes stratégiques | Conditions d'éligibilité strictes, jamais un produit de masse |

### 5b. Conditions d'éligibilité et règle d'asymétrie

Un contrat de résultat s'ouvre uniquement si cinq conditions sont réunies : capacité de mesure
fiable, capacité d'action réelle, données du client propres, engagement de son équipe, durée
minimale du contrat. Si une condition manque, l'étage reste fermé pour ce compte.

Le troisième étage n'est pas un produit de masse, c'est un instrument de sélection des batailles
que l'on accepte de livrer. L'étendre à tous les comptes revient à livrer bataille sur un terrain
que l'on ne maîtrise pas, ce que Sun Tzu (chapitre 6) déconseille.

---

## Étape 6 : Sortie et décision

### 6a. Rédiger le rapport

Lire `references/TEMPLATE.md` et produire le rapport de diagnostic selon cette structure exacte :
les trois réponses aux trois questions, la cartographie de la valeur, l'architecture proposée et le
mouvement retenu. Format par défaut Markdown, nommé
`diagnostic-tarifaire-[Offre]-[DateJour].md`.

### 6b. Retenir un seul mouvement, et l'instrumenter

Clore le rapport par une décision : **un seul mouvement**, soit la reconfiguration d'un étage de la
grille, soit la confirmation de la grille en l'état avec sa justification. Quatre chantiers ouverts
en même temps diluent l'effort et ne produisent aucune preuve.

Fixer la mesure qui prouvera l'effet du mouvement : rétention des petits comptes, volume de
réclamations de facturation, part du revenu portée par la variable, conversion de la base.
Réinstrumenter un trimestre plus tard, sans élargir le périmètre.

---

## Contrôle qualité

Avant de livrer :

- [ ] La cartographie couvre les composantes de valeur, pas les fonctionnalités
- [ ] Les trois questions sont traitées et argumentées, aucune n'est laissée sans réponse
- [ ] Le test 80/20 est appliqué avec la réponse de l'éditeur, signalée comme mesure ou estimation
- [ ] Les deux capacités (mesure, action) sont évaluées avant toute part au résultat
- [ ] Les trois tests de lisibilité sont passés au canevas de facture réel
- [ ] Chaque donnée chiffrée porte sa source et sa date ; toute source de plus de douze mois est signalée comme non confirmée
- [ ] Les seuils de méthode (80/20, 70 %, 50 %, plus ou moins 10 %) sont présentés comme tels, pas comme des données de marché
- [ ] Aucune déduction n'est présentée comme un fait : une estimation de la part de valeur est signalée comme estimation, une mesure absente n'est pas inventée
- [ ] L'architecture proposée est calibrée sur la valeur diagnostiquée, pas copiée d'un modèle dominant
- [ ] Le rapport se termine par un seul mouvement et une mesure d'effet datée

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Grille tarifaire absente | Reconstituer par entretien, ou demander la grille avant de conclure |
| Aucune mesure d'usage disponible | Estimer la part de valeur par entretien et signaler l'estimation |
| Capacité de mesure du résultat absente | Écarter la part au résultat, la signaler comme remise déguisée si maintenue |
| Capacité d'action absente | Fermer le troisième étage pour le compte concerné |
| Modèle illisible sur le canevas réel | Proposer d'abord un travail de lisibilité, avant toute reconfiguration |
| Éditeur voulant passer au résultat pur | Rappeler le transfert de risque et les deux capacités, ne pas valider sans elles |
| Aucune donnée de litige de facturation | Rester qualitatif sur le coût de l'illisibilité, ne pas inventer de taux |
| Comparaison avec une enquête de marché | Rappeler que le diagnostic porte sur la valeur de cet éditeur, pas sur une tendance |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil de l'offre, format de sortie, connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt système autonome à copier |
| `references/TEMPLATE.md` | Avant de rédiger : structure annotée du rapport de diagnostic |
| `examples/exemple-diagnostic-tarifaire.md` | Pour voir une sortie complète sur un cas fictif |
