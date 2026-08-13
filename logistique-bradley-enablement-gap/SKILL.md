---
name: logistique-bradley-enablement-gap
version: 1.0.0
description: >
  Auditer le « réseau de ravitaillement » commercial (sales enablement) d'une organisation :
  contenus, playbooks, outils et formations dont les commerciaux disposent réellement face à
  ceux dont ils ont besoin pour gagner. Produit un diagnostic du gap d'enablement relié aux
  4 métriques que la direction regarde (productivité, win rate, quota attainment, durée du cycle),
  et un plan d'action priorisé. Déclencheurs : "audit enablement", "gap sales enablement",
  "pourquoi nos commerciaux ne gagnent pas", "contenus manquants", "playbooks", "onboarding",
  "30h perdues à chercher du contenu".
  Inspiré de l'article « La logistique de Bradley » : amateurs talk tactics, professionals talk logistics.
  Compatible avec tout agent : copier INSTRUCTIONS.md comme prompt système si pas de système de skills.
---

# Logistique de Bradley — Sales Enablement Gap

Applique la leçon de Bradley à l'organisation commerciale : **on ne gagne pas avec des tacticiens
de génie, on gagne avec des camions**. Votre enablement (contenus, playbooks, outils, formations)
est votre Red Ball Express — ou il n'est rien. Cette skill audite l'écart entre l'équipement
réel des commerciaux et celui dont ils ont besoin, et le relie aux chiffres que la direction regarde.

> Principe doctrinal (article « La logistique de Bradley ») : le benchmark Seismic 2026 relie
> l'enablement au win rate, au quota attainment et à la durée du cycle. Un outil qui ne fait
> bouger aucun de ces chiffres n'est pas un outil d'enablement — c'est une bibliothèque de
> contenus coûteuse. Gartner : 50 % des vendeurs se sentent submergés par leurs outils ;
> Seismic : 30 h/mois perdues à chercher du contenu.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste

Lire `TOOLS.md` : profil organisation (taille, secteur, offre), outils connectés (enablement
platform, CRM, conversation intelligence), préférences. Absent/vide → mode dégradé : audit sur
les réponses fournies.

### 0b. Mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Réponses à un questionnaire** | L'utilisateur décrit contenus/outils/formations | Auditer ce qui est déclaré (Étape 1) |
| **Données d'outils connectés** | Enablement platform / CRM / conversation via TOOLS.md | Croiser les données réelles (usage, recherche, appels) |
| **Contexte seul** | « Je sens qu'on sous-équipe nos commerciaux » | Poser les questions de l'Étape 1 puis auditer |

Demander si absent (le minimum pour un audit utile) :
1. Effectif commercial et rôles (SDR, AE, AM, management)
2. Stack d'outils déclarée (10-15 outils ? lesquels ?)
3. Contenus/playbooks disponibles (lesquels, à jour ?)
4. Processus d'onboarding (durée, contenu)
5. Les 4 métriques si connues (win rate, quota attainment, durée de cycle, productivité)

---

## Étape 1 — Cartographie de l'équipement réel

Pour chaque dimension, établir **ce qui existe réellement** (pas ce qui est déclaré au
management) :

1. **Contenus** : études de cas, comparatifs, argumentaires, réponses aux objections.
   Sont-ils à jour (< 12 mois) ? Trouvables en < 3 clics ? Adaptés par secteur/étape ?
2. **Playbooks** : scripts d'appel, séquences, guides de négociation, playbooks par persona.
   Utilisés ou décoratifs ?
3. **Outils** : combien de tools par commercial (10-15 ?), lesquels sont réellement utilisés
   vs imposés ? Chevauchements ?
4. **Formation & coaching** : onboarding (durée vs marché), formation continue, coaching
   managérial régulier ou ponctuel ?
5. **IA** : les commerciaux ont-ils accès à des assistants IA ? Les utilisent-ils (50 % se
   sentent submergés — l'IA peut aggraver ou résoudre) ?

## Étape 2 — Identification du gap

Pour chaque dimension, calculer l'écart entre l'équipement réel et le besoin :
- **Contenus manquants** : qu'est-ce qui manque pour gagner les deals en cours (par étape du cycle) ?
- **Playbooks absents** : quelles situations récurrentes n'ont pas de procédure ?
- **Surcharge d'outils** : quels outils supprimer/fusionner (l'objectif n'est pas d'ajouter,
  c'est de ravitailler efficacement) ?
- **Formation** : quel est le coût d'un onboarding trop long (en deals perdus) ?

Repérer les signaux classiques de gap :
- Commerciaux qui réinventent des contenus à chaque deal (pas de playbook)
- Recherche de contenu > 15 min (vs 30 h/mois moyenne)
- Outils payés mais inutilisés (découvrir lesquels via les données d'usage si disponibles)
- Onboarding > 3 mois sans structure

## Étape 3 — Relier aux 4 métriques

Pour chaque gap identifié, expliciter l'impact probable sur les 4 métriques direction :
productivité, win rate, quota attainment, durée du cycle. Formuler en hypothèse chiffrée
(ex : « un playbook de négociation pourrait réduire le cycle de 15 % sur les deals > 50 k€ »)
— hypothèse, jamais certitude.

## Étape 4 — Plan d'action (Red Ball Express)

1. **Priorités** : 3 actions maximum qui auraient l'impact le plus fort (pas de liste de 20).
2. **Par action** : quoi, pour qui, pourquoi (lien métrique), estimation d'effort, quick win ?
3. **Ce qu'il faut retirer** : outils redondants, contenus obsolètes, process morts.

---

## Étape 5 — Contrôle qualité

- [ ] Chaque dimension (contenus, playbooks, outils, formation, IA) est couverte ou explicitement non évaluée
- [ ] Les gaps sont concrets (situations, exemples), pas génériques
- [ ] Chaque action est reliée à au moins une métrique
- [ ] Maximum 3 priorités
- [ ] Les données inconnues sont signalées, jamais inventées

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Aucune donnée fournie | Poser les questions minimales avant d'auditer |
| Outils inconnus | Signaler « à vérifier » — ne pas supposer |
| Métriques inconnues | Auditer quand même, marquer les impacts comme hypothèses |
| Organisation sans enablement dédié | Le signaler : c'est déjà un gap en soi (pas de Red Ball Express) |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** — profil + connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills |
| `references/TEMPLATE.md` | Avant la sortie — structure du livrable |
