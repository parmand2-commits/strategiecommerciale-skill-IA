# Salle d'Armes : les skills

Les armes IA de la [Salle d'Armes](https://strategiecommerciale.eu/salle-darmes-armurerie/),
la bibliothèque d'outils de [strategiecommerciale.eu](https://strategiecommerciale.eu) : la
stratégie militaire appliquée à la stratégie commerciale.

Chaque skill s'ancre sur un article publié du blog, produit un livrable nommé avec ses seuils
chiffrés, et fonctionne avec n'importe quel agent. Aucune dépendance entre skills : un dossier,
une arme.

## Installation

Une skill est un dossier autonome. Le chargeur de votre agent fait le reste.

| Environnement | Méthode |
|---|---|
| Agent avec système de skills | Copier le dossier de la skill dans le répertoire de skills de votre agent |
| Agent sans système de skills | Copier le contenu de `INSTRUCTIONS.md` comme prompt système |
| Agent conversationnel | Coller `INSTRUCTIONS.md` comme première instruction de la conversation |
| Automatisation | Brancher la sortie JSON, décrite dans `TOOLS.md`, sur votre orchestrateur |

Renseignez `TOOLS.md` avant le premier usage : profil de votre organisation, outils connectés,
langue et format de sortie. Sans ce fichier, la skill fonctionne en mode dégradé.

## Les skills

| Skill | Version | Ce qu'elle produit | Article ancre |
|---|---|---|---|
| [`audit-latence-commerciale-ooda`](./audit-latence-commerciale-ooda/) | 1.0.0 | Auditer la latence commerciale d'un segment en mesurant quatre latences sur les vingt dernières opportunités : délai entre le premier signal et la première action humaine, sources tierces ayant construit le cadrage du comité d'achat, rapport entre les réunions internes du comité et les réunions menées avec le vendeur, et délai entre l'accord verbal et la signature. | Boucle OODA : reprendre le tempo de la décision commerciale |
| [`audit-potentiel-expansion-nrr`](./audit-potentiel-expansion-nrr/) | 1.0.0 | Cartographier la base clients d'une organisation sur trois axes (santé du compte, potentiel d'expansion, signaux de maturité), vérifier la réserve bloquante du taux de renouvellement net (NRR), puis sélectionner 3 à 5 comptes par commercial et par trimestre. | Expansion client : vos meilleurs clients sont votre prochaine victoire |
| [`audit-visibilite-ia-geo`](./audit-visibilite-ia-geo/) | 1.0.0 | Auditer la visibilité d'une marque B2B dans les réponses des assistants conversationnels et des moteurs génératifs, avant que l'acheteur n'établisse sa shortlist. | Visibilité IA : soyez vu avant d'être shortlisté, comme à Midway |
| [`codifier-savoir-tribal-skills`](./codifier-savoir-tribal-skills/) | 1.0.0 | Transformer le savoir non écrit d'une force de vente en skills versionnées : cartographier les détenteurs du savoir tribal, extraire les règles maison par entretien et par analyse des livrables réels, tenir la revue mensuelle de deux affaires dont le livrable est un document, puis gérer un portefeuille de cinq à huit skills, une par moment de vérité du cycle de vente. | La Mémoire du Régiment : le savoir tribal de vos agents IA |
| [`coup-doeil-pre-call-briefing`](./coup-doeil-pre-call-briefing/) | 1.2.0 | Produire un briefing de pré-appel (pre-call brief) complet en 10 minutes pour un commercial B2B : synthèse du compte, contexte sectoriel, 3 angles d'attaque, questions à poser, brouillard à lever et friction d'exécution à parer. | Instinct commercial vs IA : le coup d'œil de Napoléon |
| [`diagnostic-architecture-tarifaire`](./diagnostic-architecture-tarifaire/) | 1.0.0 | Conduire un diagnostic d'architecture tarifaire pour un éditeur de logiciel en trois questions argumentées : quelle part de la valeur existe sans usage intensif, quel risque d'exécution l'éditeur accepte de porter, et le modèle reste-t-il lisible. | Pricing SaaS 2026 : le paradoxe 97/94 expliqué |
| [`logistique-bradley-enablement-gap`](./logistique-bradley-enablement-gap/) | 1.0.1 | Auditer le « réseau de ravitaillement » commercial (sales enablement) d'une organisation : contenus, playbooks, outils et formations dont les commerciaux disposent réellement face à ceux dont ils ont besoin pour gagner. | La logistique de Bradley : quand le sales enablement décide de vos win rates |
| [`meddpicc-deal-audit`](./meddpicc-deal-audit/) | 2.2.0 | Auditer, extraire et alimenter la qualification MEDDPICC d'une opportunité commerciale B2B, et fortifier un compte existant. | MEDDIC : Pourquoi vos Sales répètent-ils les erreurs de Crécy, Poitiers et Azincourt ? |
| [`mules-de-marius-temps-vente`](./mules-de-marius-temps-vente/) | 1.0.1 | Auditer le temps de vente B2B d'une équipe commerciale et identifier les « chariots inutiles » : les tâches administratives que personne ne lit et qui ne produisent aucun revenu. | Vos commerciaux sont des gratte-papiers : récupérez leur temps de vente B2B |
| [`neuf-terrains-portfolio-triage`](./neuf-terrains-portfolio-triage/) | 1.0.1 | Trier un portefeuille d'opportunités commerciales avec la grille des Neuf Terrains de Sun Tzu : classer chaque compte dans un terrain, déduire la posture recommandée (investir, accélérer, décrocher, contourner, consolider) et prioriser les 3 comptes qui méritent 80 % de l'effort. | Cartographier votre portefeuille clients : les 9 terrains de Sun Tzu |
| [`ordre-emploi-cas-usage-ia`](./ordre-emploi-cas-usage-ia/) | 1.0.0 | Rédiger l'ordre d'emploi des cas d'usage IA d'une fonction commerciale : une page par processus, écrite avant toute démonstration d'éditeur, fixant la tâche confiée, le rôle qui la porte, la sortie attendue, le contrôle et le propriétaire du résultat. | Sedan 1870 : le déploiement de l'IA commerciale se gagne à l'état-major |
| [`parole-d-ordre-audit-agents-ia`](./parole-d-ordre-audit-agents-ia/) | 2.0.0 | Auditer l'identité et la gouvernance des agents IA d'une organisation : inventaire des agents déclarés, détection des angles morts (agents fantômes, shadow IT, anciens prestataires), vérification de la parole d'ordre, seconde clé sur les actions irréversibles, surveillance du raisonnement, mandat d'agent en trois limites, cloisonnement lecture/action, adoption et propriétaire métier, plan d'action par risque et registre en livrable final. | Sécuriser l'identité de vos agents IA : la Parole d'Ordre |
| [`pas-de-tir-sparring-client`](./pas-de-tir-sparring-client/) | 1.0.1 | Sparring client IA : drill hebdomadaire de roleplay où l'IA joue le client difficile sur un cas réel, avec niveaux d'imprévisibilité et curveballs d'équipement, pour entraîner les réflexes des commerciaux. | L'IA va-t-elle remplacer les commerciaux ? La leçon des Forces Spéciales |
| [`protocole-pilote-ia-verdict`](./protocole-pilote-ia-verdict/) | 1.0.0 | Cadrer un pilote d'IA commerciale à métrique unique et rendre un verdict daté à chaque revue trimestrielle. | La Friction de Clausewitz : mesurer le ROI de votre IA commerciale |
| [`veille-concurrentielle`](./veille-concurrentielle/) | 1.1.2 | Qualifier et mesurer une veille concurrentielle B2B : transformer des changements relevés sur des sources publiques en signaux notés sur neuf, en briefs datés et en indicateurs de contribution. | Veille concurrentielle : mesurer ce que la cellule apporte vraiment |

