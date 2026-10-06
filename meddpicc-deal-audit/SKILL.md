---
name: meddpicc-deal-audit
version: 2.1.0
description: >
  Utiliser ce skill pour auditer, extraire ou alimenter la qualification MEDDPICC d'une
  opportunité commerciale B2B. Cinq modes : audit complet d'un deal, extraction des champs
  MEDDPICC depuis un transcript de réunion, brief pré-réunion sur les champs à clarifier,
  consolidation multi-sources, et préparation des mises à jour CRM.
  Déclencheurs : toute mention de "MEDDPICC", "MEDDIC", "MEDDPICC", "audit de deal",
  "qualification d'opportunité", "revue de pipeline", "audit commercial", un transcript ou
  compte rendu de réunion à exploiter, une réunion à préparer, ou une demande de mise à jour
  CRM sur une opportunité. Déclencher aussi proactivement quand l'utilisateur mentionne un
  risque sur un deal, un comité commercial, une revue de forecast, ou pose une question sur la
  solidité d'une opportunité, même sans mentionner MEDDPICC.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity…) : sans système de skills,
  copier le contenu de INSTRUCTIONS.md comme prompt système.
---

# MEDDPICC Deal Audit Skill

Audite, extrait et alimente la qualification MEDDPICC d'une opportunité commerciale B2B,
enrichie par des sources externes datées (web) et les outils déclarés dans `TOOLS.md`.

Le livrable est un document d'analyse par dimension avec scoring RAG, angles morts identifiés
et une lecture doctrinale ancrée dans la pensée stratégique classique.

> **Règle de preuve, valable dans tous les modes : un champ sans citation n'existe pas.**
> Un agent qui lit un transcript est un agent qui a envie d'inventer un Champion. Toute
> dimension renseignée doit être adossée à un verbatim, une note ou une source datée. À défaut,
> la dimension est déclarée non renseignée, jamais déduite.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Ce fichier déclare :
- les outils disponibles pour enrichir l'analyse (web_search par défaut, MCP optionnels)
- le format de sortie souhaité (Markdown, JSON ou document)
- les préférences de langue, de profondeur d'analyse et le dossier de sortie

Si `TOOLS.md` est absent ou vide, continuer avec le mode dégradé gracieux :
`web_search` uniquement, sortie Markdown, analyse standard, sortie dans le dossier courant.

### 0b. Détecter le mode

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Audit** (défaut) | Nom de compte, notes de découverte, revue de pipeline | Recherche externe complète puis audit des 8 dimensions |
| **Extraction** | Transcript, enregistrement, compte rendu de réunion, résumé d'appel | Extraire les 8 champs avec verbatim, sans recherche externe initiale |
| **Pré-réunion** | « réunion demain », « préparer le comité », « qu'est-ce qui me manque » | Brief court : champs à clarifier et questions à poser |
| **Consolidation** | Plusieurs sources hétérogènes (notes + transcripts + CRM) | Fusionner, hiérarchiser les preuves, signaler les contradictions |
| **Alimentation CRM** | « mets à jour le CRM », « remonte ces champs », « push » | Proposer les mises à jour, exiger la validation humaine avant écriture |

Un mode n'exclut pas les autres : un audit peut s'appuyer sur l'extraction d'un transcript
préalablement fourni. Enchaîner les modes si le contexte le demande, en annonçant l'enchaînement.

### 0c. Confirmer les inputs minimaux

Demander (seulement si non déjà fourni) :
1. **Nom du compte prospect** (obligatoire)
2. **Secteur / pays HQ** (recommandé pour affiner la recherche)
3. **Notes de découverte ou transcript** (optionnel, tout format accepté)
4. **Stade du deal** (exploration, validation, négociation, closing)
5. **Date de la prochaine réunion** (utile uniquement en mode Pré-réunion)

Si l'utilisateur dit « lance-toi » avec seulement un nom de compte, procéder en mode Audit.

---

## Étape 1 — Protocole de recherche externe

### 1a. Règle de fraîcheur absolue

> **Toute source externe doit être datée. Toute source de plus de 12 mois est rejetée ou
> signalée explicitement comme « information non confirmée (>12 mois) ».**

Sources prioritaires par ordre de fiabilité :
1. Rapport annuel / investor relations (exercice le plus récent)
2. Communiqués de presse et earnings calls (12 derniers mois)
3. Interviews de dirigeants (CEO, CFO, CRO) dans la presse spécialisée
4. Offres d'emploi actives (signaux d'investissement, de priorités, de douleurs)
5. Couverture analystes / presse sectorielle
6. Profils LinkedIn des contacts identifiés (Economic Buyer, Champion)

