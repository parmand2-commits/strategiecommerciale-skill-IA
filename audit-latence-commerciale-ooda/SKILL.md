---
name: audit-latence-commerciale-ooda
version: 1.0.0
description: >
  Auditer la latence commerciale d'un segment en mesurant quatre latences sur les vingt dernières
  opportunités : délai entre le premier signal et la première action humaine, sources tierces ayant
  construit le cadrage du comité d'achat, rapport entre les réunions internes du comité et les
  réunions menées avec le vendeur, et délai entre l'accord verbal et la signature. Le livrable
  classe les dossiers selon qui mène la boucle (le vendeur ou le comité) et chiffre le coût de
  la latence en écart de conversion. Déclencheurs : "audit de latence commerciale", "mesurer notre
  tempo de vente", "boucle OODA commerciale", "pourquoi nos deals traînent", "coût de la lenteur
  commerciale", "qui mène la boucle d'achat". Inspiré de l'article « Boucle OODA : reprendre le
  tempo de la décision commerciale » : l'orientation commande la décision, et le tempo se gagne
  en s'insérant dans la boucle de l'acheteur. Compatible avec tout agent (Claude, ChatGPT, Gemini,
  Perplexity) : sans système de skills, copier INSTRUCTIONS.md comme prompt système.
---

# Boucle OODA : Audit de latence commerciale

Mesure la latence entre le pilotage interne d'une organisation commerciale et la boucle de
décision réelle d'un comité d'achat. Le livrable est un rapport de latence : quatre mesures
chiffrées sur les vingt dernières opportunités d'un même segment, un classement des dossiers
selon qui mène la boucle, et le coût de la latence en écart de conversion.

> Principe doctrinal (article « Boucle OODA : reprendre le tempo de la décision commerciale ») :
> dans le briefing de John Boyd de janvier 1996, The Essence of Winning and Losing, l'orientation
> occupe le centre de la figure et commande le reste. Un comité d'achat se réoriente avant de
> décider, et il le fait en votre absence. Le pipeline décrit un processus interne ; la décision
> se prend en boucle. Mesurer l'écart entre les deux, c'est retrouver le tempo perdu.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare : le profil de l'organisation (taille, secteur,
cycle de vente), le format et la langue de sortie, la profondeur d'analyse, et les connecteurs
éventuels (CRM, plateforme de signaux).

Si `TOOLS.md` est absent ou vide : mode dégradé gracieux, analyse sur les données fournies seules,
sortie Markdown, français, profil générique. Aucun outil de recherche n'est requis pour le calcul :
la méthode s'appuie sur des dates que l'organisation possède déjà.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Export CRM** | Fichier ou extraction fournie (CSV, feuille, copier-coller) | Normaliser les colonnes, puis mesurer |
| **Connecteur déclaré** | Accès CRM opérationnel via `TOOLS.md` | Extraire les vingt dernières opportunités du segment, puis mesurer |
| **Aucune donnée** | Rien de fourni | Reconstituer le corpus par entretien structuré (Étape 1c) |

### 0c. Confirmer les entrées minimales

Demander (seulement si absent) :

1. **Le segment** retenu (un seul segment à la fois : même marché, même typologie de comité)
2. **Les vingt dernières opportunités** de ce segment, closes ou non
3. **Les dates d'étape** disponibles dans le CRM, et le **résultat** de chaque dossier
4. **La valeur** de chaque dossier, si le coût de la latence doit être chiffré en montant

Si l'utilisateur dit « lance-toi » avec un export seul : procéder en mode Export CRM.

---

## Étape 1 : Constituer le corpus des vingt dossiers

### 1a. Périmètre

Un segment unique, les vingt dernières opportunités, closes ou en cours. Le périmètre restreint
est une condition de validité : mêler segments et cycles différents rend le rapport entre réunions
et le délai de signature ininterprétables.

### 1b. Colonnes à extraire

Pour chaque dossier : identifiant, date du premier signal détecté, date de la première action
humaine, sources tierces citées avant la première réunion, réunions internes du comité (estimées),
réunions menées avec le vendeur, date de l'accord verbal, date de signature (ou absence), résultat
(gagné, perdu, en cours), valeur.

### 1c. Reconstruction par entretien (si aucune donnée)

