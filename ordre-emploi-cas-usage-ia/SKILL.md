---
name: ordre-emploi-cas-usage-ia
version: 1.0.0
description: >
  Rédiger l'ordre d'emploi des cas d'usage IA d'une fonction commerciale : une page par processus,
  écrite avant toute démonstration d'éditeur, fixant la tâche confiée, le rôle qui la porte, la
  sortie attendue, le contrôle et le propriétaire du résultat. Produit aussi le tableau de mesure
  à cinq colonnes tenu par la fonction RevOps et le mandat de l'état-major commercial permanent.
  Déclencheurs : "ordre d'emploi IA", "cadrer un cas d'usage IA", "avant la démo de l'éditeur",
  "quelle IA pour quel rôle", "réunion RevOps IA", "faut-il résilier la licence". Inspiré de
  l'article « Sedan 1870 : le déploiement de l'IA commerciale se gagne à l'état-major » : la
  supériorité qui décide est celle de l'état-major, pas celle de l'équipement. Compatible avec
  tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills, copier INSTRUCTIONS.md
  comme prompt système.
---

# Ordre d'Emploi des cas d'usage IA

Fixe ce qu'un outil d'IA commerciale doit produire, pour quel rôle et sous quel contrôle, avant même que l'éditeur ne fasse sa démonstration. Le livrable tient dans trois objets : une page d'ordre d'emploi par processus, un tableau de mesure par rôle à cinq colonnes, et le mandat d'un état-major commercial permanent.

Un ordre d'emploi se place avant l'achat. Il répond à une question unique : quel rôle nommé consomme la sortie de cet outil, et quelle décision en découle ? Sans cette réponse écrite, la licence finance une démonstration réussie, pas un résultat.