### 1b. Recherches minimales à effectuer

Lancer **au minimum 5 recherches distinctes** avant de rédiger, couvrant :
- [ ] Stratégie et priorités du compte (rapport annuel ou interview dirigeant)
- [ ] Actualité récente (M&A, lancements, restructurations, recrutements)
- [ ] Contexte sectoriel (pressions concurrentielles, tendances de marché)
- [ ] Profil de l'Economic Buyer pressenti (s'il est connu)
- [ ] Signaux de douleur (avis clients, offres d'emploi révélatrices, témoignages publics)

En mode **Pré-réunion**, la recherche peut être réduite à l'actualité du compte et au profil des
participants annoncés. En mode **Extraction**, la recherche externe est différée : extraire
d'abord, corréler ensuite.

### 1c. Utilisation des outils MCP déclarés dans TOOLS.md

Pour chaque outil MCP déclaré, consulter sa section dans `TOOLS.md` pour connaître le type de
données récupérables, les requêtes recommandées et les limites à respecter.

Exemples typiques :
- **CRM** → fiche compte, historique d'activité, opportunités liées, champs MEDDPICC existants
- **Conversation Intelligence** → transcriptions, résumés, mentions de douleurs, objections
- **Email / Agenda** → derniers échanges, engagements pris, participants aux réunions
- **Compte rendu de réunion** (webconférence, transcription mobile, notes structurées) → source
  d'extraction directe en mode Extraction

### 1d. Synthèse de recherche (usage interne — ne pas afficher)

Compiler avant de rédiger : taille et structure du compte, 3 à 5 priorités stratégiques
sourcées, signaux de douleur détectés, personnes clés et rôles publics, contexte concurrentiel.

---

## Étape 2 — Rédaction de l'audit

Lire `references/TEMPLATE.md` — c'est le template de sortie annoté.
Rédiger l'audit en suivant **exactement** cette structure.

Règles de rédaction par champ :

**Signal** : reproduire fidèlement ce que le commercial a fourni (ou « Non renseigné » si absent).
Ne pas interpréter, ne pas corriger. En mode Extraction, le signal est le **verbatim**, accompagné
de son locuteur et de son horodatage quand ils sont disponibles.

**Corroboration** : ce que les sources externes confirment, infirment ou enrichissent.
Toujours citer la source avec sa date entre parenthèses : *(Reuters, mars 2025)*.
Si aucune corroboration trouvée : « Aucune source externe trouvée. »

**Criticité** : poids de la dimension dans la décision d'achat, indépendant de sa confiance.
- **Critique** — Economic Buyer, Identify Pain, Champion
- **Haute** — Metrics, Decision Criteria, Decision Process, Competition
- **Moyenne** — Paper Process

**Confiance RAG** : évaluation sur trois niveaux avec justification d'une ligne.
- 🟢 **VERT** — Information confirmée, sourcée, cohérente entre commercial et sources externes
- 🟡 **AMBER** — Information partielle, non confirmée, ou contradictoire
- 🔴 **ROUGE** — Information absente, invérifiable, ou en contradiction avec les sources

**Angle mort** : ce qui reste inconnu après recherche, et l'implication tactique concrète.
Formuler en une phrase d'action : « Sans confirmation de X, risque de Y — action recommandée : Z. »

### Règle de scoring global

| Condition | Score |
|-----------|-------|
| 2 dimensions **critiques** en ROUGE ou plus | 🔴 À risque |
| 3 dimensions en ROUGE ou plus, toutes criticités confondues | 🔴 À risque |
| Aucun ROUGE sur les 3 dimensions critiques, les autres ≥ AMBER | 🟢 Solide |
| Tous les autres cas | 🟡 À consolider |

---

## Étape 3 — Mode Extraction : du transcript aux champs

À utiliser dès qu'un transcript, un enregistrement ou un compte rendu est fourni.

**Procédure :**

1. **Parcourir le document source en entier** avant d'extraire quoi que ce soit. Un transcript
   se contredit souvent entre le début et la fin, et c'est précisément l'information utile.
2. **Extraire dimension par dimension**, en citant pour chacune le verbatim exact, le locuteur
   et l'horodatage si disponible. Format : « *[nom ou rôle, mm:ss]* : “citation” ».
3. **Ne jamais combler un vide par déduction.** Une dimension absente du transcript reste non
   renseignée avec une confiance ROUGE, même si le contexte la rend probable.
4. **Repérer les contradictions internes** entre interlocuteurs, et les signaler en priorité
   (par exemple un Champion qui décrit un processus de décision que l'Economic Buyer contredit).
5. **Identer les questions restées sans réponse** dans la conversation : elles alimentent
   directement le mode Pré-réunion.

**Sortie du mode Extraction** : un tableau des 8 dimensions avec, pour chacune, le verbatim,
le locuteur et la confiance, suivi de la liste des dimensions sans preuve et des contradictions
détectées. Pas de recherche externe dans cette sortie : elle porte sur ce qui a été dit.

---

## Étape 4 — Mode Pré-réunion : le brief des champs à clarifier

À utiliser avant une réunion, un comité ou un point de qualification.

**Sortie volontairement courte, sur une page :**

1. **Position actuelle** — le score global et la liste des dimensions ROUGE et AMBER.
2. **Les trois questions à poser**, classées par criticité décroissante : une question par
   dimension la plus critique non renseignée, formulée telle qu'elle sera posée à l'oral, et
   rattachée à la dimension qu'elle sert.
3. **Les contradictions à faire trancher** si le mode Extraction a révélé des divergences.
4. **Le risque principal** de la réunion : ce que le deal perd si la réunion se passe mal.
5. **Le signal à écouter** : l'élément qui, s'il est prononcé, fait basculer la dimension de
   ROUGE à VERT.

Ce brief ne remplace pas l'audit complet : il en est la version de terrain, à utiliser entre
deux réunions. Pour un brief d'appel plus large (contexte du compte, angles d'attaque,
instinct de préparation), utiliser par ailleurs le skill `coup-doeil-pre-call-briefing`.
Pour entraîner les commerciaux à tenir ces questions en situation, utiliser
`pas-de-tir-sparring-client`, en lui passant les dimensions non renseignées comme scénario.

---

## Étape 5 — Mode Alimentation CRM

À utiliser quand l'utilisateur veut remonter les champs qualifiés dans son CRM.

**Le skill ne doit jamais écrire sans validation explicite.** La sortie du mode est une
**proposition de mise à jour**, pas une écriture.

Produire un tableau :

| Champ CRM | Valeur proposée | Preuve | Confiance | Proposé à l'écriture |
|----------|-----------------|--------|-----------|----------------------|
| Champion | … | *[verbatim, locuteur]* | 🟢 | Oui |
| Economic Buyer | … | *[verbatim, locuteur]* | 🟡 | Avec avertissement |
| Paper Process | (inchangé) | aucune preuve | 🔴 | Non |

**Règles d'écriture :**
- Seuls les champs en **VERT avec verbatim** sont proposés en écriture directe.
- Les champs **AMBER** sont proposés avec un avertissement explicite sur ce qui manque.
- Les champs **ROUGE** ne sont jamais proposés : ils restent vides et alimentent la liste des
  questions à poser.
- Ne jamais écraser une valeur existante du CRM sans afficher l'ancienne et la nouvelle côte à
  côte. Un écrasement silencieux détruit une qualification antérieure.
- Si aucun outil d'écriture n'est déclaré dans `TOOLS.md`, produire le tableau au format
  d'import (CSV ou JSON) et indiquer la procédure de saisie manuelle.

---

## Étape 6 — Lecture doctrinale

Après l'analyse des 8 dimensions, rédiger une section **Lecture Doctrinale** (lire `references/DOCTRINE.md`).

Cette section traduit l'état du deal dans le vocabulaire stratégique classique :
- Identifier le type de terrain (Sun Tzu) correspondant à la position commerciale actuelle
- Signaler les risques de biais cognitifs (Syndrome de Valmy, Pusillanimité décisionnelle)
- Évaluer si le deal est sur ligne intérieure (compte existant) ou extérieure (conquête)
- Si des angles morts critiques existent, formuler l'approche indirecte recommandée (Liddell Hart)

La lecture doctrinale n'est pas décorative — elle doit produire **au moins une recommandation
d'action concrète** issue du raisonnement stratégique.

---

## Étape 7 — Sortie

### Format par défaut : Markdown

Produire un fichier `audit-meddpicc-[NomCompte]-[DateJour].md` complet,
structuré selon `references/TEMPLATE.md`, livrable en Markdown.
Sauvegarder dans le dossier `output_dir` déclaré dans `TOOLS.md` (défaut : dossier courant).

En mode Pré-réunion, le nom de fichier est `brief-meddpicc-[NomCompte]-[DateJour].md`.
En mode Extraction, il est `extraction-meddpicc-[NomCompte]-[DateJour].md`.

### Format JSON (si spécifié dans TOOLS.md)

Si `output_format: json` est déclaré dans `TOOLS.md`, produire un fichier
`audit-meddpicc-[NomCompte]-[DateJour].json` avec la structure suivante :

```json
{
  "compte": "...", "secteur": "...", "stade": "...", "date": "...", "mode": "audit",
  "dimensions": {
    "metrics":     { "signal": "...", "corroboration": "...", "confiance": "VERT|AMBER|ROUGE", "angle_mort": "...", "criticite": "Haute", "preuve": "[verbatim, locuteur, mm:ss] | null" },
    "economic_buyer": { ... },
    "decision_criteria": { ... },
    "decision_process": { ... },
    "paper_process": { ... },
    "identify_pain": { ... },
    "champion": { ... },
    "competition": { ... }
  },
  "score_global": "SOLIDE|A_CONSOLIDER|A_RISQUE",
  "lecture_doctrinale": { "terrain": "...", "biais": "...", "ligne": "...", "recommandations": ["..."] },
  "questions_a_poser": ["..."],
  "proposition_crm": [{ "champ": "...", "valeur": "...", "preuve": "...", "confiance": "VERT", "ecriture": "directe|avertissement|refusee" }],
  "sources": ["source | date", "..."]
}
```

Ce format permet de brancher l'audit sur des workflows automatisés (n8n, Make, scripts).

### Format document (si spécifié dans TOOLS.md)

Si `output_format: document` est déclaré dans `TOOLS.md`, lire `references/docx/FORMAT.md`
avant de générer un fichier .docx formaté selon la charte du site (fond blanc, encre `#0C1B2E`,
accent cuivre `#C98A4B`), avec en-tête « Audit MEDDPICC — [NomCompte] — [Date] » et scoring RAG
en couleur. Sauvegarder dans le dossier `output_dir` déclaré dans `TOOLS.md`.

---

## Étape 8 — Contrôle qualité

Avant de livrer, vérifier :
- [ ] Chaque dimension des 8 a un Signal, une Corroboration, un RAG et un Angle mort
- [ ] Aucune source de plus de 12 mois sans mention explicite
- [ ] Chaque source citée inclut sa date
- [ ] Les RAG ROUGE sont accompagnés d'une action recommandée
- [ ] La Lecture Doctrinale produit au moins une recommandation actionnable
- [ ] Le Scoring Global final est cohérent avec les RAG et les criticités déclarées
- [ ] **Mode Extraction** : chaque dimension renseignée porte un verbatim identifié, et aucune
      n'a été déduite du contexte
- [ ] **Mode Pré-réunion** : chaque question posée est rattachée à une dimension et à sa criticité
- [ ] **Mode Alimentation CRM** : aucune écriture proposée sans preuve, et les écrasements de
      valeurs existantes sont affichés côte à côte

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Compte introuvable en ligne | Signaler, demander à l'utilisateur tout document ou contexte disponible |
| Notes de découverte trop lacunaires (<3 dimensions renseignées) | Avertir et proposer un guide de questions de découverte par dimension manquante |
| Sources contradictoires | Utiliser la source la plus récente et primaire ; signaler la contradiction |
| Transcript inexploitable (audio non transcrit, qualité insuffisante) | Le signaler et proposer les modes Audit ou Pré-réunion sur la base des notes disponibles |
| Transcript désignant deux interlocuteurs différents pour un même rôle | Signaler en priorité : c'est une contradiction de qualification, pas un détail de forme |
| Economic Buyer non identifié | Mettre ROUGE immédiatement, proposer 3 questions de découverte ciblées |
| Champion non identifié | Mettre ROUGE immédiatement ; c'est un facteur de risque critique |
| Aucun outil d'écriture CRM déclaré | Produire le tableau de proposition en CSV ou JSON pour saisie manuelle |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** — avant toute action |
| `INSTRUCTIONS.md` | Agents sans système de skills — c'est le prompt système à copier |
| `references/TEMPLATE.md` | Avant de rédiger l'audit — structure de sortie complète |
| `references/DOCTRINE.md` | Avant de rédiger la Lecture Doctrinale |
| `references/docx/FORMAT.md` | Uniquement si `output_format: document` est déclaré |

---

## Ancrage éditorial

Ce skill prolonge l'article MEDDIC du blog strategiecommerciale.eu (méthode de qualification et
erreurs d'engagement commercial). Il reste volontairement agnostique : aucune dépendance à un
fournisseur d'agent, à un CRM ou à une plateforme d'intelligence conversationnelle particuliers.
Les connecteurs se déclarent dans `TOOLS.md`.
