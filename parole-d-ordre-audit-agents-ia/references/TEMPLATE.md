# TEMPLATE.md : Audit de la Parole d'Ordre : [Organisation]

> **Note pour l'agent** : gabarit de sortie. Remplir chaque champ, supprimer les annotations.
> Les sections 1 à 10 sont obligatoires. Le registre (section 10) est le livrable final.

---

## AUDIT DE LA PAROLE D'ORDRE

**Organisation :** [Nom] · **Date :** [JJ/MM/AAAA] · **Secteur régulé :** [Oui/Non]
**Agents audités :** [N déclarés + N agents fantômes]
**Propriétaire de l'audit :** [Nom, fonction] · **Périmètre :** [entité, période]

---

## 1. INVENTAIRE DES AGENTS

<!-- Une ligne par agent déclaré. L'usage est l'usage réel, confronté au déclaré. Le risque :
     faible (données publiques), moyen (données internes), critique (données sensibles ou
     accès en écriture). Un agent sans propriétaire nommé est critique par défaut. -->

| Agent | Usage | Accès | Propriétaire | Risque |
|---|---|---|---|---|
| [Nom] | [usage réel] | [données/systèmes] | [qui] | Faible / Moyen / **Critique** |
| … | | | | |

## 2. ANGLES MORTS IDENTIFIÉS

<!-- Agents non déclarés : shadow IT, anciens prestataires, extensions, clés partagées, PoC
     jamais décommissionnés. Chaque angle mort porte le statut « à vérifier ». -->

- [Agent fantôme] : [origine] : statut « à vérifier »
- **Questions à poser pour les détecter :** [liste]

## 3. AUDIT PAR AGENT (parole d'ordre)

<!-- Quatre questions : qui déclenche, quelles données, qui est responsable, que se passe-t-il
     s'il est compromis. Statut : OK / À renforcer / Critique. -->

| Agent | Qui le déclenche ? | Données visibles | Responsable | Statut |
|---|---|---|---|---|
| [Nom] | [ouvert/restreint] | [données] | [qui] | OK / À renforcer / **Critique** |
| … | | | | |

## 4. LA RÈGLE DES DEUX (actions irréversibles)

<!-- Une ligne par action irréversible. Le validateur est indépendant s'il ne partage ni le
     jeton, ni le prompt, ni l'objectif chiffré de l'agent qui propose. -->

| Action irréversible | Agent | Seconde clé (validateur) | Indépendant ? | Trace |
|---|---|---|---|---|
| [envoi, paiement, remise, écriture] | [nom] | [agent ou humain] | Oui / **Non** | [journal] |
| … | | | | |

## 5. SURVEILLANCE DU RAISONNEMENT ET AUTONOMIE

<!-- Surveiller le raisonnement, pas le seul livrable. Trois alertes, un degré d'autonomie par
     agent, et l'audit du critère de notation utilisé pour le juger. -->

### 5a. Alertes de raisonnement

| Agent | Outil hors périmètre | Reprise en boucle | Écriture imprévue (ressource partagée) |
|---|---|---|---|
| [Nom] | [détecté / non] | [détecté / non] | [détecté / non] |
| … | | | |

### 5b. Dosage de l'autonomie

| Agent | Degré (1 lecture, 2 rédaction, 3 écriture approuvée, 4 autonomie) | Propriétaire | Retour arrière |
|---|---|---|---|
| [Nom] | [1 à 4] | [qui] | [chemin] |
| … | | | |

### 5c. Audit du critère de notation

| Agent | Ce qui est noté | Effet pervers possible | Correction |
|---|---|---|---|
| [Nom] | [critère] | [contournement] | [mesure] |
| … | | | |

## 6. MANDAT D'AGENT (trois limites)

<!-- Un mandat tient en trois limites mémorisables, pas en trente règles. Une règle que
     personne ne peut citer de mémoire n'est pas appliquée. -->

| Agent | Limite 1 | Limite 2 | Limite 3 | Seuil de remontée |
|---|---|---|---|---|
| [Nom] | [interdit] | [interdit] | [interdit] | [chiffré, ex. 48 h] |
| … | | | | |

## 7. CLOISONNEMENT ET QUARANTAINE

<!-- Séparation des privilèges : l'agent qui lit n'agit pas, l'agent qui agit n'ingère pas de
     contenu non sollicité. Le contenu externe est isolé et recoupé avant d'atteindre l'agent
     qui agit. -->

| Agent | Rôle (lecture/action) | Contenu externe ingéré | Quarantaine | Recoupement |
|---|---|---|---|---|
| [Nom] | [lecture / action] | [oui / non] | [oui / **non**] | [source] |
| … | | | | |

## 8. ADOPTION (point de contact, vallum, propriétaire métier)

<!-- Loger l'agent au point de contact réel, décrire le vallum de gouvernance des données,
     nommer un propriétaire métier, et situer le niveau du modèle de maturité. -->

| Cas d'usage | Point de contact | Niveau de maturité (1 à 4) | Propriétaire métier | Usage hebdo mesuré |
|---|---|---|---|---|
| [cas] | [objet opportunité, fiche contact] | [observation à autonomie] | [qui] | [%] |
| … | | | | |

**Vallum de gouvernance des données :** qui accède à quoi · quelles actions d'agent sont
tracées · qui valide · comment sortir.

## 9. PLAN D'ACTION PRIORISÉ

<!-- Critique d'abord, puis moyen, puis faible. Responsable nommé et échéance par ligne. -->

| Priorité | Action | Responsable | Échéance |
|---|---|---|---|
| **Critique** | [décommissionner, retirer un accès, second clé, tester l'interrupteur] | [qui] | [quand] |
| Moyen | [documenter, restreindre, planifier la revue] | [qui] | [quand] |
| Faible | [consigner au registre] | [qui] | [quand] |

## 10. REGISTRE DES AGENTS (livrable final)

<!-- Le registre vivant est le livrable final de l'audit. Une ligne par agent autorisé. -->

| Nom | Version | Propriétaire | Accès (données + systèmes) | Niveau d'autonomie | Seconde clé | Déclencheurs | Revue | Décommissionnement | Incidents |
|---|---|---|---|---|---|---|---|---|---|
| [Nom] | [x.y] | [qui] | [données/systèmes] | [1 à 4] | [qui] | [qui] | [période] | [procédure] | [N] |

---

*Audit généré par la skill « Parole d'Ordre », strategiecommerciale.eu*
