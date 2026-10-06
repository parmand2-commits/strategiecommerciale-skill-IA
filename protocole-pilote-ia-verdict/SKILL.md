---
name: protocole-pilote-ia-verdict
version: 1.0.0
description: >
  Cadrer un pilote d'IA commerciale à métrique unique et rendre un verdict daté à chaque revue
  trimestrielle. Le livrable est un protocole de pilote (métrique, baseline mesurée avant le
  lancement, seuil écrit, périmètre gelé, indicateurs avancés), puis un verdict de conseil de
  guerre (continuer, ajuster, couper), avec la règle de coupe appliquée après deux revues.
  Déclencheurs : "pilote IA", "mesurer le ROI de l'IA commerciale", "métrique unique du pilote",
  "conseil de guerre trimestriel", "baseline avant lancement", "faut-il couper cet outil", ou
  toute décision de poursuite, d'ajustement ou d'arrêt d'un déploiement d'IA commerciale.
  Inspiré de l'article « La Friction de Clausewitz : mesurer le ROI de votre IA commerciale » :
  la friction ne se supprime pas, elle se mesure et se gère.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Protocole de pilote IA et verdict de conseil de guerre

Cadre un pilote d'IA commerciale de bout en bout : une métrique, une baseline mesurée avant le
lancement, un seuil écrit, un périmètre gelé, des indicateurs avancés lus dans les outils existants,
puis un conseil de guerre trimestriel qui rend un verdict daté. Un pilote qui démarre sans baseline
ne produit pas un ROI, il produit une anecdote.

> Principe doctrinal (article « La Friction de Clausewitz : mesurer le ROI de votre IA
> commerciale ») : Clausewitz nomme friction l'écart permanent entre le plan et son exécution
> (ordres en retard, unités égarées, poudre détrempée). La friction ne se supprime pas, elle se
> mesure et se gère : un déploiement d'IA sans compteur revient à envoyer des troupes sans service
> de rapport. La mesure n'est pas une formalité, c'est l'organe de commandement. Le déploiement a
> distancé la preuve : 74 % des organisations ont de l'IA en production et près de la moitié ne
> peut pas démontrer ce qu'elle rapporte (Forbes, Sandy Carter, 6 août 2026).

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare : le profil de l'organisation, les outils
existants et la donnée qu'ils tracent, la métrique visée, le format de sortie et la langue. Si le
fichier est absent ou vide : mode dégradé, sortie Markdown, français, et le cadrage se conduit par
questions.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Cadrage** (défaut) | Nom d'un outil ou d'un cas d'usage IA, volonté de lancer | Construire le protocole complet (Étapes 1 à 4) |
| **Revue** | « conseil de guerre », « revue trimestrielle », données d'adoption et de métrique fournies | Passer aux trois lectures croisées (Étape 5) et rendre le verdict (Étape 6) |
| **Complet** | Pilote déjà lancé, l'utilisateur veut protocole et grille de revue | Vérifier la baseline (Étape 1), produire protocole et gabarit de revue |

### 0c. Confirmer les entrées minimales

Demander (seulement si absent) :
1. **Cas d'usage du pilote** : quel processus commercial l'IA touche (préparation d'appel, rédaction, closing)
2. **Population concernée** : nombre de commerciaux et rôles
3. **Outils déjà en place** et la donnée qu'ils tracent, pour la baseline et les indicateurs avancés
4. **Dates** : lancement prévu, date de la première revue trimestrielle
5. **Coûts connus** : licences, intégration, supervision

> Règle de preuve, valable dans tous les modes : toute donnée chiffrée porte sa source et sa date.
> Une source de plus de 12 mois est rejetée ou signalée « information non confirmée (>12 mois) ».
> Une déduction n'est jamais présentée comme un fait : une valeur non mesurée est marquée
> « non mesurée ».

## Étape 1 : La métrique unique et la baseline

### 1a. Choisir une seule métrique (lagging)

Une métrique commerciale, une seule, choisie avant le premier jour du pilote. L'appariement suit
l'objectif du déploiement :

| Cas d'usage de l'IA | Métrique unique proposée |
|---|---|
| Assistant de préparation d'appel | temps de préparation ou taux de qualification |
| Assistant de rédaction | taux de réponse |
| Copilote de closing | win rate |

La métrique unique est le lagging indicator : le résultat stratégique qui se juge après coup. Un
pilote jugé sur plusieurs indicateurs ne peut pas être jugé du tout. Sa justification tient en une
phrase : quel objectif du déploiement elle touche, quelle décision elle éclaire. Une métrique qui
n'éclaire aucune décision est un tableau de bord décoratif.

### 1b. Mesurer la baseline avant le lancement

Mesurer la valeur de référence avant le premier jour, sur une fenêtre comparable (même périmètre,
même durée, même définition du calcul). Noter valeur, fenêtre, source et date de mesure.

Règle : si la donnée n'existe pas avant le lancement, elle n'existera pas après. C'est le premier
signal de friction. Dans ce cas, ne pas fixer de seuil : déclarer le protocole inexploitable et
proposer de mesurer la baseline pendant une période de référence (par exemple 4 semaines) avant de
lancer.

## Étape 2 : Le seuil écrit et le périmètre gelé

### 2a. Écrire le seuil

Le seuil de succès est fixé par écrit avant le lancement : une valeur chiffrée, une fenêtre de
mesure, le mode de comparaison à la baseline (écart absolu ou relatif). Défaut proposé, à valider
avec le commanditaire et à justifier : une amélioration relative de 20 % de la métrique sur
12 semaines.

Ajouter le **plancher d'adoption** : la part minimale de la population qui doit réellement utiliser
l'outil pour que la métrique soit interprétable (par exemple 60 % des licences avec un usage
hebdomadaire). Un seuil de performance sans plancher d'adoption produit un verdict illisible : on
ne sait pas si l'outil échoue ou s'il n'a pas été utilisé.