Si le CRM ne porte pas les dates utiles, reconstituer chaque dossier à l'oral, avec le
responsable du dossier : signal, première action, accord verbal, signature. Une date estimée est
acceptée et **signalée comme estimée** ; une date inventée ne l'est jamais.

---

## Étape 2 : Mesurer les quatre latences

Chaque latence correspond à un étage de la boucle. Le tableau ci-dessous est la grille de mesure,
à recopier telle quelle.

| Boucle | Donnée à extraire | Seuil d'alerte | Propriétaire |
|--------|-------------------|----------------|--------------|
| **Observer** | Délai entre la date du premier signal détecté et la date de la première action humaine | Plus de 24 heures ouvrées | Première ligne, pilotage RevOps |
| **S'orienter** | Nombre de sources tierces ayant construit le cadrage du comité avant la première réunion avec vous | Aucune source tierce | Champion, appuyé par le marketing produit |
| **Décider** | Réunions internes estimées du comité, divisées par les réunions menées avec vous | Rapport supérieur à 3 | Account executive |
| **Agir** | Délai entre l'accord verbal et la signature | Plus de 30 jours sans raison documentée | Sales manager |

### 2a. Observer

Un signal est un événement observable qui modifie la situation d'un client : recrutement sur un
poste lié à votre périmètre, appel d'offres, publication de direction, visite de la page de tarifs,
changement d'outil concurrent. Mesurer le délai en **heures ouvrées**. Justification du seuil :
au-delà de 24 heures ouvrées, le dossier retourne dans une file d'attente et le comité a une
semaine d'avance (article, manœuvre 1).

### 2b. S'orienter

Pour chaque dossier, documenter ce qui a construit la compréhension du problème par le comité
avant de vous parler. Trois réponses suffisent : les tiers consultés en dehors de vous et du
champion, le pair ou la référence vers lesquels le comité s'est tourné, le cadrage qu'il a retenu
spontanément. **L'absence de toute source tierce est l'alerte** : un comité qui n'a lu que vous
n'a pas commencé à s'orienter, et vous portez son travail d'analyse.

### 2c. Décider

Compter, dossier par dossier, les réunions internes du comité (estimées) et les réunions tenues
avec vous, puis calculer le rapport. Un rapport **supérieur à 3** signale un comité qui travaille
sans vous. L'information est neutre tant qu'aucune de vos productions n'est citée en réunion
interne ; elle devient une alerte dès que le rapport dépasse 3 sans citation.

### 2d. Agir

Mesurer le délai entre l'accord verbal et la signature. **Au-delà de 30 jours sans raison
documentée**, une réorientation a eu lieu ou un fournisseur est revenu dans la discussion
(article, manœuvre 3). Documenter la raison quand elle existe ; ne pas l'inventer quand elle
manque.

### 2e. Tableau des latences

Produire un tableau : une ligne par dossier, une colonne par latence mesurée, et le seuil franchi
signalé. Puis une ligne de synthèse par latence : délai médian observé, nombre de dossiers en
alerte, écart au seuil.

---

## Étape 3 : Classer les dossiers selon qui mène la boucle

### 3a. La colonne du tempo

Pour chaque transition d'un dossier (signal vers action, étape vers étape, accord vers signature),
établir qui a bougé en premier : le vendeur ou le comité. C'est la seule colonne qui change le
pilotage, et celle que personne ne remplit spontanément (article, jour 3).

### 3b. Le classement

| Classement | Signal | Lecture |
|------------|--------|---------|
| **Le vendeur mène** | Le vendeur a déclenché la majorité des transitions | Tempo maîtrisé, la latence est un problème d'exécution |
| **Le comité mène** | Le comité a déclenché la majorité des transitions | Tempo subi, la latence est un problème d'orientation |
| **Mixte** | Répartition proche de l'équilibre | Le dossier bascule selon l'étage ; isoler l'étage qui décroche |

Un dossier en alerte sur l'orientation (aucune source tierce) et mené par le comité est le
profil le plus coûteux : vous fournissez les critères de comparaison et la lecture du problème,
c'est-à-dire le travail de l'acheteur.

---

## Étape 4 : Chiffrer le coût de la latence

### 4a. Écart de conversion

Calculer le taux de conversion de chaque colonne du classement :

