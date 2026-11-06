---
name: coup-doeil-pre-call-briefing
version: 1.2.0
description: >
  Produire un briefing de pré-appel (pre-call brief) complet en 10 minutes pour un commercial
  B2B : synthèse du compte, contexte sectoriel, 3 angles d'attaque, questions à poser, brouillard
  à lever et friction d'exécution à parer. Le livrable ouvre sur une question unique portant sur
  l'événement déclencheur de l'acheteur, interdit la démonstration au premier rendez-vous, sépare
  ce que le briefing ignore de ce qui l'empêchera d'agir sur ce qu'il sait, trace le champ CRM
  « problème client », se clôt sur une charte d'engagement et se referme, après l'appel, sur un
  compte rendu de trois lignes.
  Déclencheurs : "briefing avant appel", "préparer mon appel", "pre-call brief", "que sais-je
  sur ce compte", "angles d'attaque pour ce prospect", "question de Foch", "événement
  déclencheur de l'acheteur", "brouillard ou friction", "retour de call", "charte d'engagement
  avant appel".
  Inspiré de l'article « Instinct commercial vs IA : le coup d'œil de Napoléon »
  (https://strategiecommerciale.eu/ia-force-de-vente-coup-doeil-napoleon/) : la machine nourrit
  l'instinct, elle ne le remplace pas. Complété par « La question de Foch : la vente consultative
  B2B avant le pitch » (https://strategiecommerciale.eu/vente-consultative-b2b-question-de-foch/),
  « Gouvernance de l'IA commerciale : la mise en garde de Machiavel »
  (https://strategiecommerciale.eu/gouvernance-ia-commerciale-machiavel/) et « La Friction de
  Clausewitz : mesurer le ROI de votre IA commerciale »
  (https://strategiecommerciale.eu/roi-ia-commerciale-friction-clausewitz/), qui fournit la
  distinction entre le brouillard et la friction et les quatre sources de friction.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Coup d'Œil : Pre-call Briefing

Produit un briefing de pré-appel structuré pour une opportunité ou un compte prospect B2B.
Le livrable donne au commercial **l'état-major de Berthier** (données, contexte, angles) pour
que son **coup d'œil de Napoléon** (instinct, lecture du terrain) s'exprime au mieux.

> Principe doctrinal : Napoléon lisait le terrain d'un coup d'œil, mais n'a gagné aucune
> bataille sans l'état-major de Berthier. L'IA ne remplace pas l'instinct commercial : elle le
> nourrit. Foch ajoute que le diagnostic commande l'offre, jamais l'inverse. Clausewitz
> distingue le brouillard, qui est le manque d'informations, de la friction, qui empêche
> d'agir sur ce que l'on sait : un briefing utile nomme les deux, il ne les confond pas.
> Machiavel rappelle qu'un agent qui engage l'entreprise doit être gouverné : ses actes
> opposables restent réservés à une validation humaine.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare :
- le profil de l'organisation utilisatrice (taille, secteur, typologie de clients)
- les outils connectés disponibles (CRM, conversation intelligence, email, optionnels)
- les préférences de langue, format et profondeur

Si `TOOLS.md` est absent ou vide : mode dégradé, `web_search` uniquement, sortie Markdown,
profil organisation « générique ».

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Nom de compte seul** | Juste le nom du prospect | Recherche web complète (Étape 1) |
| **Nom + notes** | Nom + notes de découverte | Prioriser les notes, web pour combler |
| **Nom + données CRM** | Fiche compte, contacts, opportunités | Prioriser le connecté, web pour le reste |

### 0c. Confirmer les inputs minimaux

Demander (seulement si absent) :
1. **Nom du compte** (obligatoire)
2. **Objet de l'appel** (découverte, démo, négociation, QBR…), recommandé
3. **Participants connus** (qui sera dans la salle), recommandé
4. Toute note ou contexte disponible (optionnel)

Si l'utilisateur dit « lance-toi » avec un nom seul : procéder en Mode 1.

---

## Étape 1 : Renseignement (5 à 8 minutes max)

### 1a. Règle de fraîcheur

> Toute source externe datée. Source de plus de 12 mois : rejetée ou signalée
> « information non confirmée (plus de 12 mois) ».

### 1b. Recherches minimales (selon le profil défini dans TOOLS.md)

Lancer **au minimum 4 recherches distinctes** :
- [ ] Actualité récente du compte (12 derniers mois : M&A, lancements, réorganisation)
- [ ] Contexte sectoriel (pressions, tendances, réglementation)
- [ ] Profil des participants pressentis (LinkedIn, prises de parole)
- [ ] Signaux de douleur (avis clients, offres d'emploi, témoignages)

### 1c. Données connectées (si déclarées dans TOOLS.md)

Pour chaque outil connecté (CRM, conversation intelligence, email), consulter sa section
dans `TOOLS.md` : quel type de données récupérer, quelles requêtes, quelles limites.
Exemples :
- **CRM** : fiche compte, contacts, opportunités ouvertes, historique d'activité, et le champ
  « problème client » déjà renseigné s'il existe
- **Conversation Intelligence** : derniers appels, objections entendues, prochaines étapes
- **Email/Agenda** : derniers échanges, engagements, participants aux réunions

### 1d. Synthèse (usage interne, ne pas afficher)

Compiler mentalement : taille et revenus du compte, 3 priorités stratégiques sourcées,
signaux de douleur, personnes clés, contexte concurrentiel.

---

## Étape 2 : La question de Foch (le diagnostic avant l'offre)

> « De quoi s'agit-il ? » Foch ouvrait toute étude de situation par cette question, reprise de
> Verdy du Vernois. Le diagnostic commande l'offre, jamais l'inverse.

### 2a. La question d'ouverture unique

Le briefing porte **une seule question d'ouverture**, et elle porte sur l'**événement
déclencheur** de l'acheteur : le changement interne qui a fait naître le projet. Un achat B2B
naît d'un changement chez l'acheteur, pas d'une démonstration produit.

- Formuler la question avant toute présentation de l'offre.
- Question type : « Qu'est-ce qui a changé chez vous pour que ce sujet arrive sur la table
  maintenant ? »
- Ne jamais remplacer cette question par une question de qualification fermée.

### 2b. L'interdiction de la démonstration au premier rendez-vous

La **démonstration est interdite au premier rendez-vous**. Le premier rendez-vous sert à
établir le diagnostic ; le support produit ne s'ouvre qu'une fois l'événement déclencheur
nommé par l'acheteur. La qualification (MEDDIC) sert à **éprouver le diagnostic**, jamais à
cocher des cases. Si l'acheteur demande « une démo rapide », le briefing prévoit la réponse :
revenir à l'événement déclencheur.

### 2c. Le champ CRM « problème client »

Préparer le **champ CRM « problème client »** du compte ou de l'opportunité, rédigé **dans les
mots de l'acheteur**. Interdits : la reformulation commerciale, le vocabulaire produit, la
traduction automatique en bénéfice. Le champ est contrôlé à chaque revue de pipeline.

Si un CRM est connecté (déclaré dans `TOOLS.md`), proposer la mise à jour du champ. Sinon,
livrer le texte prêt à coller, clairement identifié comme une saisie manuelle.

---

## Étape 3 : Trier le brouillard et la friction

> Clausewitz sépare deux empêchements que l'on confond souvent. Le **brouillard** est le manque
> d'informations : on ignore ce que fait l'acheteur. La **friction** est ce qui empêche d'agir
> sur ce que l'on sait : un ordre mal transmis, une unité en retard, une batterie qui ne tire
> pas. Un briefing qui ne nomme que le brouillard prépare des questions ; celui qui nomme aussi
> la friction prépare l'exécution de l'appel.

### 3a. Le brouillard : trois inconnues, trois questions

Lister **3 inconnues maximum** sur la situation de l'acheteur. Pour chacune :
- ce que l'on ignore, formulé comme une question ouverte ;
- la question d'appel qui lèvera l'inconnue pendant l'entretien.

Une inconnue sans question pour la lever est du bruit : la retirer. Une inconnue ne se comble
jamais par une inférence présentée comme un fait.

### 3b. La friction : quatre sources, quatre parades

Clausewitz ramène la friction à quatre sources : le danger, l'effort, l'incertitude et le
hasard. Le briefing les décline en **risques d'exécution**, distincts des objections du client :
la friction ne vient pas de l'acheteur, elle vient de notre propre conduite de l'appel.

| Source | Risque d'exécution pendant l'appel | Parade inscrite au briefing |
|--------|-----------------------------------|-----------------------------|
| **Danger** | un chiffre faux, un nom mal orthographié, une promesse hors charte | vérifier la source des deux faits structurants, marquer les données non confirmées |
| **Effort** | le briefing n'est pas lu, le commercial reprend son pitch habituel | une page, trois minutes de lecture, question d'ouverture en tête |
| **Incertitude** | une donnée CRM incomplète ou périmée fausse la qualification | dater chaque donnée interne, signaler les champs vides |
| **Hasard** | l'événement que le plan n'a pas prévu : champion qui part, réorganisation, gel de budget | préparer la question « qui décide si X quitte l'entreprise ? » |

Ne retenir que les frictions réelles du compte, **3 maximum**. Une friction générique n'aide
personne à exécuter.

### 3c. Le coup d'œil ne se remplace pas

Clausewitz fait du coup d'œil un jugement que l'expérience forme, pas un produit du volume
d'information. Conséquence pour le livrable : le briefing propose des **hypothèses à éprouver**
(les angles, avec les signaux qui les confirment ou les infirment), jamais des conclusions.
Aucun angle n'est présenté comme un fait établi.

---

## Étape 4 : Rédaction du briefing

Lire `references/TEMPLATE.md`, le gabarit annoté. Rédiger le briefing en suivant
**exactement** cette structure. Règles par section :

**Règle d'ouverture** : la question de Foch (Étape 2) en tête, la démonstration interdite.
**Situation** : 3 à 5 lignes factuelles sourcées (qui, quoi, où en est le compte).
**Brouillard et friction** : 3 inconnues avec leur question, puis 3 frictions d'exécution avec
leur parade (Étape 3).
**Enjeux stratégiques** : 2 à 3 priorités du compte, sourcées et datées.
**Angles d'attaque** : **exactement 3 angles** différenciés, formulés en bénéfice prospect
(jamais en caractéristique produit). Chaque angle : 2 à 3 phrases + 1 question d'ouverture.
**Questions à poser** : 5 questions maximum, classées par priorité, ouvertes.
**Signaux à écouter** : ce qui, entendu pendant l'appel, confirme ou infirme chaque angle.
**Risques et objections probables** : 3 maximum, avec l'esquive recommandée.
**Décision demandée** : la prochaine étape à formuler explicitement en fin d'appel.

### 4a. La trace CRM dans le livrable

Reporter la section « Trace CRM » avec le texte du champ « problème client » dans les mots de
l'acheteur, prêt à saisir. Mentionner la provenance (champ existant, saisie manuelle).

### 4b. Clore sur la charte d'engagement

Terminer chaque briefing par le **rappel de la charte d'engagement** de l'équipe : une page,
signée par la direction commerciale et le juridique, qui fixe ce que l'agent a le droit
d'affirmer, de promettre et de chiffrer.

- Rappeler que les **actes opposables** (message client, chiffrage, appel d'offres) restent
  **réservés à une validation humaine**.
- Rappeler la règle de fraîcheur des sources et l'absence de chiffre client non confirmé.
- La charte est un rappel, pas une signature : ne jamais présenter un acte opposable comme
  validé par la seule production du briefing.

---

## Étape 5 : Après l'appel, le compte rendu de trois lignes

Clausewitz ne supprime pas la friction : il en fait un objet de rapport. Les états-majors
prussiens comparent le déroulé au plan et corrigent à l'exercice suivant. Le briefing se juge
donc après l'appel, sur trois lignes, avant de nourrir le suivant :

1. **Ce que le briefing annonçait** : l'angle retenu, l'événement déclencheur supposé.
2. **Ce qui s'est passé** : l'événement déclencheur réel, l'angle qui a porté, la friction
   rencontrée.
3. **Ce que l'on change** : une seule correction, reportée dans le prochain briefing.

Ce compte rendu est demandé au commercial à chaud, en trois lignes maximum. Un compte rendu de
trois paragraphes n'est jamais rempli.

### 5a. Les traces qui jugent la skill

Un briefing n'est pas jugé sur sa longueur mais sur ce qu'il laisse dans les outils :

- **Avant l'appel (signaux avancés)** : briefing produit en 10 minutes maximum, lu avant
  l'appel, champ CRM saisi, question d'ouverture posée.
- **Après l'appel (résultat)** : taux de qualification des appels briefés, taux de
  transformation des opportunités briefées.

Un briefing que le commercial ne lit pas est une friction, pas un livrable. Le constat se
corrige dans le briefing suivant, pas dans une note de bilan.

---

## Contrôle qualité

Avant de livrer :
- [ ] Une question d'ouverture unique porte sur l'événement déclencheur de l'acheteur
- [ ] La démonstration au premier rendez-vous est explicitement écartée
- [ ] Le brouillard est nommé : 3 inconnues maximum, chacune avec la question qui la lève
- [ ] Les frictions d'exécution sont distinguées des objections du client
- [ ] Aucun angle n'est présenté comme un fait établi
- [ ] Le champ CRM « problème client » est rédigé dans les mots de l'acheteur
- [ ] Chaque information externe est datée (source + date)
- [ ] Exactement 3 angles d'attaque, formulés en bénéfice prospect
- [ ] 5 questions maximum, ouvertes, hiérarchisées
- [ ] Une décision demandée explicite en fin de briefing
- [ ] La charte d'engagement et la validation humaine des actes opposables sont rappelées
- [ ] Le compte rendu de trois lignes est fourni après l'appel
- [ ] Temps de lecture du briefing ≤ 3 minutes (le commercial le lit entre deux appels)
- [ ] Aucune information non confirmée présentée comme un fait

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Compte introuvable en ligne | Le dire, demander tout document ou note disponible |
| Participants inconnus | Le signaler, préparer les angles sur le compte seul |
| Sources contradictoires | Prendre la plus récente et primaire, signaler la contradiction |
| Moins de 2 angles identifiables | Avertir « briefing en mode dégradé », proposer un angle secteur |
| Événement déclencheur non nommé | Ne pas ouvrir le support produit, revenir à la question de Foch |
| Aucune inconnue identifiable | Le signaler : soit le compte est surexposé en ligne, soit la recherche est incomplète. Prévoir une question de vérification |
| Aucune friction identifiable | Retenir les deux frictions par défaut : briefing non lu, donnée interne périmée |
| CRM non connecté | Livrer le texte du champ « problème client » prêt à coller, signaler la saisie manuelle |
| Charte d'engagement absente du dossier | Le signaler et utiliser la charte générique du gabarit |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil organisation + outils connectés |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt à copier |
| `references/TEMPLATE.md` | Avant de rédiger : structure du briefing |
| `examples/exemple-briefing-verdier.md` | Pour voir une sortie complète sur un cas fictif |
