---
name: audit-potentiel-expansion-nrr
version: 1.0.0
description: >
  Cartographier la base clients d'une organisation sur trois axes (santé du compte, potentiel
  d'expansion, signaux de maturité), vérifier la réserve bloquante du taux de renouvellement net
  (NRR), puis sélectionner 3 à 5 comptes par commercial et par trimestre. Le livrable est un plan
  d'expansion trimestriel : cartographie scorée, comptes retenus par commercial, ordre du jour de
  revue d'affaires destiné à anticiper le prochain budget du client, et règles d'intégration du
  NRR au variable commercial. Déclencheurs : "audit de potentiel d'expansion", "cartographier
  notre base clients", "lignes intérieures commerciales", "sélectionner les comptes à développer",
  "revue d'affaires trimestrielle", "intégrer le NRR dans le variable". Inspiré de l'article
  « Expansion client : vos meilleurs clients sont votre prochaine victoire » : vos clients
  existants sont vos lignes intérieures, développez la position centrale avant de disperser vos
  forces. Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de
  skills, copier INSTRUCTIONS.md comme prompt système.
---

# Lignes intérieures : audit du potentiel d'expansion et NRR

Cartographie une base clients sur trois axes, applique la réserve bloquante du taux de
renouvellement net, puis sélectionne les comptes à développer dans le trimestre. Le livrable est
un plan d'expansion trimestriel : cartographie scorée, sélection de 3 à 5 comptes par commercial,
ordre du jour de revue d'affaires, et règles d'intégration du NRR au variable commercial.

> Principe doctrinal (article « Expansion client : vos meilleurs clients sont votre prochaine
> victoire ») : dans le Précis de l'Art de la Guerre (1838), Jomini formalise la supériorité de la
> position centrale. La force qui occupe le centre se déplace sur des arcs courts et bat ses
> adversaires l'un après l'autre, avant qu'ils ne se rejoignent. Un client existant est un terrain
> déjà tenu, donc un arc court ; le prospect impose le long arc de l'acquisition. Développer la
> base acquise avant de disperser les forces, c'est appliquer les lignes intérieures au
> portefeuille commercial.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare : le profil de l'organisation (taille, secteur,
offre, cycle de vente), le nombre de commerciaux, le format et la langue de sortie, les seuils de
NRR, et les connecteurs éventuels (CRM, plateforme Customer Success, analytics produit, mesure de
satisfaction).

Si `TOOLS.md` est absent ou vide : mode dégradé gracieux, analyse sur les données fournies seules,
sortie Markdown, français, profil générique, seuils doctrinaux (NRR bloquant à 90 %, NRR prudent
à 100 %, 3 à 5 comptes par commercial et par trimestre). Aucun nouvel outil n'est requis : la
méthode s'appuie sur des données que l'organisation possède déjà.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Export fourni** | Fichier ou extraction (CSV, feuille, copier-coller) : usage, satisfaction, incidents, produits, sites, NRR | Normaliser les colonnes, puis cartographier |
| **Connecteur déclaré** | Accès CRM ou plateforme Customer Success opérationnel via `TOOLS.md` | Extraire la base et les indicateurs, puis cartographier |
| **Aucune donnée** | Rien de fourni | Reconstituer la cartographie par entretien structuré (Étape 1c) |

### 0c. Confirmer les entrées minimales

Demander (seulement si absent) :

1. **Le périmètre** retenu (une base, un segment, ou un portefeuille par commercial)
2. **Le nombre de commerciaux** et, si possible, la répartition des comptes
3. **Le NRR** du périmètre sur les douze derniers mois, avec sa base de calcul
4. **Par compte** : usage, NPS ou CSAT, incidents, divisions et sites couverts, produits souscrits
5. **Les signaux récents** : promotion d'un champion, budget nouveau, évolution réglementaire

Si l'utilisateur dit « lance-toi » avec un export seul : procéder en mode Export fourni.

---

## Étape 1 : Constituer le corpus des comptes

### 1a. Périmètre

Un seul périmètre à la fois : une base, ou un portefeuille par commercial. Mêler segments et
cycles de vente différents rend l'indice de priorité ininterprétable. La cible est la base clients
entière ; si elle dépasse la capacité de lecture, la scinder par segment homogène.

### 1b. Colonnes à extraire

Pour chaque compte : identifiant, segment, propriétaire (rôle commercial), ancienneté, usage du
produit, NPS ou CSAT daté, incidents des 90 derniers jours, divisions ou unités non couvertes,
produits souscrits et non adoptés, sites ou filiales hors périmètre, dernier signal de maturité
daté, et part de chiffre d'affaires.

