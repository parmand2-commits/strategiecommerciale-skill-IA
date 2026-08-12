---
name: coup-doeil-pre-call-briefing
version: 1.0.0
description: >
  Produire un briefing de pré-appel (pre-call brief) complet en 10 minutes pour un commercial B2B :
  synthèse du compte, contexte sectoriel, 3 angles d'attaque, questions à poser et risques à surveiller.
  Déclencheurs : "briefing avant appel", "préparer mon appel", "pre-call brief", "que sais-je sur ce compte",
  "angles d'attaque pour ce prospect", ou avant toute démo/appel client programmé. Inspiré de l'article
  « Le coup d'œil de Napoléon » : la machine nourrit l'instinct, elle ne le remplace pas.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity…) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Coup d'Œil — Pre-call Briefing

Produit un briefing de pré-appel structuré pour une opportunité ou un compte prospect B2B.
Le livrable donne au commercial **l'état-major de Berthier** (données, contexte, angles)
pour que son **coup d'œil de Napoléon** (instinct, lecture du terrain) s'exprime au mieux.

> Principe doctrinal (article « Le coup d'œil de Napoléon ») : Napoléon lisait le terrain d'un
> coup d'œil, mais n'a gagné aucune bataille sans l'état-major de Berthier. L'IA ne remplace
> pas l'instinct commercial — elle le nourrit.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Il déclare :
- le profil de l'organisation utilisatrice (taille, secteur, typologie de clients)
- les outils connectés disponibles (CRM, conversation intelligence, email — optionnels)
- les préférences de langue, format et profondeur

Si `TOOLS.md` est absent ou vide : mode dégradé — `web_search` uniquement, sortie Markdown,
profil organisation « générique ».

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Nom de compte seul** | Juste le nom du prospect | Recherche web complète (Étape 1) |
| **Nom + notes** | Nom + notes de découverte | Prioriser les notes, web pour combler |
| **Nom + données CRM** | Fiche compte, contacts, opportunités (via TOOLS.md) | Prioriser les données connectées, web pour les angles morts |

### 0c. Confirmer les inputs minimaux

Demander (seulement si absent) :
1. **Nom du compte** (obligatoire)
2. **Objet de l'appel** (découverte, démo, négociation, QBR…) — recommandé
3. **Participants connus** (qui sera dans la salle) — recommandé
4. Toute note ou contexte disponible (optionnel)

Si l'utilisateur dit « lance-toi » avec un nom seul : procéder en Mode 1.

---

## Étape 1 — Renseignement (5 à 8 minutes max)

### 1a. Règle de fraîcheur

> Toute source externe datée. Source > 12 mois : rejetée ou signalée
> « information non confirmée (>12 mois) ».

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
- **CRM** → fiche compte, contacts, opportunités ouvertes, historique d'activité
- **Conversation Intelligence** → derniers appels, objections entendues, next steps
- **Email/Agenda** → derniers échanges, engagements, participants aux réunions

### 1d. Synthèse (usage interne — ne pas afficher)

Compiler mentalement : taille/revenus du compte, 3 priorités stratégiques sourcées,
signaux de douleur, personnes clés, contexte concurrentiel.

---

## Étape 2 — Rédaction du briefing

Lire `references/TEMPLATE.md` — c'est le template annoté. Rédiger le briefing en suivant
**exactement** cette structure. Règles par section :

**Situation** : 3-5 lignes factuelles sourcées (qui, quoi, où en est le compte).
**Enjeux stratégiques** : 2-3 priorités du compte, sourcées et datées.
**Angles d'attaque** : **exactement 3 angles** différenciés, formulés en bénéfice prospect
(pas en caractéristique produit). Chaque angle = 2-3 phrases + 1 question d'ouverture.
**Questions à poser** : 5 questions maximum, classées par priorité, ouvertes.
**Signaux à écouter** : ce qui, entendu pendant l'appel, confirme ou infirme chaque angle.
**Risques & objections probables** : 3 maximum, avec l'esquive recommandée.
**Décision demandée** : la demande de prochaine étape à formuler en fin d'appel.

---

## Étape 3 — Contrôle qualité

Avant de livrer :
- [ ] Chaque information externe est datée (source + date)
- [ ] Exactement 3 angles d'attaque, formulés en bénéfice prospect
- [ ] 5 questions maximum, ouvertes, hiérarchisées
- [ ] Une décision demandée explicite en fin de briefing
- [ ] Temps de lecture du briefing ≤ 3 minutes (le commercial le lira entre deux appels)
- [ ] Aucune information non confirmée présentée comme un fait

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Compte introuvable en ligne | Le dire, demander tout document/note disponible |
| Participants inconnus | Le signaler, préparer les angles sur le compte seul |
| Sources contradictoires | Prendre la plus récente et primaire, signaler la contradiction |
| Moins de 2 angles identifiables | Avertir : « briefing en mode dégradé », proposer un angle sur le secteur |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** — profil organisation + outils connectés |
| `INSTRUCTIONS.md` | Agents sans système de skills — prompt à copier |
| `references/TEMPLATE.md` | Avant de rédiger — structure du briefing |