- **Taux de conversion, dossiers menés par le vendeur** = gagnés / total de la colonne
- **Taux de conversion, dossiers menés par le comité** = gagnés / total de la colonne
- **Écart de conversion** = différence en points de pourcentage

L'écart obtenu chiffre le coût de votre latence (article, jour 4) : c'est ce que vous laissez sur
la table à chaque fois que le comité mène la boucle.

### 4b. Traduction en montant (si les valeurs sont fournies)

Coût de la latence = écart de conversion × volume annuel du segment × valeur moyenne du dossier.
Si les valeurs ne sont pas fournies, rester en points de pourcentage et en nombre de dossiers, et
le signaler. Aucun montant n'est estimé sans base de calcul explicite.

### 4c. Lecture des ordres de grandeur

Deux repères externes encadrent la lecture. Selon Gartner (communiqué du 19 mai 2026, enquête
auprès de 210 directeurs commerciaux et dirigeants, recueil de janvier à février 2026), les outils
d'IA font gagner en moyenne 4,8 heures par semaine à un vendeur, mais 72 % des organisations
réinvestissent peu ce temps, et celles qui le réinvestissent sont 3,1 fois plus susceptibles de
dépasser leurs objectifs de conversion. Selon Gartner (The B2B Buying Journey, date de publication
non précisée par la source), 17 % seulement du parcours d'achat se passe en réunion avec des
fournisseurs. Ces repères situent l'enjeu, ils ne remplacent pas la mesure interne.

---

## Étape 5 : Sortie et décision

### 5a. Rédiger le rapport

Lire `references/TEMPLATE.md` et produire le rapport de latence selon cette structure exacte :
tableau des quatre latences, classement du tempo, écart de conversion, coût de la latence,
chantier retenu. Format par défaut Markdown, nommé `audit-latence-[Segment]-[DateJour].md`.

### 5b. Retenir un seul chantier

Clore le rapport par une décision : **un seul chantier parmi les quatre**, choisi en visant la
latence la plus longue rapportée à son coût. La mesure est réinstrumentée un mois plus tard, sans
élargir le périmètre (article, jour 5). Quatre chantiers ouverts en même temps diluent l'effort et
ne produisent aucune preuve.

---

## Contrôle qualité

Avant de livrer :

- [ ] Le corpus porte sur les vingt dernières opportunités d'un segment unique
- [ ] Les quatre latences sont mesurées pour chaque dossier, aucun dossier laissé vide
- [ ] Chaque donnée chiffrée porte sa source et sa date ; toute source de plus de douze mois est signalée comme non confirmée
- [ ] Les seuils appliqués sont explicités (24 heures ouvrées, aucune source tierce, rapport supérieur à 3, plus de 30 jours)
- [ ] Le classement du tempo est établi dossier par dossier, pas par impression
- [ ] L'écart de conversion est calculé entre les deux colonnes, en points de pourcentage
- [ ] Aucune déduction n'est présentée comme un fait : une date estimée est signalée comme estimée, une valeur non fournie n'est pas inventée
- [ ] Le rapport se termine par un seul chantier retenu et une date de réinstrumentation
- [ ] Aucune donnée présente dans le livrable n'a été inventée pour combler un trou

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Moins de vingt dossiers disponibles | Le signaler ; mesurer sur ce qui existe et noter la fragilité du rapport |
| Dates de signal absentes du CRM | Reconstituer par entretien ou marquer la latence « non mesurable », jamais estimer en silence |
| Segment mixte fourni | Demander de restreindre à un segment, ou scinder le rapport en deux |
| Valeurs de dossiers absentes | Rester en points de pourcentage et en nombre de dossiers, le mentionner |
| Réunions internes du comité inconnues | Utiliser l'estimation du champion et la signaler comme estimation |
| Aucune source tierce sur tous les dossiers | Traiter comme un signal d'orientation global, pas comme un accident de dossier |
| Résultats de dossiers en cours | Les exclure du calcul de conversion, ou les compter séparément |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil, format de sortie, connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt système autonome à copier |
| `references/TEMPLATE.md` | Avant de rédiger : structure annotée du rapport de latence |
| `examples/exemple-audit-latence.md` | Pour voir une sortie complète sur un cas fictif |