### 1c. Reconstruction par entretien (si aucune donnée)

Si les données d'usage ou de satisfaction n'existent pas, reconstituer chaque compte à l'oral avec
le responsable : usage perçu, satisfaction, incidents, périmètre couvert, signaux récents. Une
valeur estimée est acceptée et **signalée comme estimée** ; une valeur inventée ne l'est jamais.

---

## Étape 2 : Cartographier la base sur les trois axes

Chaque axe est noté de 0 à 3. La grille ci-dessous est la grille de notation, à recopier telle
quelle.

| Axe | Signaux à extraire | Note 0 | Note 1 | Note 2 | Note 3 |
|-----|--------------------|--------|--------|--------|--------|
| **Santé du compte** | Usage, NPS ou CSAT, incidents | compte en risque : usage effondré, incidents ouverts | usage en recul, satisfaction sous la moyenne, ou incident non résolu | usage stable, satisfaction dans la moyenne | usage en croissance, satisfaction au-dessus de la moyenne, aucun incident majeur |
| **Potentiel d'expansion** | Divisions non couvertes, produits souscrits non adoptés, sites hors périmètre | aucun levier | un levier | deux leviers | trois leviers ou plus |
| **Signaux de maturité** | Champion promu, budget nouveau, évolution réglementaire ou sectorielle, sur 90 jours | aucun signal | un signal | deux signaux | trois signaux ou plus |

Indice de priorité = somme des trois axes, de 0 à 9. Un compte est **prioritaire** quand chaque
axe atteint au moins 2 et que le total atteint au moins 7. Cette règle reprend l'article : un
compte qui score haut sur les trois axes est le nœud central du dispositif, celui où porter les
forces d'abord. Un compte à fort potentiel mais à santé sous 2 relève de la rétention, pas de
l'expansion.

---

## Étape 3 : Appliquer la réserve bloquante du NRR

### 3a. Calculer le NRR

Taux de renouvellement net du périmètre sur douze mois glissants :

NRR = (ARR de départ + expansion et montée en gamme - rétrogradation - résiliation) / ARR de
départ.

Le NRR mesure ce que devient la base acquise en l'absence de tout nouveau client. Il se lit avec
sa période et sa base de calcul explicites.

### 3b. Les trois bandes de décision

| NRR sur douze mois | Lecture | Décision |
|--------------------|---------|----------|
| **Sous 90 %** | Positions intérieures contestées | Réserve bloquante : expansion suspendue, plan de rétention d'abord |
| **90 % à 100 %** | La base ne compense pas encore ses pertes | Expansion prudente : 1 à 2 comptes, priorité à l'adoption des produits souscrits |
| **100 % et plus** | La base croît sans nouveau logo | Expansion pleine : 3 à 5 comptes par commercial et par trimestre |

Justification : l'article pose qu'en dessous de 100 % la base perd plus vite qu'elle ne gagne, et
que **sous 90 % le terrain acquis est trop fragile : aucune tactique d'expansion ne compense une
valeur perçue insuffisante**. Concentrer la force sur un terrain qui s'effondre n'est pas une
stratégie. La réserve s'applique au périmètre mesuré ; un sous-segment sous 90 % est mis en
rétention même si la base globale est au-dessus.

---

## Étape 4 : Sélectionner 3 à 5 comptes par commercial et par trimestre

Trier les comptes prioritaires par indice décroissant, dans la limite de la bande NRR. Retenir
**3 à 5 comptes par commercial** pour le trimestre : c'est la concentration séquentielle de
l'article, l'attaque sur un objectif à la fois plutôt que la dispersion. Le plafond de 5 est ferme.

Règles de sélection : exclure les comptes du sous-segment en réserve bloquante ; écarter un compte
dont la santé est sous 2, quelle que soit sa note de potentiel ; répartir les comptes prioritaires
sur les commerciaux, en visant 3 par commercial ; attribuer à chaque compte retenu un propriétaire
en rôle, jamais un nom de personne.

---

## Étape 5 : Construire l'ordre du jour de revue d'affaires

La revue d'affaires trimestrielle n'a pas pour objet de présenter les résultats. Elle vise à
comprendre les enjeux du prochain exercice budgétaire du client **avant que le client ne sache
lui-même ce qu'il va décider**. Être à l'intérieur quand la décision se forme, c'est occuper la
position centrale. Ordre du jour type :

