---
name: audit-visibilite-ia-geo
version: 1.0.0
description: >
  Auditer la visibilité d'une marque B2B dans les réponses des assistants conversationnels et des
  moteurs génératifs, avant que l'acheteur n'établisse sa shortlist. Le livrable est un rapport de
  reconnaissance en trois chantiers chiffrés : inventaire du balisage JSON-LD réellement servi,
  confronté aux types Organization, Product ou Service et FAQPage de Schema.org ; liste des réponses
  courtes et autonomes manquantes aux questions des acheteurs, avec l'état du fichier llms.txt et la
  règle du chiffre daté et attribué ; protocole de mesure mensuel de dix à quinze questions sur trois
  assistants, notées en présence, rang et formulation. Déclencheurs : "audit de visibilité IA",
  "sommes-nous cités par les IA", "AEO", "GEO", "optimisation pour les moteurs génératifs",
  "balisage Schema.org", "llms.txt", "shortlist IA", "contenu citable". Inspiré de l'article
  « Visibilité IA : soyez vu avant d'être shortlisté, comme à Midway » : la reconnaissance décide du
  résultat avant le premier engagement, il faut se rendre lisible avant d'être cherché. Compatible
  avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills, copier
  INSTRUCTIONS.md comme prompt système.
---

# Visibilité IA : audit de reconnaissance avant shortlist

Établit où une marque B2B apparaît dans les réponses des assistants conversationnels, ce que la
machine peut lire d'elle, et ce qui manque pour qu'elle soit citée plutôt qu'écartée.

