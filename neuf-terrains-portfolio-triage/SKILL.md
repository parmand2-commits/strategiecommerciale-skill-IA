---
name: neuf-terrains-portfolio-triage
version: 1.0.0
description: >
  Trier un portefeuille d'opportunités commerciales avec la grille des Neuf Terrains de Sun Tzu :
  classer chaque compte dans un terrain, déduire la posture recommandée (investir, accélérer,
  décrocher, contourner, consolider) et prioriser les 3 comptes qui méritent 80% de l'effort.
  Déclencheurs : "trie mon portefeuille", "prioriser mes deals", "revue de pipeline", "quels comptes
  attaquer cette semaine", "cartographie de mon portefeuille", "quels deals abandonner".
  Compatible avec tout agent : copier INSTRUCTIONS.md comme prompt système si pas de système de skills.
---

# Neuf Terrains — Portfolio Triage

Applique la grille du chapitre XI de Sun Tzu au portefeuille commercial : chaque opportunité
occupe un terrain, et chaque terrain impose une posture. Le livrable est un tri actionnable :
**où concentrer la force, où décrocher, où contourner**.

> Principe doctrinal (article « Les Neuf Terrains de Sun Tzu ») : terrains possédés (clients),
> disputés (opportunités), contrôlés par l'ennemi (comptes concurrents). À chaque terrain
> correspond une posture — ne pas traiter un terrain grave comme un terrain léger.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste

Lire `TOOLS.md` : profil organisation (taille, secteur, offre), outils connectés, préférences.
Absent/vide → mode dégradé : analyse sur les données fournies seules.

### 0b. Mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Liste de comptes** | Tableau/lignes de deals | Classer chaque compte (Étape 1) |
| **CRM connecté** | Accès aux opportunités via TOOLS.md | Extraire le portefeuille, puis classer |
| **Fichier/export** | CSV, feuille, copier-coller | Normaliser, puis classer |

Demander si absent : la liste des comptes (nom, valeur, stade, dernier contact, champion si connu).
Si l'utilisateur dit « prends-les dans mon CRM » : utiliser les instructions du connecteur.

---

## Étape 1 — Classement par terrain

Pour **chaque** compte, déterminer le terrain dominant parmi les 9 :

| Terrain | Signaux | Posture |
|---------|---------|---------|
| **Dispersé** | Compte dans son confort, faible pression, qualification superficielle | Ne pas s'engager — attendre un signal plus fort |
| **Léger** | Premier contact, qualification incomplète | Avancer vite ou décrocher |
| **Disputé** | Prospect activement sollicité par des concurrents | Forcer la décision rapidement |
| **Ouvert** | Accès libre, pas de position dominante | Construire l'asymétrie informationnelle |
| **Carrefour** | Décision à forts enjeux, plusieurs parties influentes | Chercher des alliances (champions, partenaires) |
| **Grave** | Deal avancé, fort investissement mutuel | Consolider le champion, verrouiller le calendrier |
| **Difficile** | Cycle long, obstacles structurels (budget gelé, réorg) | Progression prudente, évaluer le coût d'opportunité |
| **Encerclé** | Concurrent très bien implanté | Ruse et différenciation radicale — pas de frontal |
| **Mortel** | Décision imminente, risque total de perte | Urgence maximale — le statu quo est la défaite |

Règles de classement :
- Le **stade** et la **présence d'un champion** sont les deux signaux les plus discriminants.
- Un deal « Négociation » sans champion ni accès à l'Economic Buyer = **terrain mortel déguisé en grave**.
- Un compte client existant = terrain possédé : vérifier s'il est en risque (churn) avant de l'ignorer.

---

## Étape 2 — Priorisation

1. **Top 3 de la semaine** : les 3 comptes qui méritent 80 % de l'effort, justifiés par le
   terrain + la valeur + la probabilité de mouvement rapide.
2. **À décrocher** : terrains dispersés/légers sans signal depuis > 60 jours, ou encerclés
   sans angle de différenciation.
3. **À re-qualifier** : comptes dont les données sont trop pauvres pour un classement fiable.

---

## Étape 3 — Sortie

Lire `references/TEMPLATE.md` et produire :
1. **Tableau de synthèse** : compte | terrain | posture | action (une ligne par compte).
2. **Analyse par terrain** : pour chaque terrain identifié, 2-3 phrases + action concrète.
3. **Priorités de la semaine** : 3 comptes max, avec justification stratégique.
4. **Signaux d'alerte** : terrains mortels/encerclés non traités, champions manquants.

---

## Étape 4 — Contrôle qualité

- [ ] Chaque compte est classé dans un terrain (aucun « non classé »)
- [ ] Chaque terrain a une action concrète (pas de prose doctrinale seule)
- [ ] La priorisation est justifiée (pourquoi ces 3-là, pas les 3 plus gros)
- [ ] Les comptes à décrocher sont explicitement nommés
- [ ] Les données manquantes (champion inconnu, stade flou) sont signalées, pas inventées

---

## Gestion des erreurs

| Situation | Comportement |
|-----------|-------------|
| Moins de 3 comptes fournis | Le signaler : le tri gagne en pertinence avec ≥ 5 comptes |
| Champion inconnu partout | Classer avec prudence, signaler l'incertitude sur les terrains |
| Comptes sans valeur | Utiliser le stade + dernier contact comme critères secondaires |
| CRM inaccessible | Mode dégradé sur les données fournies |

---

## Fichiers de référence

| Fichier | Quand le lire |
|---------|--------------|
| `TOOLS.md` | **En premier** — profil + connecteurs |
| `INSTRUCTIONS.md` | Agents sans système de skills |
| `references/TEMPLATE.md` | Avant la sortie — structure du livrable |