1. Où en sont l'exercice budgétaire en cours et le suivant : calendrier, enveloppe, arbitrages
2. Quels objectifs internes du client ont changé depuis la dernière revue
3. Quelles divisions, sites ou produits restent hors de notre périmètre, et pourquoi
4. Quels incidents ou freins d'adoption ne sont pas résolus
5. Quelle prochaine étape datée, avec quel responsable côté client

Chaque question est posée avec un fait interne en appui (usage, incident, périmètre), jamais comme
une relance commerciale.

---

## Étape 6 : Intégrer le NRR au variable commercial

Un commercial mesuré sur le seul revenu nouveau chasse le revenu nouveau. Intégrer le NRR du
portefeuille au variable rééquilibre les priorités vers l'expansion, sans séminaire de formation.
Le poids exact du NRR dans le variable est **fixé par l'organisation et documenté** ; la méthode
n'impose aucun pourcentage.

Mise en garde : un commercial qui hérite d'un portefeuille mal accompagné par ses prédécesseurs
serait pénalisé sur une base qu'il n'a pas construite. Le dispositif doit prévoir une base de
référence datée au moment de la prise de portefeuille, une progressivité les premiers mois, et une
distinction entre la rétention héritée et l'expansion produite. C'est le premier frein pratique
d'après l'article.

---

## Étape 7 : Sortie et décision

### 7a. Rédiger le plan

Lire `references/TEMPLATE.md` et produire le plan d'expansion selon cette structure exacte :
réserve bloquante NRR, cartographie des trois axes, sélection par commercial, ordre du jour de
revue d'affaires, règles d'intégration du NRR au variable, décision. Format par défaut Markdown,
nommé `plan-expansion-nrr-[Segment]-[DateJour].md`.

### 7b. Décision de sortie

Clore par une décision nette : la bande NRR retenue et ses conséquences (expansion pleine,
prudente, ou suspendue au profit de la rétention). Si l'expansion est suspendue, le plan devient
un plan de rétention et le dit explicitement. Fixer une date de réexamen du NRR au trimestre
suivant, sur le même périmètre.

---

## Contrôle qualité

Avant de livrer :

- [ ] Le périmètre est homogène (une base ou un portefeuille), pas un mélange de segments
- [ ] Chaque compte porte ses trois notes d'axe et son indice de priorité, aucun compte laissé vide
- [ ] Le NRR est calculé sur douze mois, avec sa base de calcul et sa date explicites
- [ ] La réserve bloquante est appliquée : sous 90 %, aucune sélection d'expansion
- [ ] Chaque donnée chiffrée porte sa source et sa date ; toute source de plus de douze mois est signalée comme non confirmée
- [ ] Les seuils appliqués sont explicités (axes 0 à 3, priorité à 7, NRR 90 % et 100 %, 3 à 5 comptes)
- [ ] Aucune déduction n'est présentée comme un fait : une note estimée est signalée comme estimée, un NRR non fourni n'est pas inventé
- [ ] Chaque commercial retenu a entre 3 et 5 comptes, le plafond de 5 n'est pas franchi
- [ ] L'ordre du jour de revue d'affaires vise le prochain budget du client, pas la présentation des résultats
- [ ] Les règles de variable prévoient la protection du portefeuille hérité
- [ ] Aucune donnée présente dans le livrable n'a été inventée pour combler un trou

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| NRR non calculable (pas d'ARR ni de churn daté) | Le signaler ; produire la cartographie seule et refuser de conclure sur l'expansion |
| NRR global sous 90 % | Réserve bloquante sur tout le périmètre : plan de rétention, pas d'expansion |
| Sous-segment sous 90 % dans une base au-dessus | Mettre le sous-segment en rétention, poursuivre sur le reste, le mentionner |
| Aucun champion identifié sur un compte | Réduire l'axe maturité, inscrire la recherche de champion comme préalable |
| Données d'usage ou de satisfaction absentes | Noter l'axe comme estimé et le signaler, jamais inventer une note |
| Plus de 5 comptes prioritaires pour un commercial | Trier par indice, plafonner à 5, reporter le surplus au trimestre suivant |
| Commercial avec portefeuille hérité | Dater la base de référence à la prise de portefeuille, l'exclure des pénalités de rétention héritée |
| Signal de maturité non daté | Ne pas le compter dans l'axe 3 tant que sa date n'est pas établie |
| Moins de 3 comptes prioritaires sur un périmètre | Le signaler : la contrainte est le vivier, pas la méthode |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil, seuils de NRR, connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt système autonome à copier |
| `references/TEMPLATE.md` | Avant de rédiger : structure annotée du plan d'expansion |
| `examples/exemple-expansion-nrr.md` | Pour voir une sortie complète sur un cas fictif |
