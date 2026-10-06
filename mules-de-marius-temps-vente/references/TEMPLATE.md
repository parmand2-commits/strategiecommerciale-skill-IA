# TEMPLATE.md · Inventaire du train de bagages : [Organisation]

> **Note pour l'agent** : template de sortie. Remplir chaque champ, supprimer les annotations.

---

## INVENTAIRE DU TRAIN DE BAGAGES

**Organisation :** [Nom] · **Date :** [JJ/MM/AAAA] · **Effectif commercial :** [N]
**Stack détectée :** [CRM + outils principaux, connectés ou fragmentés]

---

## 1. INVENTAIRE EN TROIS COLONNES

| Activité | Fréquence | h/sem./commercial | Qui la lit ? | Quelle décision ? | Colonne |
|---|---|---|---|---|---|
| [saisie des comptes rendus d'appels] | quotidienne | 2,0 | [personne nommable] | [décision] | **Chariot** / Charge de commandement / Charge utile |
| … | | | | | |

> Justification d'une ligne par ligne douteuse. La saisie qui alimente un tableau de bord mort
> est un convoi de mulets ; la donnée qui sert le deal est le paquetage du légionnaire.

## 2. DIAGNOSTIC

- **Temps perdu (chariots)** : [X] h/semaine → [Y] ETP gaspillés ([Z] % de l'effectif) → [coût annuel € si fourni]
- **Chariots priorisés** (par temps × fréquence × personnes concernées) :
  1. [activité] : [impact]
  2. …
- **Causes racines** : [champs obligatoires excessifs / rituels hérités / outils déconnectés…]
- **Signaux de fragmentation** : [recopies manuelles, tableurs parallèles, outils jamais ouverts]

## 3. PLAN D'AUTOMATISATION (MANŒUVRE 2 : LA CAPTURE REMPLACE LA SAISIE)

| Charge cible | Catégorie de capteur | Gain estimé | Coût d'entrée | Prérequis | Risque |
|---|---|---|---|---|---|
| [logging e-mails/réunions] | **Capture d'activité** | [X] h/sem. × [N] comm. | faible | [CRM avec connecteur] | [confidentialité] |
| … | | | | | |

**Coupes immédiates (chariots purs : trimestre, sans négociation) :**
- [activité] : suppression (réglage administrateur d'une demi-journée sur la plupart des CRM)

**Capteurs à déployer (par gain décroissant) :**
1. [catégorie] : responsable [X], échéance [Y]
2. …

> ⚠ Garde-fou : chaque passerelle agentique ajoute de la complexité. L'arbitrage appartient au
> commandement : une usine à gaz agentique est un chariot de plus, pas un allègement.

## 4. PLAN DE RÉFORME 30-60-90

| Horizon | Actions | Responsable |
|---|---|---|
| **30 jours** | [supprimer chariots purs, alléger champs obligatoires, désigner responsable] | [qui] |
| **60 jours** | [déployer le premier capteur, mesurer le temps récupéré] | [qui] |
| **90 jours** | [étendre aux charges de commandement, unifier les outils] | [qui] |

**Indicateur unique :** part du temps commercial passée en interaction client (trimestre après
trimestre). Perspective RevOps à horizon : responsable unique + droit de veto sur tout nouvel
outil sans intégration native avec le CRM de référence.

---

*Audit généré par la skill « Mules de Marius », strategiecommerciale.eu. Un champ rempli pour
qu'une colonne d'un tableau ne reste pas vide est un chariot de commodités, et Marius l'aurait
brûlé avant l'aube.*
