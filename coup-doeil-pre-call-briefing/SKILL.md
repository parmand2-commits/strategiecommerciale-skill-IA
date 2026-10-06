---
name: coup-doeil-pre-call-briefing
version: 1.1.0
description: >
  Produire un briefing de pré-appel (pre-call brief) complet en 10 minutes pour un commercial
  B2B : synthèse du compte, contexte sectoriel, 3 angles d'attaque, questions à poser et risques
  à surveiller. Le livrable ouvre sur une question unique portant sur l'événement déclencheur de
  l'acheteur, interdit la démonstration au premier rendez-vous, trace le champ CRM « problème
  client » et se clôt sur une charte d'engagement.
  Déclencheurs : "briefing avant appel", "préparer mon appel", "pre-call brief", "que sais-je
  sur ce compte", "angles d'attaque pour ce prospect", "question de Foch", "événement
  déclencheur de l'acheteur", "charte d'engagement avant appel".
  Inspiré de l'article « Instinct commercial vs IA : le coup d'œil de Napoléon »
  (https://strategiecommerciale.eu/ia-force-de-vente-coup-doeil-napoleon/) : la machine nourrit
  l'instinct, elle ne le remplace pas. Complété par « La question de Foch : la vente consultative
  B2B avant le pitch » (https://strategiecommerciale.eu/vente-consultative-b2b-question-de-foch/)
  et « Gouvernance de l'IA commerciale : la mise en garde de Machiavel »
  (https://strategiecommerciale.eu/gouvernance-ia-commerciale-machiavel/).
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Coup d'Œil : Pre-call Briefing

Produit un briefing de pré-appel structuré pour une opportunité ou un compte prospect B2B.
Le livrable donne au commercial **l'état-major de Berthier** (données, contexte, angles) pour
que son **coup d'œil de Napoléon** (instinct, lecture du terrain) s'exprime au mieux.

> Principe doctrinal : Napoléon lisait le terrain d'un coup d'œil, mais n'a gagné aucune
> bataille sans l'état-major de Berthier. L'IA ne remplace pas l'instinct commercial : elle le
> nourrit. Foch ajoute que le diagnostic commande l'offre, jamais l'inverse, et Machiavel
> rappelle qu'un agent qui engage l'entreprise doit être gouverné : ses actes opposables
> restent réservés à une validation humaine.

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

## Étape 3 : Rédaction du briefing

Lire `references/TEMPLATE.md`, le gabarit annoté. Rédiger le briefing en suivant
**exactement** cette structure. Règles par section :

**Règle d'ouverture** : la question de Foch (Étape 2) en tête, la démonstration interdite.
**Situation** : 3 à 5 lignes factuelles sourcées (qui, quoi, où en est le compte).
**Enjeux stratégiques** : 2 à 3 priorités du compte, sourcées et datées.
**Angles d'attaque** : **exactement 3 angles** différenciés, formulés en bénéfice prospect
(jamais en caractéristique produit). Chaque angle : 2 à 3 phrases + 1 question d'ouverture.
**Questions à poser** : 5 questions maximum, classées par priorité, ouvertes.
**Signaux à écouter** : ce qui, entendu pendant l'appel, confirme ou infirme chaque angle.
**Risques et objections probables** : 3 maximum, avec l'esquive recommandée.
**Décision demandée** : la prochaine étape à formuler explicitement en fin d'appel.

### 3a. La trace CRM dans le livrable

Reporter la section « Trace CRM » avec le texte du champ « problème client » dans les mots de
l'acheteur, prêt à saisir. Mentionner la provenance (champ existant, saisie manuelle).

### 3b. Clore sur la charte d'engagement

Terminer chaque briefing par le **rappel de la charte d'engagement** de l'équipe : une page,
signée par la direction commerciale et le juridique, qui fixe ce que l'agent a le droit
d'affirmer, de promettre et de chiffrer.

- Rappeler que les **actes opposables** (message client, chiffrage, appel d'offres) restent
  **réservés à une validation humaine**.
- Rappeler la règle de fraîcheur des sources et l'absence de chiffre client non confirmé.
- La charte est un rappel, pas une signature : ne jamais présenter un acte opposable comme
  validé par la seule production du briefing.

---

## Contrôle qualité

Avant de livrer :
- [ ] Une question d'ouverture unique porte sur l'événement déclencheur de l'acheteur
- [ ] La démonstration au premier rendez-vous est explicitement écartée
- [ ] Le champ CRM « problème client » est rédigé dans les mots de l'acheteur
- [ ] Chaque information externe est datée (source + date)
- [ ] Exactement 3 angles d'attaque, formulés en bénéfice prospect
- [ ] 5 questions maximum, ouvertes, hiérarchisées
- [ ] Une décision demandée explicite en fin de briefing
- [ ] La charte d'engagement et la validation humaine des actes opposables sont rappelées
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
