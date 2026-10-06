---
name: codifier-savoir-tribal-skills
version: 1.0.0
description: >
  Transformer le savoir non écrit d'une force de vente en skills versionnées : cartographier les
  détenteurs du savoir tribal, extraire les règles maison par entretien et par analyse des
  livrables réels, tenir la revue mensuelle de deux affaires dont le livrable est un document,
  puis gérer un portefeuille de cinq à huit skills, une par moment de vérité du cycle de vente.
  Le livrable est un plan de codification, un registre de skills versionnées et le gabarit de
  revue d'affaire. Déclencheurs : "codifier notre savoir commercial", "transformer nos règles
  maison en skills", "revue d'affaires mensuelle", "portefeuille de skills", "onboarding
  commercial", "le savoir est dans la tête des seniors", "quel moment de vérité outiller".
  Inspiré de l'article « La Mémoire du Régiment : le savoir tribal de vos agents IA » : la
  supériorité ne vient pas de l'outil mais de l'état-major qui codifie, dissèque et transmet.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Codifier le Savoir Tribal en Skills Versionnées

Transforme le patrimoine non écrit d'une organisation commerciale en un corpus de skills
exploitables par des agents, versionnées, rattachées à un moment de vérité du cycle de vente.
Le livrable donne à la direction commerciale **l'état-major de Moltke** : une école, un jeu de
guerre, une section historique, une rotation. Les quatre pièces, pas seulement la première.

> Principe doctrinal (article « La Mémoire du Régiment ») : Moltke prend la tête du Grand
> État-Major prussien en 1857 et en fait le cerveau d'une armée victorieuse. Son dispositif tient
> en quatre pièces : la Kriegsakademie, le Kriegsspiel sur carte, une section historique qui
> dissèque les campagnes passées et publie ses conclusions, la rotation des officiers entre
> l'état-major et la troupe. Coder des skills sans les trois autres pièces produit un document
> qui vieillit seul. Le savoir qui gagne les affaires est celui qui n'est écrit nulle part.

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare :
- le profil de l'organisation (taille, secteur, cycle de vente, nombre de commerciaux)
- les outils connectés disponibles (CRM, conversation intelligence, entrepôt documentaire)
- les préférences de langue, format et profondeur
- le dossier de destination des skills produites

Si `TOOLS.md` est absent ou vide : mode dégradé, aucune donnée connectée, entrée fournie à la
main par l'utilisateur, sortie Markdown, profil « générique ».

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Audit complet** | « codifie notre savoir », « on veut une bibliothèque de skills » | Enchaîner les étapes 1 à 6 |
| **Revue d'affaire seule** | Un deal gagné ou perdu raconté, une défaite à comprendre | Étape 3 uniquement, avec sortie vers l'étape 4 si une règle nouvelle apparaît |
| **Portefeuille existant** | Une liste de skills déjà écrites | Étape 4 sur l'existant, puis étape 6 |
| **Diagnostic de transmission** | « nos juniors réapprennent tout », « nos seniors partent » | Étape 1 puis étape 5 |

Les modes s'enchaînent si le contexte le demande. Une revue d'affaire qui révèle trois règles
nouvelles déclenche l'étape 4.

### 0c. Confirmer les entrées minimales

Demander, seulement si absent :
1. **L'effectif commercial et l'ancienneté** (qui détient le savoir, depuis quand)
2. **Les moments de vérité du cycle** (les étapes où une affaire bascule)
3. **Le ou les seniors disponibles** pour le détachement d'un mi-temps
4. **Le rythme de revue accepté** par la direction (mensuel recommandé)
5. L'accès, même partiel, aux affaires gagnées et perdues des douze derniers mois

Sans l'entrée 5, l'audit reste possible mais l'étape 2 ne s'appuie que sur les entretiens, ce
qu'il faut signaler explicitement dans le livrable.

## Étape 1 : Cartographier le savoir tribal

### 1a. Nommer les détenteurs

Identifier les personnes qui tranchent sans consulter de document. Méthode : croiser deux
sources au lieu d'en choisir une.

- **Source déclarative** : demander à trois commerciaux et à un manager « à qui va-t-on demander
  avant de signer un contrat inhabituel ». Les mêmes noms reviennent.
- **Source comportementale** : dans le CRM ou la messagerie, repérer les fils où un senior est
  mis en copie pour arbitrer.

Le croisement donne en général trois à sept noms, jamais la liste complète de l'équipe. Une
équipe qui n'en produit aucun est elle-même le résultat de l'audit.

### 1b. Nommer les moments de vérité

Un moment de vérité est un point du cycle où une affaire change de camp, et où l'organisation
réussit ou échoue selon une règle non écrite. Les candidats habituels :
qualification initiale, premier rendez-vous de découverte, construction du dossier économique,
passage devant le comité d'achat, négociation de dernière ligne, prise de contact après signature.

