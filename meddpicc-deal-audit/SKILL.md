---
name: meddpicc-deal-audit
version: 2.0.0
description: >
  Utiliser ce skill pour produire un audit MEDDPICC complet d'une opportunité commerciale B2B.
  Déclencheurs : toute mention de "MEDDPICC", "MEDDIC", "audit de deal", "qualification d'opportunité",
  "revue de pipeline", "audit commercial", ou lorsque l'utilisateur fournit des notes de découverte,
  un nom de compte prospect, ou demande d'analyser l'état d'avancement d'un deal. Déclencher aussi
  proactivement quand l'utilisateur mentionne un risque sur un deal, un comité commercial, une revue
  de forecast, ou pose une question sur la solidité d'une opportunité — même sans mentionner MEDDPICC.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity…) : sans système de skills,
  copier le contenu de INSTRUCTIONS.md comme prompt système.
---

# MEDDPICC Deal Audit Skill

Produit un audit structuré d'une opportunité commerciale B2B selon le cadre MEDDPICC, enrichi
par des sources externes datées (web) et les outils déclarés dans `TOOLS.md`.
Le livrable est un document d'analyse par dimension avec scoring RAG, angles morts identifiés,
et une lecture doctrinale finale ancrée dans la pensée stratégique classique.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Ce fichier déclare :
- les outils disponibles pour enrichir l'analyse (web_search par défaut, MCP optionnels)
- le format de sortie souhaité (Markdown, JSON ou document)
- les préférences de langue, de profondeur d'analyse et le dossier de sortie

Si `TOOLS.md` est absent ou vide, continuer avec le mode dégradé gracieux :
`web_search` uniquement, sortie Markdown, analyse standard, sortie dans le dossier courant.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Nom de compte seul** | Juste le nom du prospect | Lancer la recherche web complète (Étape 1) |
| **Notes libres** | L'utilisateur colle des notes de découverte | Extraire les signaux par dimension, combler par web |
| **Notes structurées** | Notes organisées par dimension MEDDPICC | Valider, corroborer par web, signaler les lacunes |
| **Contexte riche** | Notes + URLs + fichiers | Prioriser le contenu fourni, web pour les angles morts |

### 0c. Confirmer les inputs minimaux

Demander (seulement si non déjà fourni) :
1. **Nom du compte prospect** (obligatoire)
2. **Secteur / pays HQ** (recommandé pour affiner la recherche)
3. **Notes de découverte** (optionnel — tout format accepté)
4. **Stade du deal** (exploration, validation, négociation, closing)

Si l'utilisateur dit "lance-toi" avec seulement un nom de compte, procéder en Mode 1.

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

### 1c. Utilisation des outils MCP déclarés dans TOOLS.md

Pour chaque outil MCP déclaré, consulter sa section dans `TOOLS.md` pour :
- le type de données récupérables
- les requêtes ou paramètres recommandés
- les limites à respecter

Exemples typiques :
- **CRM** → fiche compte, historique d'activité, opportunités liées
- **Conversation Intelligence** → appels récents, mentions de douleurs, objections
- **Email / Agenda** → derniers échanges, engagements pris, participants aux réunions

### 1d. Synthèse de recherche (usage interne — ne pas afficher)

Avant de rédiger le template, compiler mentalement :
- Taille / revenus / structure du compte
- 3–5 priorités stratégiques identifiées (sourcées)
- Signaux de douleur détectés
- Personnes clés identifiées et leurs rôles publics
- Éléments de contexte concurrentiel

---

## Étape 2 — Rédaction de l'audit

Lire `references/TEMPLATE.md` — c'est le template de sortie annoté.
Rédiger l'audit en suivant **exactement** cette structure.

Règles de rédaction par champ :

**Signal** : reproduire fidèlement ce que le commercial a fourni (ou "Non renseigné" si absent).
Ne pas interpréter, ne pas corriger.

**Corroboration** : ce que les sources externes confirment, infirment ou enrichissent.
Toujours citer la source avec sa date entre parenthèses : *(Reuters, mars 2025)*.
Si aucune corroboration trouvée : écrire "Aucune source externe trouvée."