### 2b. Geler le périmètre

Le périmètre est gelé pour toute la durée du pilote : population, cas d'usage, métrique unique,
durée. Toute demande d'ajout (nouvel usage, nouvelle équipe, nouvel indicateur) est refusée pendant
le pilote et consignée au registre des demandes ; elle n'est examinée qu'à la revue.

Règle : la plupart des déploiements échouent par périmètre, pas par technologie. Trois cas d'usage
et quatre indicateurs lancés ensemble ne permettent d'en prouver aucun.

### 2c. Poser les critères de sortie dès le lancement

Annoncer d'avance la règle de coupe (Étape 6) : ce qui reste sous le seuil après deux revues se coupe.

## Étape 3 : Les indicateurs avancés, lus dans les outils existants

### 3a. Le principe

La métrique unique (lagging) se juge à la revue. Les indicateurs avancés (leading) se lisent en
continu, chaque semaine, dans les outils déjà en place. Le commandant qui ne lit que le résultat
découvre la friction trop tard ; celui qui lit les signaux intermédiaires la voit se former.

### 3b. Table des indicateurs avancés

| Indicateur avancé | Où il se lit | Seuil de surveillance |
|---|---|---|
| Adoption réelle (utilisateurs actifs / licences) | journal d'accès de l'outil, CRM | supérieure au plancher d'adoption |
| Temps moyen de mise à jour des données | CRM | stable ou en baisse |
| Taux de qualification à l'entrée du pipeline | CRM, revenue intelligence | stable ou en hausse |
| Longueur de cycle de vente | revenue intelligence | stable ou en baisse |
| Maîtrise des compétences commerciales clés | plateforme de renforcement | en hausse sur la population pilote |

Ne retenir que les indicateurs dont la donnée est déjà tracée avant le lancement : si la donnée
n'existe pas avant, elle n'existera pas après.

### 3c. Les quatre sources de friction à surveiller

Clausewitz décompose la friction en quatre sources. Les nommer dans le protocole, chacune comme un
angle mort du calcul : le **danger** (les erreurs qui coûtent), l'**effort** (l'adoption qui retombe
quand les commerciaux retournent à leurs habitudes), l'**incertitude** (des données de CRM
incomplètes qui faussent la métrique), le **hasard** (les événements imprévus : réorganisation,
changement de direction, crise).

## Étape 4 : Écrire le protocole (premier livrable)

Recopier `references/TEMPLATE.md` (section protocole) exactement. Le protocole tient sur une page :
cas d'usage, population, métrique unique et justification, baseline (valeur, fenêtre, source, date),
seuil, plancher d'adoption, périmètre gelé, indicateurs avancés et leurs seuils de surveillance,
sources de friction, date de la première revue, coûts connus.

Nom de fichier : `protocole-pilote-ia-[CasUsage]-[DateJour].md`, dans le dossier `output_dir`
déclaré dans `TOOLS.md` (défaut : dossier courant). Ne pas livrer un protocole sans baseline mesurée :
dans ce cas produire la version « baseline à mesurer » et le dire explicitement.

## Étape 5 : Le conseil de guerre trimestriel

Une heure par trimestre, mêmes participants, mêmes critères. Ordre du jour en quatre blocs :

1. **Adoption réelle contre licences payées** : combien d'utilisateurs actifs, à quelle fréquence, et l'écart au plancher d'adoption.
2. **Métrique mesurée contre seuil fixé** : la valeur du lagging sur la fenêtre, l'écart au seuil.
3. **Coût total contre valeur constatée** : licences, intégration, supervision, plus le temps interne consommé.
4. **Décision datée** : continuer, ajuster ou couper, avec un responsable et une échéance.

Croiser trois lectures du terrain, pour ne pas comparer des impressions : la conversation
intelligence (les commerciaux se servent-ils réellement de l'outil en rendez-vous ?), le CRM (les
données remontent-elles, à quelle vitesse ?), la revenue intelligence (le pipeline bouge-t-il ?).

Entre deux conseils de guerre, les indicateurs avancés se lisent chaque semaine ; le conseil de
guerre, lui, tranche sur le lagging. Une revue qui ne décide pas est une revue de plus.