> **Principe doctrinal** (article « Sedan 1870 : le déploiement de l'IA commerciale se gagne à
> l'état-major ») : le 1er septembre 1870, l'armée française aligne un fusil Chassepot supérieur
> au Dreyse pour la portée et une mitrailleuse Reffye à 100 coups par minute, puis perd la
> campagne en moins de sept semaines. La mitrailleuse, engagée à 1 800 mètres comme pièce
> d'artillerie, fut repérée et détruite par l'artillerie prussienne ; le bon outil placé dans le
> mauvais rôle ne produit rien. La supériorité qui décide est celle de l'état-major, pas celle de
> l'équipement.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare :
- le profil de la fonction commerciale (taille, effectif, processus déjà outillés)
- les connecteurs accessibles en lecture (CRM, conversation intelligence, tableaux de bord)
- la langue, le format de sortie et la profondeur d'analyse
- le dossier de sortie (`output_dir`)

Si `TOOLS.md` est absent ou vide, continuer en mode dégradé : entretien structuré seul, sortie
Markdown, français, profil générique.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Processus nommé** | Un processus précis à cadrer (« préparer un rendez-vous », « qualifier un lead ») | Rédiger l'ordre d'emploi complet (Étape 2) |
| **Portefeuille** | Plusieurs processus ou un catalogue d'outils à cadrer | Cadrer chaque processus, un ordre d'emploi par page |
| **Démonstration programmée** | Un éditeur doit démontrer son outil prochainement | Mode urgence : écrire l'ordre d'emploi avant la démo, pour fixer ce qu'elle doit prouver |
| **Licence déjà signée** | L'outil est acheté, l'objectif est de valider son usage | Rétro-rédiger l'ordre d'emploi, puis alimenter la mesure (Étape 3) |

### 0c. Confirmer les entrées minimales

Demander (seulement si absent) :
1. **Le processus** concerné (obligatoire), nommé par son déclencheur et sa fréquence
2. **Le rôle** qui porte aujourd'hui la tâche (une fonction, pas un service)
3. **L'outil ou la catégorie d'outil** envisagé (optionnel)
4. **Le propriétaire** devant qui le résultat se défend en revue (recommandé)

Si l'utilisateur dit « lance-toi » avec un processus, procéder en mode « processus nommé ».

---

## Étape 1 : Cadrer le processus

### 1a. Nommer le processus

Un processus se nomme par son déclencheur et sa fréquence, pas par un thème : « préparer une
note de contexte avant un rendez-vous », « qualifier un lead entrant », « rédiger le compte rendu
d'un appel ». Un thème (« améliorer la prospection ») n'est pas un processus et ne supporte pas
d'ordre d'emploi.

### 1b. Décrire le trajet actuel

- Qui exécute la tâche aujourd'hui, avec quel outil, en combien de temps
- Ce que la tâche produit et qui consomme cette sortie en aval
- Quelle décision aval en dépend ; si aucune décision n'est identifiable, le processus est candidat à la coupe, pas à l'outillage

### 1c. Poser la question de la valeur avant d'outiller

Rappeler le point de départ chiffré : 90 % des entreprises interrogées utilisent l'IA et 6 % en
tirent des résultats que leurs dirigeants qualifient de transformateurs (enquête HubSpot relayée
par Forbes, article de John Koetsier, 16 septembre 2026). L'écart ne se comble pas par le choix
de l'outil. Gartner mesure que 22 % des organisations seulement ont réussi à passer l'IA à
l'échelle sur plusieurs business units, et que 11 % des responsables ignorent la dépense d'IA de
leur fonction en 2025 (Gartner, communiqué du 1er septembre 2026, enquête de janvier à avril 2026
auprès de 1 303 responsables). L'ordre d'emploi traite précisément cet angle mort.

---

## Étape 2 : Rédiger l'ordre d'emploi (première manœuvre)

Un ordre d'emploi tient sur une page par processus et se rédige avant la démonstration de
l'éditeur, parce que c'est lui qui fixe ce que la démonstration doit prouver. Il contient cinq
champs, dans cet ordre.

### 2a. Les cinq champs

| Champ | Règle de rédaction | Contre-exemple |
|---|---|---|
| **Tâche confiée** | Un verbe et un objet, jamais une catégorie | « Préparer une note de contexte avant un rendez-vous », et non « assister la force de vente » |
| **Rôle qui la porte** | Une fonction, jamais un service | « Le commercial qui tient le rendez-vous », et non « le commerce » |
| **Sortie attendue** | Un format et un délai | « Une note d'une page, disponible la veille du rendez-vous » |
| **Contrôle qui la valide** | Qui vérifie, sur quoi, à quel moment | « Le compte rendu de rendez-vous, déposé dans les 24 heures » |
| **Propriétaire du résultat** | La fonction devant qui la sortie se défend en revue | « Le directeur commercial, pour ce processus » |

### 2b. Où vit la page

La fiche vit dans le CRM, sur la fiche du processus, pas dans une présentation de comité : c'est
ce qui supprime la seconde saisie et le document mort. La fonction RevOps en tient le registre,
le révise une fois par trimestre, et à chaque changement d'outil ou de rôle.

### 2c. La règle de coupe appliquée en amont

Un ordre d'emploi sans rôle consommateur nommé n'autorise pas la mise en service de l'outil.
C'est la règle de coupe appliquée un cran plus tôt, avant l'achat et non au renouvellement.

---

## Étape 3 : Tenir la mesure par rôle (deuxième manœuvre)

La mesure se prend par rôle, dans un tableau tenu par la fonction RevOps, celle qui porte les
processus et les données de la fonction commerciale, entre les opérations et la direction.

### 3a. Les cinq colonnes

| Colonne | Ce qu'elle contient |
|---|---|
| **Le rôle** | La fonction qui consomme la sortie |
| **La tâche** | Reprise mot pour mot de l'ordre d'emploi |
| **L'output** | La sortie produite, et par qui elle est consommée |
| **L'usage** | Le nombre d'utilisations par semaine |
| **La décision du trimestre** | Reconduite, réaffectée ou coupée |

### 3b. Les trois sources, à ne pas confondre

- La **matière conversationnelle** dit ce que l'outil sert réellement à faire
- Les **tableaux de bord du CRM** donnent l'usage, donc la fréquence
- La **revue de pipeline** donne le résultat

Confondre la fréquence avec le résultat est l'erreur la plus fréquente d'un déploiement d'IA
commerciale : un usage élevé sans effet sur le pipeline décrit une adoption, pas un gain.

### 3c. La règle de coupe, écrite d'avance

Trois verdicts, prononcés au trimestre suivant et jamais à l'échéance du contrat :

| Verdict | Condition |
|---|---|
| **Réaffecter** | La sortie est utile à un autre rôle ; réécrire l'ordre d'emploi en conséquence |
| **Reconduire** | La sortie est consommée par un rôle nommé et une décision en découle |
| **Résilier** | Aucun rôle nommé ne consomme la sortie ; la licence était une subvention versée à un éditeur |

Le tableau se met à jour chaque semaine et se lit en comité chaque mois. Gartner chiffre à 81 %
les initiatives à retour positif là où ce retour est suivi, et relève que ceux qui suivent ce
retour de loin en ignorent le taux sur 29 % de leurs initiatives (Gartner, communiqué du
1er septembre 2026).

---

## Étape 4 : Mandater l'état-major permanent (troisième manœuvre)

L'état-major prussien tenait un travail continu, pas une réunion annuelle : cartes, horaires,
doctrine, retours de manœuvre. Un état-major commercial tient dans deux personnes.

### 4a. Le mandat

- **Deux personnes** : un responsable RevOps et un responsable sales enablement, c'est-à-dire la fonction qui rend la doctrine exécutable par la formation et les contenus
- **Une heure par semaine** : le cycle est hebdomadaire et tient en une heure
- **Trois points à l'ordre du jour** :

| Point | Contenu |
|---|---|
| 1. Ce que la mesure a montré | Les chiffres de la semaine ou du mois, sans commentaire |
| 2. La décision unique | Une licence réaffectée, un ordre d'emploi réécrit, un processus arrêté |
| 3. Ce qui change pour le terrain | La mise à jour de l'ordre d'emploi et le module de formation qui l'accompagne |

### 4b. Les trois livrables du cycle

L'ordre d'emploi mis à jour, la note de décision qui l'accompagne, le contenu de formation qui la
rend exécutable. L'IA s'insère dans ces trois objets à la place que l'ordre d'emploi lui donne,
jamais à la place d'un rôle.

### 4c. Le test de fin de trimestre

Deux nombres suffisent : combien de processus ont un ordre d'emploi à jour, et combien de
licences ont un rôle nommé qui consomme leur sortie. Les organisations qui répondent à ces deux
questions sans préparer de dossier sont celles qui ont installé l'état-major, et non celles qui
l'ont annoncé.

---

## Étape 5 : Sortie

### 5a. Format par défaut : Markdown

Rédiger le livrable selon `references/TEMPLATE.md` :
`ordre-emploi-[processus]-[DateJour].md`, sauvegardé dans le dossier `output_dir` déclaré dans
`TOOLS.md` (défaut : dossier courant). Un ordre d'emploi par processus, une page chacun.

### 5b. Ce que le livrable contient

1. **Le registre des ordres d'emploi** : une page par processus, cinq champs remplis
2. **Le tableau de mesure** : cinq colonnes, une ligne par couple de rôle et de tâche
3. **Le mandat de l'état-major** : les deux personnes, la cadence, les trois points
4. **Les valeurs de référence** : les chiffres sourcés et datés, avec leur périmètre

### 5c. Contrôle qualité avant livraison

- [ ] Chaque ordre d'emploi a un rôle consommateur nommé (une fonction, pas un service)
- [ ] La tâche est écrite avec un verbe et un objet, jamais une catégorie
- [ ] La sortie attendue porte un format et un délai
- [ ] Le contrôle nomme qui vérifie, sur quoi, à quel moment
- [ ] Le propriétaire du résultat est une fonction identifiée
- [ ] Chaque donnée chiffrée porte sa source et sa date
- [ ] Aucune déduction n'est présentée comme un fait : les estimations sont signalées comme telles
- [ ] La règle de coupe est écrite avant le renouvellement du contrat

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Aucun processus identifiable | Redemander le déclencheur et la fréquence ; un thème n'est pas un processus |
| Aucun rôle consommateur | Signaler que l'outil ne peut pas être mis en service ; proposer de réaffecter ou de couper |
| Sortie non consommée en aval | Marquer la licence « candidate à la résiliation » et le dire |
| Source de plus de douze mois | Signaler « information non confirmée (plus de 12 mois) » ou l'écarter |
| Démonstration d'éditeur déjà passée | Rétro-rédiger l'ordre d'emploi, puis alimenter la mesure ; ne pas choisir sur des impressions |
| Données de mesure indisponibles | Démarrer le tableau avec la seule colonne de décision renseignée, et l'assumer comme incomplet |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier**, profil de la fonction commerciale et connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills, prompt à copier |
| `references/TEMPLATE.md` | Avant de rédiger, structure de l'ordre d'emploi et du tableau |

---

*Skill « Ordre d'Emploi » de la collection strategiecommerciale.eu. Inspirée de l'article
« Sedan 1870 : le déploiement de l'IA commerciale se gagne à l'état-major » (22 septembre 2026).*
