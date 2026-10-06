# INVENTAIRE DU TRAIN DE BAGAGES : Exemple complet

> **Exemple golden file** : sortie de référence de la skill « Mules de Marius » sur le scénario
> de test fixture-11 (ETI négoce B2B, 28 commerciaux). Cet exemple illustre la structure
> attendue : inventaire en trois colonnes, diagnostic chiffré, plan d'automatisation et plan
> de réforme. Les données sont fictives.

---

## INVENTAIRE DU TRAIN DE BAGAGES

**Organisation :** MateriauxPro (fictif) · **Date :** 26/08/2026 · **Effectif commercial :** 28 (SDR, AE, AM)
**Stack détectée :** Salesforce (CRM), reporting manuel dans Excel, 3 outils de prospection
déconnectés, e-mailing, conversation intelligence non déployé

---

## 1. INVENTAIRE EN TROIS COLONNES

| Activité | Fréquence | h/sem./commercial | Qui la lit ? | Quelle décision ? | Colonne |
|---|---|---|---|---|---|
| Saisie des comptes rendus d'appels | Quotidienne | 10,0 | Personne (tableau de bord consulté 1×/trimestre) | Aucune | **Chariot** |
| Mise à jour des opportunités | Continue | 4,0 | Sales manager | Revue de pipeline hebdo | Charge utile |
| Reporting hebdo | Hebdomadaire | 2,0 | Comité de direction | Prévisionnel de CA mensuel | Charge de commandement |
| Réunions internes | Hebdomadaire | 5,0 | Manager et équipe | Coordination (2 h utiles) / rituel sans décision (3 h) | Mixte : 3 h **chariot** |
| Prospection (e-mails, appels sortants) | Quotidienne | 8,0 | Le commercial lui-même | Pipeline entrant | Charge utile |
| RDV et appels clients | Quotidienne | 14,0 | Le commercial, le client | Avancement des deals | Charge utile |
| Administratif résiduel (devis, relances manuelles) | Quotidienne | 2,0 | Personne d'identifiable | Aucune | **Chariot** |

> Justification des lignes douteuses : la saisie des CR alimente un tableau de bord que le
> comité consulte une fois par trimestre : aucun deal n'en dépend, aucun manager ne la lit.
> C'est le chariot type de l'article : « un champ rempli pour qu'une colonne d'un tableau ne
> reste pas vide ».

## 2. DIAGNOSTIC

- **Temps perdu (chariots) :** 15 h/semaine par commercial → **420 h/semaine → 12 ETP gaspillés
  sur 28** (43 % du temps commercial) → **≈ 756 000 €/an** (coût chargé médian 90 k€).
- **Chariots priorisés :**
  1. Saisie des comptes rendus (10 h) : le plus lourd, aucun lecteur identifié
  2. Réunions internes (3 h de rituel sans décision) : le plus « politique » à couper
  3. Administratif résiduel (2 h) : recopies et relances manuelles
- **Causes racines :** 12 champs obligatoires à la création d'opportunité, rituel de reporting
  hérité d'une époque sans CRM, outils de prospection déconnectés du CRM (recopies manuelles),
  aucune autorité en charge de la cohérence de la stack.
- **Signaux de fragmentation :** reporting hebdo recopié à la main dans Excel, 3 outils de
  prospection qui n'écrivent rien dans Salesforce, conversation intelligence jamais déployé.

## 3. PLAN D'AUTOMATISATION (MANŒUVRE 2 : LA CAPTURE REMPLACE LA SAISIE)

| Charge cible | Catégorie de capteur | Gain estimé | Coût d'entrée | Prérequis | Risque |
|---|---|---|---|---|---|
| Saisie des CR d'appels (10 h) | **Conversation intelligence** + **capture d'activité** | 8 h/sem. × 28 comm. | moyen | Adoption par les commerciaux, conformité RGPD (enregistrement) | Résistance au micro |
| Logging des e-mails et réunions (inclus dans la saisie) | **Capture d'activité** (synchronisation automatique vers le CRM) | 2 h/sem. × 28 comm. | faible | Connecteur Salesforce activé | Confidentialité des échanges |
| Administratif résiduel (2 h) | **Intégrations natives / API** (devis et relances depuis le CRM) | 1,5 h/sem. × 28 comm. | faible | Map des flux, CRM de référence | Périmètre des intégrations |
| Reporting hebdo (2 h) | **Intégration CRM → BI** (extraction automatique) | 1,5 h/sem. × 28 comm. | faible | Tableau de bord dédié | - |

**Coupes immédiates (chariots purs : trimestre, sans négociation) :**
- Saisie des CR : supprimer les champs obligatoires inutiles à la création d'opportunité
  (réglage administrateur d'une demi-journée sur Salesforce) : 10 h/semaine récupérées
  immédiatement, sans achat.
- Rituel de réunions : réduire à 2 h/semaine avec ordre du jour écrit et décisions actées.

**Capteurs à déployer (par gain décroissant) :**
1. Conversation intelligence + capture d'activité, responsable : sales ops, échéance J60
2. Intégration CRM → BI pour le reporting, responsable : sales ops, échéance J90
3. Intégrations devis/relances, responsable : RevOps (à nommer), échéance J90

> ⚠ Garde-fou : chaque passerelle agentique ajoute de la complexité. Aucune recommandation
> d'agent de logging n'est faite ici tant que la capture native n'est pas déployée : l'arbitrage
> appartient au commandement, une usine à gaz agentique serait un chariot de plus.

## 4. PLAN DE RÉFORME 30-60-90

| Horizon | Actions | Responsable |
|---|---|---|
| **30 jours** | Supprimer les champs CR inutiles, réduire le rituel de réunions à 2 h, désigner le responsable du plan, mesurer le temps réellement récupéré | Sales ops |
| **60 jours** | Déployer conversation intelligence + capture d'activité sur l'échantillon pilote (5 commerciaux), mesurer le gain réel vs les 8 h estimées | Sales ops |
| **90 jours** | Étendre à toute l'équipe, automatiser le reporting (CRM → BI), nommer un RevOps avec droit de veto sur tout nouvel outil sans intégration native | Direction |

**Indicateur unique :** part du temps commercial passée en interaction client, mesurée
trimestre après trimestre (cible : +20 points sous 3 trimestres).

---

*Audit généré par la skill « Mules de Marius », strategiecommerciale.eu. Un champ rempli pour
qu'une colonne d'un tableau ne reste pas vide est un chariot de commodités, et Marius l'aurait
brûlé avant l'aube.*
