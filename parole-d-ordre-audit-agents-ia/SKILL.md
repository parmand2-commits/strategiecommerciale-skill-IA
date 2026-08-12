---
name: parole-d-ordre-audit-agents-ia
version: 1.0.0
description: >
  Auditer l'identité et la gouvernance des agents IA d'une organisation : inventaire des agents
  déclarés, détection des angles morts (agents fantômes, shadow IT, anciens prestataires),
  vérification de la « parole d'ordre » (qui peut déclencher, quelles données, qui est responsable),
  plan d'action priorisé par risque et modèle de registre. Déclencheurs : "audit mes agents IA",
  "quels agents IA avons-nous", "gouvernance IA", "registre des agents", "sécurité des agents",
  "recenser mes outils IA", demande DPO/RSSI.
  Compatible avec tout agent : copier INSTRUCTIONS.md comme prompt système si pas de système de skills.
---

# Parole d'Ordre — Audit d'identité des agents IA

Applique la discipline romaine de la parole d'ordre à la gouvernance des agents IA :
**avant chaque bataille, les légions changeaient la parole d'ordre — quiconque ne la connaissait
pas était un ennemi.** Transposé à l'IA : tout agent non identifié, non enregistré, aux accès
non maîtrisés est un risque.

> Principe doctrinal (article « La Parole d'Ordre ») : registre, permissions, données fiables.
> Sans identification des agents avant l'ouverture du feu, le tir fratricide est assuré.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste

Lire `TOOLS.md` : profil organisation (taille, secteur, réglementation), outils connectés
(inventaire des agents si un outil de gouvernance existe), préférences.

### 0b. Mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Liste d'agents déclarés** | Noms, usages, accès, propriétaires | Auditer chaque agent (Étape 1) |
| **Contexte seul** | « On utilise plusieurs outils IA… » | Commencer par l'inventaire via questions |
| **Demande DPO/RSSI** | Contexte réglementaire (RGPD, secteur régulé) | Prioriser les accès aux données personnelles |

Demander si absent : la liste des agents connus (nom, usage, accès, propriétaire) et le
contexte (registre existant ? prestataires ? incidents ?).

---

## Étape 1 — Inventaire

Pour chaque agent déclaré, collecter/évaluer :
- **Nom** et usage réel (pas l'usage déclaré — confronter)
- **Accès** : quelles données, quels systèmes (CRM, emails, API internes, données personnelles)
- **Propriétaire** : qui le maintient, qui peut le modifier
- **Niveau de risque** : faible (données publiques) / moyen (données internes) /
  **critique** (données personnelles, financières, santé, accès écriture)

## Étape 2 — Détection des angles morts

Poser les questions qui révèlent les agents non déclarés :
- Outils IA utilisés par les équipes sans validation IT (shadow IT) ?
- Agents créés par d'anciens prestataires ou d'anciens employés — toujours actifs ?
- Extensions de navigateur, assistants personnels connectés aux outils pro ?
- API de modèles accessibles sans registre (clés partagées, comptes personnels) ?
- Agents hérités de tests/PoC jamais décommissionnés ?

## Étape 3 — Vérification de la parole d'ordre (par agent)

Pour chaque agent (déclaré ou suspecté), répondre à :
1. **Qui peut le déclencher ?** (accès ouvert à tous = risque)
2. **Quelles données peut-il voir ?** (principe du moindre privilège)
3. **Qui est responsable ?** (propriétaire identifié, joignable)
4. **Que se passe-t-il s'il est compromis ?** (impact, détection, remédiation)

Statut par agent : **OK** (parole d'ordre connue et maîtrisée) / **À renforcer** /
**Critique** (parole d'ordre inconnue = agent ennemi potentiel).

## Étape 4 — Plan d'action et registre

1. **Plan d'action priorisé par risque** : critique d'abord, avec responsable et échéance.
2. **Modèle de registre** : proposer les champs à collecter pour chaque agent
   (nom, version, propriétaire, accès, données, déclencheurs, revue, décommissionnement).

---

## Étape 5 — Contrôle qualité

- [ ] Chaque agent déclaré est audité (statut attribué)
- [ ] Les angles morts sont listés AVEC les questions pour les détecter
- [ ] Le plan d'action classe par risque critique → faible
- [ ] Un modèle de registre est proposé (réutilisable)
- [ ] Rien n'est inventé : les accès inconnus sont signalés « à vérifier », pas devinés

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Aucune liste d'agents fournie | Commencer par les questions d'inventaire (Étape 2) |
| Accès inconnus | Signaler « à vérifier » — ne pas deviner |
| Secteur régulé (banque, santé, assurance) | Alerter sur les exigences spécifiques (DPO, registre obligatoire) |
| Agents d'anciens prestataires | Risque critique par défaut — décommissionnement prioritaire |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** — profil + réglementation |
| `INSTRUCTIONS.md` | Agents sans système de skills |
| `references/TEMPLATE.md` | Avant la sortie — structure du livrable |