## Ajouter une skill

Un dossier `kebab-case` par skill, quatre fichiers obligatoires :

```
<nom-kebab-case>/
├── SKILL.md                  orchestration, pour les agents qui lisent les skills
├── INSTRUCTIONS.md           le même contenu en prompt système autonome
├── TOOLS.md                  manifeste de configuration
├── references/TEMPLATE.md    gabarit de sortie annoté
└── examples/                 un exemple de sortie complète
```

Règles de la maison, contrôlées automatiquement à chaque proposition :

- la skill s'ancre sur un article publié du blog, cité dans le frontmatter ;
- le frontmatter de `SKILL.md` ne porte que `name`, `version` (semver) et `description` ;
- `name` est identique au nom du dossier ;
- `INSTRUCTIONS.md` est autonome : il ne cite aucun autre fichier du dossier ;
- aucun tiret cadratin ni demi-cadratin, dans aucun fichier ;
- aucun chemin absolu de machine ;
- aucune dépendance à une plateforme d'agent : les environnements ne sont cités que dans le
  bandeau de compatibilité ;
- toute donnée chiffrée porte sa source et sa date ;
- une ligne vide précède chaque titre markdown.

## Vérification

Chaque proposition passe un contrôle avant publication : structure du dossier, frontmatter,
absence de tiret cadratin, sources datées. Une skill non conforme n'est jamais publiée.

## Licence

MIT pour le code et les prompts, voir `LICENSE`. Les données produit citées dans les exemples
restent la propriété de leurs éditeurs.
