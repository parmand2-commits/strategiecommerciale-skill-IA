# TOOLS.md : manifeste de configuration

Renseignez ce fichier avant le premier usage. Sans lui, la skill fonctionne en mode dégradé,
c'est-à-dire à partir de ce que l'utilisateur fournit à la main.

## Langue et format

| Réglage | Valeur | Commentaire |
|---|---|---|
| `langue` | `fr` | Langue de tous les livrables |
| `format_sortie` | `markdown` | Valeurs admises : `markdown`, `docx`, `json` |
| `profondeur` | `standard` | Valeurs admises : `bref`, `standard`, `complet` |
| `dossier_skills` | `skills/` | Emplacement du corpus de skills de l'organisation |
| `dossier_livrables` | `savoir-tribal/` | Emplacement des livrables de cet audit |

En sortie `json`, la structure suit `references/TEMPLATE.md` : un objet par livrable, les mêmes
intitulés de champs que les colonnes des tableaux.

## Profil de l'organisation

| Champ | Valeur | Effet sur le livrable |
|---|---|---|
| `effectif_commercial` | à renseigner | Détermine le nombre attendu de détenteurs du savoir |
| `secteur` | à renseigner | Oriente les moments de vérité (cycle long ou court, appels d'offres) |
| `cycle_de_vente` | à renseigner | En jours ou en mois, cadre la revue mensuelle |
| `anciennete_moyenne` | à renseigner | Une équipe jeune a peu de savoir tribal, une équipe senior en a beaucoup et le perd en bloc |
| `segments` | à renseigner | Un corpus par segment si les moments de vérité diffèrent |
| `sensibilite_rh` | `normale` | Valeurs : `normale`, `elevee`. En `elevee`, les noms des détenteurs restent internes |

## Outils disponibles

### Recherche web (obligatoire)

Utilisée pour dater les références externes et vérifier une pratique de marché. Toute donnée
chiffrée reprise dans un livrable porte sa source et sa date. Une source de plus de douze mois
est rejetée ou signalée comme non confirmée.

### CRM, en lecture seule (optionnel)

Exemples d'intégration : Salesforce, HubSpot, Pipedrive, Dynamics.

| Usage | Ce qu'on y cherche |
|---|---|
| Sélection des affaires à passer en revue | Affaires gagnées et perdues des douze derniers mois, par segment |
| Croisement des détenteurs | Personnes mises en copie ou en validation sur les affaires inhabituelles |
| Mesure d'usage des skills | Activités rattachées aux moments de vérité couverts par le corpus |

Aucune écriture n'est effectuée par cette skill. Le CRM est consulté, jamais modifié.

### Conversation intelligence, en lecture seule (optionnel)

Exemples d'intégration : Gong, Chorus, Clari Copilot.

Usage : retrouver les passages d'appel où un senior change de méthode par rapport au process, et
les objections récurrentes non consignées. Ces passages alimentent la partie 2b de la SKILL.md.

### Entrepôt documentaire, en lecture seule (optionnel)

Exemples d'intégration : SharePoint, Google Drive, Notion.

Usage : lire les courriels de relance réellement envoyés, les comptes rendus de rendez-vous et
les propositions signées. C'est la matière de l'analyse du livrable réel.

### Messagerie d'équipe, en lecture seule (optionnel)

Usage : repérer les fils d'arbitrage où un senior est sollicité. C'est la source
comportementale de la cartographie des détenteurs.

## Connecteurs en écriture : désactivés par défaut

Aucun connecteur d'écriture n'est actif. Si vous en activez un, il porte quatre règles de garde.

1. **Jamais d'écriture sans affichage préalable.** Le contenu destiné à être écrit est montré en
   entier avant l'écriture, sur la ressource exacte visée.
2. **Jamais de remplacement de valeur existante en silence.** Un écrasement est présenté en
   comparaison côte à côte, ancienne valeur et nouvelle valeur, avec sa justification.
3. **Jamais d'écriture sur une ressource partagée sans propriétaire identifié.** Le registre des
   skills appartient à un propriétaire nommé. À défaut, aucune écriture.
4. **Toute écriture est datée et attribuée.** La ligne écrite porte la date et la source de la
   modification, sans quoi la prochaine revue ne peut rien arbitrer.

## Mode dégradé

Quand `TOOLS.md` est absent ou incomplet, et qu'aucun connecteur n'est disponible :

- la cartographie des détenteurs repose sur la seule source déclarative, ce qui est signalé dans
  le livrable ;
- l'analyse du livrable réel n'est pas exécutée, seules les pièces fournies par l'utilisateur
  sont lues ;
- la sortie est en Markdown, en langue française ;
- le profil de l'organisation est traité comme générique, ce qui interdit toute conclusion
  chiffrée sur le nombre attendu de détenteurs ou de moments de vérité.

Le livrable en mode dégradé reste utile, à condition que ses limites soient écrites dans le
livrable lui-même. Un audit partiel présenté comme complet est un faux document.

## Sécurité

- Aucune donnée nominative de client final ne sort du livrable sans nécessité : les affaires sont
  désignées par un identifiant court, pas par le nom du client, quand la sensibilité est élevée.
- Les noms des détenteurs du savoir restent internes à l'organisation.
- Aucune donnée issue des connecteurs n'est recopiée dans un livrable destiné à un tiers.