**Confiance RAG** : évaluation sur trois niveaux avec justification d'une ligne.
- 🟢 **VERT** — Information confirmée, sourcée, cohérente entre commercial et sources externes
- 🟡 **AMBER** — Information partielle, non confirmée, ou contradictoire
- 🔴 **ROUGE** — Information absente, invérifiable, ou en contradiction avec les sources

**Angle mort** : ce qui reste inconnu après recherche, et l'implication tactique concrète.
Formuler en une phrase d'action : "Sans confirmation de X, risque de Y — action recommandée : Z."

---

## Étape 3 — Lecture doctrinale

Après l'analyse des 8 dimensions, rédiger une section **Lecture Doctrinale** (lire `references/DOCTRINE.md`).

Cette section traduit l'état du deal dans le vocabulaire stratégique classique :
- Identifier le type de terrain (Sun Tzu) correspondant à la position commerciale actuelle
- Signaler les risques de biais cognitifs (Syndrome de Valmy, Pusillanimité décisionnelle)
- Évaluer si le deal est sur ligne intérieure (compte existant) ou extérieure (conquête)
- Si des angles morts critiques existent, formuler l'approche indirecte recommandée (Liddell Hart)

La lecture doctrinale n'est pas décorative — elle doit produire **au moins une recommandation
d'action concrète** issue du raisonnement stratégique.

---

## Étape 4 — Sortie

### Format par défaut : Markdown

Produire un fichier `audit-meddpicc-[NomCompte]-[DateJour].md` complet,
structuré selon `references/TEMPLATE.md`, livrable en Markdown.
Sauvegarder dans le dossier `output_dir` déclaré dans `TOOLS.md` (défaut : dossier courant).

### Format JSON (si spécifié dans TOOLS.md)

Si `output_format: json` est déclaré dans `TOOLS.md`, produire un fichier
`audit-meddpicc-[NomCompte]-[DateJour].json` avec la structure suivante :

```json
{
  "compte": "...", "secteur": "...", "stade": "...", "date": "...",
  "dimensions": {
    "metrics":     { "signal": "...", "corroboration": "...", "confiance": "VERT|AMBER|ROUGE", "angle_mort": "...", "criticite": "..." },
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
  "sources": ["source | date", "..."]
}
```

Ce format permet de brancher l'audit sur des workflows automatisés (n8n, Make, scripts).

### Format document (si spécifié dans TOOLS.md)

Si `output_format: document` est déclaré dans `TOOLS.md`, lire `references/docx/SKILL.md`
avant de générer un fichier .docx formaté avec :
- En-tête : "Audit MEDDPICC — [NomCompte] — [Date]"
- Couleurs : fond `#0d0c0a`, accents `#b49840` (identité visuelle strategiecommerciale.eu)
- Scoring RAG en couleur (vert/amber/rouge)
- Sauvegarder dans le dossier `output_dir` déclaré dans `TOOLS.md`

---

## Étape 5 — Contrôle qualité

Avant de livrer, vérifier :
- [ ] Chaque dimension des 8 a un Signal, une Corroboration, un RAG et un Angle mort
- [ ] Aucune source de plus de 12 mois sans mention explicite
- [ ] Chaque source citée inclut sa date
- [ ] Les RAG ROUGE sont accompagnés d'une action recommandée
- [ ] La Lecture Doctrinale produit au moins une recommandation actionnable
- [ ] Le Scoring Global final (Étape 5 dans le template) est cohérent avec les RAG individuels

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Compte introuvable en ligne | Signaler, demander à l'utilisateur tout document ou contexte disponible |
| Notes de découverte trop lacunaires (<3 dimensions renseignées) | Avertir et proposer un guide de questions de découverte par dimension manquante |
| Sources contradictoires | Utiliser la source la plus récente et primaire ; signaler la contradiction |
| Economic Buyer non identifié | Mettre ROUGE immédiatement, proposer 3 questions de découverte ciblées |
| Champion non identifié | Mettre ROUGE immédiatement ; c'est un facteur de risque critique selon l'article MEDDIC du blog |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** — avant toute action |
| `INSTRUCTIONS.md` | Agents sans système de skills — c'est le prompt système à copier |
| `references/TEMPLATE.md` | Avant de rédiger l'audit — structure de sortie complète |
| `references/DOCTRINE.md` | Avant de rédiger la Lecture Doctrinale |