## Étape 6 : Le verdict daté et la règle de coupe

### 6a. Grille de verdict

| Condition observée | Verdict |
|---|---|
| Métrique égale ou supérieure au seuil et adoption au-dessus du plancher | **Continuer** |
| Métrique au seuil ou au-dessus, mais adoption sous le plancher | **Ajuster** (action corrective datée sur l'adoption) |
| Métrique sous le seuil, première revue consécutive | **Ajuster** (cause racine identifiée, action corrective datée) |
| Métrique sous le seuil, deuxième revue consécutive | **Couper** et réaffecter le budget vers ce qui mesure |

Tenir un compteur de revues sous le seuil, reporté d'une revue à l'autre. Une seule revue sous le
seuil n'entraîne pas de coupe : elle déclenche une action corrective datée.

### 6b. La règle de coupe

Ce qui reste sous le seuil après deux revues se coupe. Couper un pilote n'est pas un échec, c'est
la preuve que la discipline fonctionne. Un pilote qui dure plus de deux trimestres sans décision
n'est plus un test, c'est une dépense : il consomme du budget, de l'attention et des données.

Chaque verdict est daté et assorti du nom d'un responsable unique (une personne, pas un comité).
Le budget libéré par une coupe est réaffecté vers ce qui mesure : une coupe sans réaffectation
laisse le budget disponible pour le pilote suivant, et la friction recommence.

## Étape 7 : Sortie

Deux livrables, rédigés selon `references/TEMPLATE.md`, dans le dossier `output_dir` déclaré dans
`TOOLS.md` (défaut : dossier courant) :
- `protocole-pilote-ia-[CasUsage]-[DateJour].md` (cadrage, avant lancement) ;
- `verdict-conseil-de-guerre-[CasUsage]-[AAAA-Trimestre].md` (revue trimestrielle).

Si `output_format: json` est déclaré dans `TOOLS.md`, produire un objet `verdict` avec `cas_usage`,
`date_revue`, `metrique` (`baseline`, `valeur_mesuree`, `seuil`, `ecart`), `adoption` (`licences`,
`actifs`, `plancher`, `part`), `cout_total`, `indicateurs_avances[]`, `revues_sous_seuil`,
`verdict` (`continuer|ajuster|couper`), `decision` (`date`, `responsable`) et `sources[]`.

## Contrôle qualité

- [ ] Une seule métrique commerciale est retenue, et sa justification tient en une phrase
- [ ] La baseline est mesurée avant le lancement (valeur, fenêtre, source, date) ; sinon le protocole est déclaré en mode « baseline à mesurer »
- [ ] Le seuil est chiffré, écrit, et accompagné d'un plancher d'adoption chiffré
- [ ] Le périmètre gelé est explicite et le registre des demandes existe
- [ ] Chaque indicateur avancé se lit dans un outil déjà en place avant le lancement
- [ ] Toute donnée chiffrée porte sa source et sa date ; toute source de plus de 12 mois est signalée « information non confirmée (>12 mois) »
- [ ] Aucune déduction n'est présentée comme un fait : une valeur non mesurée est marquée « non mesurée »
- [ ] Le verdict est daté, nomme un responsable unique, et prend un des trois termes continuer, ajuster, couper
- [ ] La règle de coupe est appliquée quand la métrique reste sous le seuil après deux revues
- [ ] Le compteur de revues sous le seuil est reporté d'une revue à l'autre
- [ ] Aucune promesse de ROI certain, aucune généralisation absolue, aucun ordre de grandeur sans son périmètre

## Gestion des erreurs

| Situation | Comportement |
|---|---|
| Baseline indisponible au lancement | Ne pas fixer de seuil : produire un protocole « baseline à mesurer » et planifier une période de référence |
| Demande d'ajout de périmètre en cours de pilote | La refuser, l'inscrire au registre des demandes, ne l'examiner qu'à la revue |
| Adoption non tracée par l'outil | Le signaler, proposer un proxy (activité dans le CRM) en indiquant sa faiblesse, ou une mesure manuelle hebdomadaire |
| Chiffre d'adoption ou de coût sans source | Ne pas l'utiliser comme fait, le marquer « non confirmé » et demander la source |
| Source externe de plus de 12 mois | La rejeter ou la signaler « information non confirmée (>12 mois) » |
| Aucune revue trimestrielle planifiée | Ne pas produire de protocole tant qu'aucune date de conseil de guerre n'est fixée |
| Métrique mesurée sur une fenêtre non comparable à la baseline | Ne pas conclure : recalculer sur une fenêtre comparable, sinon marquer le verdict « illisible » |

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil, outils tracés, métrique visée, format de sortie |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt système à copier |
| `references/TEMPLATE.md` | Avant de rédiger : structure du protocole et du verdict de revue |
| `examples/exemple-pilote-ia.md` | Exemple complet : protocole puis deux revues |

---

*Skill « Protocole de pilote IA et verdict » (strategiecommerciale.eu). Ancrage : article « La
Friction de Clausewitz : mesurer le ROI de votre IA commerciale » (2026).*
