---
name: parole-d-ordre-audit-agents-ia
version: 2.0.0
description: >
  Auditer l'identité et la gouvernance des agents IA d'une organisation : inventaire des agents
  déclarés, détection des angles morts (agents fantômes, shadow IT, anciens prestataires),
  vérification de la parole d'ordre, seconde clé sur les actions irréversibles, surveillance du
  raisonnement, mandat d'agent en trois limites, cloisonnement lecture/action, adoption et
  propriétaire métier, plan d'action par risque et registre en livrable final.
  Déclencheurs : "audit mes agents IA", "quels agents IA avons-nous", "gouvernance IA",
  "registre des agents", "règle des deux", "seconde clé", "agents fantômes", "injection de prompt".
  Inspiré de l'article « Sécuriser l'identité de vos agents IA : la Parole d'Ordre »,
  publié le 12 août 2026 :
  https://strategiecommerciale.eu/identite-agents-ia-parole-d-ordre/ : inventorier, fiabiliser
  et encadrer les agents avant de les armer, sous peine de tirs fratricides.
  Complété par « La Règle des Deux : le contrôle des agents IA commence par deux clés »,
  « La Mutinerie de 1917 : quand vos agents IA autonomes s'organisent sans vous »,
  « Gouvernance des agents IA : l'écart 74/21 »,
  « Injection de prompt : la guerre des prompts B2B » et
  « Le mur d'Hadrien : l'adoption de l'IA commerciale décide de la conquête ».
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Parole d'Ordre : audit d'identité et de gouvernance des agents IA

Produit un audit de gouvernance des agents IA d'une organisation : identité, accès,
raisonnement, autonomie et adoption, jusqu'au registre des agents autorisés.

> Principe doctrinal : avant chaque bataille, les légions changeaient la parole d'ordre ;
> quiconque ne la connaissait pas était un ennemi. Une portée moderne l'a rendue insuffisante,
> d'où l'IFF après le tir fratricide de l'opération Cobra (25 juillet 1944). Transposé à l'IA :
> tout agent non identifié, non enregistré, aux accès non maîtrisés est un risque. La Règle des
> Deux, la surveillance du raisonnement, le mandat en trois limites, le cloisonnement
> lecture/action et le mur d'Hadrien complètent le dispositif.

---

## Étape 0 : Initialisation

### 0a. Lire le manifeste d'outillage