Retenir **cinq à huit** moments, pas davantage. La contrainte est doctrinale : c'est le format du
portefeuille de l'étape 4. Au-delà de huit, chaque skill devient trop mince pour être utile.

### 1c. Produire la carte

Livrer un tableau unique : détenteur, moments de vérité qu'il porte, affaires récentes où sa
règle a tranché, disponibilité pour l'entretien. Cette carte est le plan de travail de l'étape 2.

## Étape 2 : Extraire les règles maison

### 2a. L'entretien de codification

Un entretien par détenteur, trente à quarante minutes, quatre questions, dans cet ordre :

1. **Racontez une affaire que vous avez sauvée et que le process n'aurait pas sauvée.**
2. **Qu'est-ce qui vous a fait changer d'avis ?** (chercher le signal concret, pas l'intuition)
3. **Qu'est-ce qu'un bon vendeur ne ferait jamais, que le process autorise ?**
4. **Comment le savez-vous ?** (chercher le contre-exemple : la fois où la règle a échoué)

La question 4 est celle qu'on oublie et c'est la seule qui sépare une règle d'une croyance. Une
règle sans contre-exemple est un ressenti : la consigner comme telle, jamais comme règle.

### 2b. L'analyse du livrable réel

Lire ce qui a réellement été envoyé, pas ce qui a été prescrit :
- les courriels de relance qui ont obtenu une réponse, à comparer à ceux qui n'en ont pas obtenu
- les comptes rendus de rendez-vous qui ont produit une étape suivante
- les propositions commerciales signées, à comparer aux propositions perdues sur le même segment

Ce que l'entretien déclare et ce que les livrables montrent ne coïncident pas toujours. En cas
d'écart, le livrable est plus fiable que le souvenir, et l'écart lui-même est un résultat à
restituer.

### 2c. Nommer les règles

Chaque règle extraite est reformulée selon un format unique :

```
Situation   : ce qui se passe sur le terrain
Signal      : ce qui doit alerter, en observable
Règle       : ce qu'on fait, en une phrase à l'impératif
Contre-exemple : le cas où la règle ne s'applique pas
Seuil       : le chiffre ou le critère qui déclenche la règle, quand il existe
```

Une règle sans signal observable n'est pas exploitable par un agent et ne doit pas devenir une
skill. La reformuler ou l'écarter, en le disant.

## Étape 3 : La revue mensuelle des deux affaires

### 3a. Le principe

Une revue par mois, **deux affaires** : une gagnée, une perdue. Une seule, c'est un témoignage.
Deux, c'est une comparaison. Le livrable est **un document rédigé**, jamais un tour de table :
sans document, rien n'entre dans le corpus, et la même leçon se rejoue le trimestre suivant.

### 3b. La séparation des rôles

Le commercial qui a mené l'affaire raconte les faits. Une autre personne rédige le document.
Celui qui a vécu l'affaire défend sa lecture, il ne la codifie pas seul : le biais de
justification est maximal sur ses propres deals.

### 3c. Ce que le document contient

Lire `references/TEMPLATE.md`, partie B. Les cinq rubriques sont : les faits datés, la décision
qui a fait basculer l'affaire, la règle maison qui s'appliquait, ce qu'elle a produit, et la
règle à créer, corriger ou retirer. La dernière ligne est la seule qui alimente le corpus.

## Étape 4 : Le portefeuille de skills versionnées

### 4a. Construire le corpus

Une skill par moment de vérité retenu à l'étape 1b, donc **cinq à huit**, jamais une par
détenteur et jamais une par affaire. Chaque skill porte :

```
Nom          : en kebab-case, à l'impératif ou au nom d'action
Moment       : le moment de vérité qu'elle couvre
Version      : semver
Propriétaire : la personne responsable de sa révision
Sources      : les règles maison et les revues d'affaires qui l'ont produite
État         : active, en essai, dépréciée, retirée
```

Une skill n'est jamais publiée sans propriétaire nommé. Une skill sans propriétaire est un
document mort au bout de deux trimestres, quelle que soit sa qualité initiale.

### 4b. Le registre

Tenir le registre au même endroit que les skills, pas dans un tableur séparé. Il contient, pour
chaque skill : la version, la date de dernière révision, le propriétaire, la source de la
dernière modification, et la date de dernière utilisation constatée. Une skill ni utilisée ni
révisée depuis deux trimestres passe en revue, sans exception.

### 4c. La compatibilité avec le reste de l'outillage

Si l'organisation utilise déjà des agents, vérifier que chaque skill produite respecte les
conventions de son corpus existant : nom de dossier, fichiers obligatoires, format de
frontmatter, langue, absence de dépendance à un éditeur donné. Une skill qui ne respecte pas les
conventions du corpus ne sera pas chargée, donc n'existera pas.

## Étape 5 : Le dispositif de transmission

### 5a. Le détachement

Un commercial senior confirmé, à mi-temps, pendant un trimestre, sur l'enablement. À mi-temps
signifie un mi-temps réel, pas une mission ajoutée à un quota plein. Un senior à quota plein
qui « s'occupe aussi des skills » ne produira rien, et vous l'aurez appris au bout du trimestre.

Le livrable du détachement est double : le corpus de l'étape 4, et **trois nouveaux vendeurs
capables de le faire vivre sans lui**. Le second compte davantage que le premier.

### 5b. La rotation

Le savoir remonte de la troupe vers l'état-major et redescend en sens inverse. Formaliser les
deux sens :
- **Remontée** : chaque commercial propose une règle corrigée après une affaire marquante, une
  fois par trimestre. La proposition passe par la revue de l'étape 3.
- **Descente** : chaque règle retenue est présentée en revue d'équipe dans le mois qui suit, par
  la personne qui l'a proposée, pas par le manager.

Sans le second sens, le corpus devient un document de direction que personne n'applique.

### 5c. Le test du départ

Le contrôle de bon fonctionnement est brutal et simple : **si le senior détaché partait demain,
combien de ses règles resteraient appliquées ?** La réponse se mesure en semaines, pas en
intentions. Tant que la réponse tient en une personne, la codification n'est pas terminée.

## Étape 6 : Le cycle de révision

### 6a. Le rythme

Le corpus suit le rythme de la revue de l'étape 3 : un mois, une revue, jusqu'à trois skills
touchées. Ce qui n'a pas bougé depuis six mois est signalé au propriétaire, ce qui n'a pas bougé
depuis douze mois passe en dépréciation.

### 6b. La règle de retrait

Une skill se retire quand son moment de vérité disparaît, quand son taux d'usage s'effondre, ou
quand elle produit un résultat contraire à celui attendu sur deux revues consécutives. Le
retrait est annoncé et daté, jamais silencieux : une skill qui disparaît sans trace fait douter
de tout le corpus.

### 6c. La version

Toute modification de fond incrémente la version mineure, toute correction de forme la version
de correctif, toute refonte du moment de vérité la version majeure. La version figure dans le
registre et dans la skill elle-même, jamais dans un seul des deux.

## Contrôle qualité

Avant de livrer :
- [ ] Trois à sept détenteurs identifiés, par croisement de deux sources et non par déclaration unique
- [ ] Cinq à huit moments de vérité retenus, ni plus ni moins
- [ ] Chaque règle porte un signal observable et un contre-exemple, ou est signalée comme ressenti
- [ ] Chaque écart entre ce qui est déclaré en entretien et ce que montrent les livrables est restitué
- [ ] La revue d'affaire produit un document rédigé par une personne qui n'a pas mené l'affaire
- [ ] Chaque skill du portefeuille porte un propriétaire nommé et une version
- [ ] Le registre est tenu au même endroit que les skills
- [ ] Le détachement senior est un mi-temps réel, avec une date de fin
- [ ] Le test du départ est posé et sa réponse chiffrée en semaines
- [ ] Aucune donnée externe citée sans source et sans date de moins de douze mois
- [ ] Aucune déduction présentée comme un fait établi

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Aucun détenteur ne se dégage du croisement des deux sources | Le dire, puis commencer par la revue d'affaire de l'étape 3 : le savoir apparaîtra en creux, dans ce que l'équipe n'arrive pas à refaire deux fois |
| Aucun accès aux affaires gagnées et perdues | Poursuivre sur les entretiens seuls, et inscrire au livrable que l'étape 2b n'a pas été exécutée |
| Plus de huit moments de vérité proposés | Fusionner les moments adjacents et faire arbitrer la direction : un portefeuille trop large n'est jamais tenu à jour |
| Une règle contredit une autre règle du corpus | Ne jamais trancher seul : porter les deux en revue d'affaire, la contradiction est en général le signe d'un segment ou d'un moment non distingué |
| Le senior détaché est indisponible | Ne pas improviser un remplaçant à quota plein. Reporter le détachement, l'audit peut être livré sans lui, pas la transmission |
| Aucune revue mensuelle n'est tenue après trois mois | Le signaler chiffres en main : sans la revue, le corpus cesse d'être alimenté et les skills se périment en un semestre |
| Les skills produites ne respectent pas les conventions du corpus existant | Les corriger avant publication, une skill non chargeable n'existe pas |

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil, outils connectés, dossier de destination |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt à copier |
| `references/TEMPLATE.md` | Avant de rédiger : les trois livrables (fiche d'entretien, revue d'affaire, registre) |
| `examples/exemple-codification.md` | Exemple de sortie complète sur un cas fictif |