> Principe doctrinal (article « Visibilité IA : soyez vu avant d'être shortlisté, comme à Midway ») :
> en juin 1942, à Midway, l'amiral Nimitz aligne trois porte-avions contre quatre. La Station Hypo
> déchiffre partiellement le code JN-25, un faux message sur une panne d'eau douce confirme la cible
> « AF », et les hydravions repèrent la flotte adverse avant qu'elle ne voie la flotte américaine.
> Décrypter avant de frapper : la reconnaissance décide du résultat avant le premier engagement, et
> la shortlist se constitue dans la réponse, sans vendeur dans la pièce.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare la marque et son domaine, les assistants retenus,
le format et la langue de sortie, et les connecteurs éventuels.

Si `TOOLS.md` est absent ou vide : mode dégradé gracieux, audit mené sur les seules URL publiques et
les questions fournies, sortie Markdown, français, profil générique. Aucun connecteur n'est requis :
l'inventaire du balisage se fait sur des pages publiques, la mesure par saisie manuelle des questions.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Audit balisage seul** | Une ou plusieurs URL, sans questions | Exécuter l'Étape 2 seule |
| **Audit contenu seul** | Des questions et des pages, sans mesure | Exécuter l'Étape 3 seule |
| **Audit complet** | Domaine, questions et assistants déclarés | Exécuter les Étapes 1 à 5 |
| **Aucune donnée** | Rien de fourni | Reconstituer le périmètre par entretien (Étape 1b) |

### 0c. Confirmer les entrées minimales

Demander (seulement si absent) :

1. **La marque**, son domaine, et les **URL** qui portent son identité (société, offres, tarification,
   références, conformité, questions fréquentes)
2. **Les trois assistants** retenus, les mêmes à chaque passage
3. **Les dix à quinze questions** que posent réellement les acheteurs, et leur origine interne
   (commerciaux, support, CRM)
4. **Le fichier llms.txt** s'il existe, avec sa date de dernière mise à jour
5. **Le mois de référence** et, si l'audit est récurrent, le relevé du mois précédent

Si l'utilisateur dit « lance-toi » avec un domaine seul : procéder en mode Audit balisage seul.

---

## Étape 1 : Cadrer le périmètre et figer les questions

### 1a. Périmètre et questions

Retenir les pages qui portent les entités de la marque, et fixer ce périmètre avant la mesure.
Constituer la liste des dix à quinze questions que les acheteurs posent réellement, celles qui
précèdent la consultation (article, manœuvre 3).

Chaque question provient d'une source interne nommée : appel commercial, ticket de support, requête
du CRM. Une question inventée est écartée ; une question reformulée est signalée comme reformulée.
Périmètre et formulations restent identiques d'un mois sur l'autre : un périmètre qui bouge rend
l'écart mensuel ininterprétable.

### 1b. Reconstruction et tableau de suivi

Si l'organisation n'a pas de questions écrites, reconstituer la liste en interrogeant commerciaux et
support, et consigner pour chacune son origine. La liste est validée avant la première mesure, puis
figée.

Ouvrir un tableau de suivi : une ligne par question, une colonne par assistant, et les colonnes de
notation de l'Étape 4. Le même tableau sert chaque mois, les relevés s'empilent par date.

---

## Étape 2 : Chantier 1, inventaire du balisage

### 2a. La règle de la page servie

L'inventaire porte sur la **page réellement servie** : le document que reçoit un agent qui parcourt
l'URL publique, et non le modèle, le gabarit ou le code source de l'éditeur. Un balisage déclaré dans
le gabarit qui n'apparaît pas dans le document servi est compté **absent**. C'est la condition de
validité du chantier : il s'agit de voir ce que la machine voit, pas ce que l'organisation croit
publier.

### 2b. Méthode de vérification

Pour chaque URL du périmètre :

1. Récupérer la page à son adresse publique, telle qu'elle est servie.
2. Isoler les blocs de données structurées de type `application/ld+json`.
3. Relever les types déclarés et les confronter à Schema.org.
4. Consigner chaque écart et chaque erreur bloquante.

Le contrôle se répète à chaque évolution du site : un balisage conforme un mois peut se dégrader au
passage suivant d'une refonte.

### 2c. Les types attendus

| Type | Ce qu'il déclare | Attendu |
|------|------------------|---------|
| **Organization** | Identité : raison sociale, secteur, implantations, dirigeants, certifications | Obligatoire |
| **Product ou Service** | Offre : périmètre, catégorie, tarification | Obligatoire, l'un des deux selon l'offre |
| **FAQPage** | Questions fréquentes et réponses courtes | Obligatoire dès que des questions fréquentes existent |
| **Review** | Avis et notes | Optionnel, recommandé si des avis publics existent |

### 2d. Grille et lecture

Remplir une ligne par page : type détecté, conformité, champs obligatoires manquants, erreurs
bloquantes, méthode de vérification, statut. Les statuts possibles sont : conforme, partiel, absent,
non vérifiable sur la page servie.

L'écart le plus coûteux est le balisage **partiel** : présent, donc jugé fait, mais incomplet sur les
champs qui décident de la citation. Un balisage absent laisse la machine reconstituer seule ce que la
marque est ; un balisage périmé diffuse une description fausse plus vite qu'auparavant, sans le
lecteur humain qui aurait haussé un sourcil (article, manœuvre 1).

---

## Étape 3 : Chantier 2, contenu citable

### 3a. La liste des réponses manquantes

Pour chaque question figée, vérifier qu'une page y répond explicitement :

- En **moins de soixante mots lisibles isolément** (seuil de l'article, manœuvre 2)
- **Hors de son contexte** : le passage se tient seul, sans dépendre du paragraphe précédent
- Avec **au moins un chiffre attribué à une source datée**

Une question sans page correspondante, ou dont la réponse tient en un paragraphe narratif sans prise
extractible, est comptée manquante.

### 3b. La règle du chiffre daté et attribué

Tout chiffre publié porte le nom de sa source et sa date. Un ordre de grandeur sans attribution ne
rend pas la page citable : la formulation qui convainc un lecteur ne suffit pas à une machine qui
vérifie. Une source de plus de douze mois est signalée comme non confirmée à la date de l'audit.

### 3c. llms.txt et découvrabilité

Relever l'état du fichier : présent ou absent, date de dernière mise à jour, nombre d'URL listées
rapporté au nombre d'URL du périmètre, écarts entre les pages d'identité et les entrées listées. Un
llms.txt absent est consigné absent, jamais créé sans validation explicite.

Les pages du périmètre doivent aussi être accessibles aux robots des éditeurs de modèles et présentes
dans les corpus tiers consultés : un agent ne cite que ce qu'il a pu lire (article, manœuvre 2).

### 3d. Grille du contenu citable

Remplir une ligne par question : réponse courte existante, autonomie hors contexte, présence d'un
chiffre daté et attribué, page porteuse, action à mener.

---

## Étape 4 : Chantier 3, mesure

### 4a. Le protocole figé

Poser les dix à quinze questions, avec les **mêmes formulations**, sur les **trois assistants**
retenus, dans le même ordre. Ce qui change d'un passage à l'autre, c'est la réponse observée, pas la
question posée.

### 4b. La notation en trois colonnes

Pour chaque couple question et assistant, noter trois choses (article, manœuvre 3) :

| Colonne | Valeurs | Ce qu'elle dit |
|---------|---------|----------------|
| **Présence** | citée, non citée | La marque figure-t-elle dans la réponse |
| **Rang** | 1er, 2e, 3e, au-delà, absent | À quelle place, sachant que la réponse en accorde deux ou trois |
| **Formulation** | termes exacts relevés | Dans quels mots la marque ou la catégorie est décrite |

Ajouter les sources citées par l'assistant, et signaler toute question où un concurrent est cité à la
place de la marque. La formulation relevée décrit ce que la machine a lu : elle n'est pas un jugement
porté sur la marque et ne se corrige pas dans le relevé.

### 4c. La synthèse et le rythme

Produire, par assistant : le taux de présence (questions citées rapportées au total), le rang médian,
et l'écart avec le mois précédent. Ajouter la liste des questions où un concurrent apparaît à votre
place, et les sources que les assistants ont citées pour vous décrire.

Rythme **mensuel**, à intervalle fixe : un rythme régulier bat une campagne ponctuelle, en
reconnaissance comme en marketing (article, manœuvre 3). Chaque passage produit une page de compte
rendu et une action déclenchée par question perdue.

---

## Étape 5 : Sortie et décision

### 5a. Rédiger le rapport

Suivre la structure de `references/TEMPLATE.md` : en-tête, inventaire du balisage, contenu citable,
mesure, synthèse, chantier, repères externes. Format par défaut Markdown, nommé
`audit-visibilite-ia-[Marque]-[DateJour].md`.

### 5b. Un seul chantier et une réinstrumentation

Le chantier de mesure se poursuit chaque mois : c'est le radar, il ne s'arrête pas. Le chantier à
ouvrir pour le cycle suivant est retenu parmi les deux autres, le balisage et le contenu citable, en
visant l'écart le plus large rapporté à l'effort. Un seul chantier ouvert à la fois.

Fixer la date de réinstrumentation à **un mois** de l'audit, sur le même périmètre d'URL et les mêmes
questions, sans élargir : la comparaison avec le relevé précédent est la seule preuve de progrès.

---

## Contrôle qualité

Avant de livrer :

- [ ] L'inventaire du balisage porte sur la page servie, pas sur le code source de l'éditeur
- [ ] Chaque page du périmètre a un statut explicite : conforme, partiel, absent, non vérifiable
- [ ] Les questions de mesure sont au nombre de dix à quinze et leurs formulations sont figées
- [ ] Les trois assistants retenus sont les mêmes que le mois précédent
- [ ] Chaque question est notée en présence, rang et formulation, aucun couple laissé vide
- [ ] Chaque donnée chiffrée porte sa source et sa date ; toute source de plus de douze mois est signalée comme non confirmée
- [ ] Le seuil de soixante mots par réponse courte est appliqué, ou son écart est justifié
- [ ] Aucune déduction n'est présentée comme un fait : un balisage absent de la page servie n'est pas supposé présent, une citation non observée n'est pas supposée acquise
- [ ] Le rapport se termine par un seul chantier à ouvrir et une date de réinstrumentation
- [ ] Aucune donnée présente dans le livrable n'a été inventée pour combler un trou

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Page inaccessible ou robots bloqués | Marquer « non vérifiable sur la page servie », ne pas supposer conforme |
| Balisage dans le code de l'éditeur mais absent de la page servie | Le compter absent : la page servie fait foi |
| llms.txt absent | Le consigner absent, ne pas le créer sans validation explicite |
| Moins de dix questions disponibles | Mesurer sur ce qui existe et signaler la fragilité du relevé |
| Un assistant indisponible ou un résultat non reproductible | Marquer le passage non concluant et le refaire le lendemain, à formulations identiques |
| Aucune source interne pour les questions | Reconstituer par entretien avec commerciaux et support, signaler l'origine |
| Marque citée sous une formulation erronée | La consigner telle quelle et renvoyer au contenu citable ou au balisage concerné |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : marque, assistants, format de sortie, connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt système autonome à copier |
| `references/TEMPLATE.md` | Avant de rédiger : structure annotée du rapport de reconnaissance |
| `examples/exemple-audit-visibilite.md` | Pour voir une sortie complète sur un cas fictif |