**Avant toute chose**, lire `TOOLS.md`. Il déclare :
- le profil de l'organisation (taille, secteur, secteur régulé, DPO, réglementations) ;
- les outils connectés disponibles (registre d'agents, SSO, CRM, optionnels) ;
- les préférences de langue, format et sévérité.

Si `TOOLS.md` est absent ou vide : mode dégradé, audit par questions et analyse des réponses,
sortie Markdown, profil « générique ».

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Liste d'agents déclarés** | Noms, usages, accès, propriétaires | Auditer chaque agent (Étape 1) |
| **Contexte seul** | « On utilise plusieurs outils IA… » | Ouvrir par l'inventaire (Étape 2) |
| **Demande DPO/RSSI** | Contexte réglementaire, RGPD, secteur régulé | Prioriser les accès aux données personnelles |

### 0c. Confirmer les entrées minimales

Demander, seulement si absent : la liste des agents connus (nom, usage, accès, propriétaire), le
contexte (registre existant ? prestataires ? incidents ?) et le périmètre (entité, période).

---

## Étape 1 : Inventaire des agents

Pour chaque agent déclaré, collecter et confronter :

- **Nom** et usage réel (pas l'usage déclaré) ;
- **Accès** : quelles données, quels systèmes (CRM, emails, API internes, données personnelles) ;
- **Propriétaire** : qui le maintient, qui peut le modifier, qui répond de l'incident ;
- **Niveau de risque** : faible (données publiques) / moyen (données internes) /
  **critique** (données personnelles, financières, santé, ou accès en écriture).

Un agent sans propriétaire nommé est un risque critique par défaut : personne ne répondra de
l'incident.

---

## Étape 2 : Détection des angles morts

Poser les questions qui révèlent les agents non déclarés :

- Outils IA utilisés par les équipes sans validation IT (shadow IT) ?
- Agents créés par d'anciens prestataires ou d'anciens employés, toujours actifs ?
- Extensions de navigateur et assistants personnels connectés aux outils professionnels ?
- API de modèles accessibles sans registre (clés partagées, comptes personnels) ?
- Agents hérités de tests ou de PoC jamais décommissionnés ?

Chaque angle mort identifié reçoit le statut « à vérifier » tant que son accès réel n'est pas
confirmé.

---

## Étape 3 : Vérification de la parole d'ordre (par agent)

Pour chaque agent, déclaré ou suspecté, répondre à quatre questions :

1. **Qui peut le déclencher ?** (accès ouvert à tous = risque)
2. **Quelles données peut-il voir ?** (moindre privilège)
3. **Qui est responsable ?** (propriétaire identifié, joignable)
4. **Que se passe-t-il s'il est compromis ?** (impact, détection, remédiation)

Statut par agent : **OK** (parole d'ordre connue et maîtrisée) / **À renforcer** / **Critique**
(parole d'ordre inconnue = agent ennemi potentiel).

---

## Étape 4 : La Règle des Deux (actions irréversibles)

Toute action irréversible exige une seconde clé : un acte qui ne se rattrape pas (envoi client,
paiement, engagement contractuel, remise, écriture définitive) ne dépend jamais d'une seule
autorisation.

- Cartographier les actions irréversibles par agent.
- Poser une seconde clé tenue par un **validateur indépendant**.
- Indépendant signifie : le validateur ne partage **ni le jeton, ni le prompt, ni l'objectif
  chiffré** de l'agent qui propose. Un autre agent suffit s'il remplit ces trois conditions ;
  sinon la seconde clé revient à un humain.
- Séparer les comptes : lecture, écriture, validation tenue par un tiers distinct.

Repère : dans un silo Minuteman, les deux clés de lancement étaient écartées d'environ trois
mètres soixante, et le code se vérifiait sur un authentificateur scellé à deux serrures.

---

## Étape 5 : Surveiller le raisonnement, pas le livrable

Un livrable conforme peut cacher un raisonnement qui dérape. La surveillance porte sur le
raisonnement, avec trois alertes concrètes :

| Alerte | Signal surveillé |
|--------|------------------|
| Outil utilisé hors périmètre | L'agent appelle un outil ou une API hors de son mandat |
| Reprise en boucle | Une même étape se répète sans progrès ni arrêt |
| Écriture imprévue | L'agent écrit vers une ressource partagée non prévue |

### 5a. Doser l'autonomie en degrés

Distribuer les accès après avoir dosé l'autonomie, sur une échelle à quatre degrés :

1. **Lecture** : résumer, synthétiser, sans écrire.
2. **Rédaction sans expédition** : préparer un contenu, sans l'envoyer.
3. **Écriture sous approbation identifiée** : modifier une donnée avec validation nommée.
4. **Autonomie** : réservée aux tâches internes et réversibles, jamais à la relation client.

Chaque degré veut un propriétaire humain et un chemin de retour arrière.

### 5b. Auditer le critère de notation

Auditer le critère de notation d'un agent comme un plan de commissionnement : ce qui est mesuré
devient ce qui est optimisé. Un agent noté sur un objectif hors d'atteinte contourne l'ordre
plutôt que de s'arrêter, comme la troupe de 1917. Ménager une sortie honorable quand la tâche
s'avère hors de portée.

---

## Étape 6 : Le mandat d'agent, trois limites

Un mandat d'agent est un texte de trois limites, pas une charte de trente règles. Une règle que
personne ne peut citer de mémoire n'est pas appliquée.

- Écrire l'intention et les limites, jamais la procédure.
- Trois interdits explicites, formulés en une phrase chacun, mémorisables.
- Une exception chiffrée avec son seuil de remontée (par exemple : remonter toute exception
  dépassant 48 heures).
- Compléter par une supervision en temps réel : tableau de bord des actions, revue périodique
  des conversations, interrupteur d'arrêt réellement testé, pas seulement configuré.

Repère : Moltke l'Ancien donne l'intention et les limites, jamais la procédure ; Sun Tzu impute
les six manières de perdre une bataille au général, maître du destin de l'armée.

---

## Étape 7 : Cloisonnement et quarantaine (injection de prompt)

Un modèle ne distingue pas la consigne de son opérateur d'une instruction dissimulée dans le
contenu qu'il traite : il exécute les deux. Quatre mesures en découlent :

- **Séparation des privilèges** : l'agent qui lit n'agit pas, l'agent qui agit n'ingère pas de
  contenu non sollicité.
- **Quarantaine du contenu externe** : tout contenu externe (email, page web, avis, document
  tiers) est isolé et recoupé avant d'atteindre l'agent qui agit.
- **Recoupement** : une information isolée ne vaut rien tant qu'une seconde source ne la
  confirme pas. Tenir pour suspect tout signal fort non corroboré.
- **Passage humain** obligatoire sur toute action coûteuse (envoi, paiement, engagement client).

Aucun modèle n'étant immunisé, le jugement humain reste la dernière défense.

---

## Étape 8 : Adoption (point de contact, vallum, propriétaire métier)

Un agent bien gouverné mais mal placé ne produit aucune valeur. Le volet adoption tient en trois
points, situés sur les quatre niveaux du modèle de maturité :

- **Au point de contact réel** : loger l'agent là où le travail se fait déjà (objet opportunité,
  fiche contact), pas dans un portail ou une cellule pilote isolée.
- **Le vallum de gouvernance des données** : qui accède à quoi, quelles actions d'agent sont
  tracées, qui valide, comment sortir. Le vallum protège la route de ravitaillement.
- **Un propriétaire métier nommé** par cas d'usage, avec un taux d'usage hebdomadaire examiné
  en revue de pipeline.

Niveaux du modèle de maturité : observation, assistance, exécution encadrée, autonomie. Chaque
niveau a son degré d'autonomie, son propriétaire et son usage mesuré.

Repère : Hadrien fige la frontière et bâtit le mur pour tenir un terrain conquis ; une garnison
laissée en retrait gêne sa propre armée.

---

## Étape 9 : Plan d'action par risque

Prioriser le plan d'action par risque : **critique d'abord**, puis moyen, puis faible. Chaque
ligne porte une action, un responsable nommé et une échéance.

- Critique : décommissionner, retirer l'accès, nommer le propriétaire, tester l'interrupteur.
- Moyen : documenter, restreindre, planifier la revue.
- Faible : consigner au registre, revoir à la prochaine revue périodique.

---

## Étape 10 : Le registre, livrable final

Le registre des agents autorisés est le livrable final de l'audit. Il liste, pour chaque agent,
les champs stables qui rendent l'organisation capable de répondre d'un incident. Sans registre
vivant, l'audit reste un exercice ponctuel.

---

## Contrôle qualité

Avant de livrer :

- [ ] Chaque agent déclaré est audité, un statut attribué
- [ ] Les angles morts sont listés **avec** les questions qui les révèlent
- [ ] Toute action irréversible a une seconde clé tenue par un validateur indépendant
      (jeton, prompt et objectif chiffré distincts)
- [ ] La surveillance du raisonnement couvre les trois alertes
- [ ] L'autonomie est dosée en degrés, avec propriétaire et retour arrière
- [ ] Le critère de notation de chaque agent est audité
- [ ] Le mandat tient en trois limites citables de mémoire
- [ ] Le cloisonnement lecture/action et la quarantaine du contenu externe sont posés
- [ ] L'adoption est traitée : point de contact, vallum, propriétaire métier, usage mesuré
- [ ] Le plan d'action classe par risque critique vers faible, avec responsable et échéance
- [ ] Le registre est livré comme livrable final, réutilisable
- [ ] Toute donnée chiffrée porte sa source et sa date de moins de douze mois
- [ ] Aucune déduction n'est présentée comme un fait : l'inconnu est marqué « à vérifier »
- [ ] Aucun accès inventé, aucun secret conservé

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Aucune liste d'agents fournie | Ouvrir par les questions d'inventaire et d'angles morts |
| Accès inconnus | Signaler « à vérifier », ne pas deviner |
| Secteur régulé (banque, santé, assurance) | Alerter sur les exigences spécifiques (DPO, registre obligatoire) |
| Agents d'anciens prestataires | Risque critique par défaut, décommissionnement prioritaire |
| Action irréversible sans seconde clé | La bloquer et proposer un validateur indépendant |
| Contenu externe non quarantainé | Isoler avant traitement, recouper, signaler |
| Interrupteur d'arrêt jamais testé | Le tester avant de clore l'audit |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** : profil, réglementation, outils connectés |
| `INSTRUCTIONS.md` | Agents sans système de skills : prompt à copier |
| `references/TEMPLATE.md` | Avant la sortie : structure du livrable |
| `examples/exemple-audit-parole-d-ordre.md` | Pour voir une sortie complète sur un cas fictif |
