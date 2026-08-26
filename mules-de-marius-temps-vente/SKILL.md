---
name: mules-de-marius-temps-vente
version: 1.0.0
description: >
  Utiliser ce skill pour auditer le temps de vente B2B d'une équipe commerciale et identifier
  les « chariots inutiles » : les tâches administratives que personne ne lit et qui ne produisent
  aucun revenu. Déclencheurs : « audit du temps de mes commerciaux », « mes commerciaux passent
  trop de temps en saisie/administratif », « récupérer du temps de vente », « chariots inutiles »,
  « mules de Marius », « inventaire du train de bagages », ou toute revue d'organisation
  commerciale avant un achat d'outil de productivité. Inspirée de la réforme de Marius (107 av.
  J.-C.) et de l'article « Vos commerciaux sont des gratte-papiers » du blog strategiecommerciale.eu.
  Compatible avec tout agent (Claude, ChatGPT, Gemini, Perplexity…) : sans système de skills,
  copier le contenu de INSTRUCTIONS.md comme prompt système.
---

# Mules de Marius — Audit du temps de vente B2B

Audite la charge administrative d'une équipe commerciale avec la méthode de Marius : inventorier
le train de bagages, distinguer la charge utile du chariot, puis remplacer la saisie par la capture.
Le livrable est un rapport « Inventaire du train de bagages » : classement de chaque activité en
trois colonnes, diagnostic du temps perdu, plan d'automatisation par catégorie d'outils et plan
de réforme 30-60-90 jours.

La doctrine : en 107 av. J.-C., Marius n'a pas allégé ses légionnaires, il a supprimé le train de
bagages (l'*impedimenta*) et transféré la charge utile sur le dos de l'homme. Chaque objet était
trié sur une question unique : sert-il au combat dans les quarante-huit heures ? Un rapport de
visite qui alimente la préparation du prochain rendez-vous est un pieu de palissade. Un champ
rempli pour qu'une colonne d'un tableau ne reste pas vide est un chariot de commodités — et Marius
l'aurait brûlé avant l'aube.

---

## Étape 0 — Initialisation

### 0a. Lire le manifeste d'outils

**Avant toute chose**, lire `TOOLS.md`. Ce fichier déclare :
- le profil de l'organisation (taille, secteur, effectif commercial, CRM de référence)
- la stack technologique et les connecteurs éventuels (CRM, conversation intelligence, API)
- le format de sortie et la langue

Si `TOOLS.md` est absent ou vide, continuer en mode dégradé gracieux : questions d'inventaire
seules, sortie Markdown, français.

### 0b. Détecter le mode d'entrée

| Mode | Signaux | Comportement |
|------|---------|--------------|
| **Relevé complet** | L'utilisateur fournit un relevé d'activité (2 semaines, template `references/RELEVE.md`) | Analyser ligne par ligne, classer |
| **Estimation** | L'utilisateur donne les grandes activités + heures hebdo | Consolider, questionner les usages aval |
| **Aucune donnée** | Rien de fourni | Mener l'inventaire par questions structurées (voir 1b) |

### 0c. Confirmer les inputs minimaux

Demander (seulement si non déjà fourni) :
1. **Effectif commercial** et répartition des rôles (SDR / AE / AM…)
2. **Les activités hebdomadaires** et le temps passé sur chacune (le relevé ou une estimation)
3. **La stack technologique** (CRM, outils de prospection, conversation intelligence, tableurs…)
4. **L'usage aval** de chaque activité : qui lit ? quelle décision en dépend ?

Si l'utilisateur dit « lance-toi » sans données, procéder en mode questions : l'inventaire se
construit à l'oral, activité par activité.

---

## Étape 1 — Inventaire du train de bagages (manœuvre 1 de l'article)

> « Aucune direction commerciale ne connaît réellement la répartition du temps de ses équipes.
> Les estimations en comité oscillent entre le déni et l'approximation. » — Commencez par mesurer.

### 1a. Relevé (si fourni)

Pour chaque ligne du relevé (`references/RELEVE.md` ou le tableur `references/releve-activite-2-semaines.xlsx`
fourni dans le paquet), extraire : **activité, fréquence, temps hebdo par commercial, outil
utilisé**. Ne pas interpréter : reporter les chiffres tels quels.

### 1b. Questions d'inventaire (si pas de relevé)

Parcourir systématiquement les cinq familles d'obligations administratives :

1. **Saisie CRM** : mise à jour des champs d'opportunité, comptes rendus d'appels, d'e-mails, de réunions
2. **Reporting** : rapports hebdo/mensuel, prévisions, tableaux de bord alimentés à la main
3. **Réunions internes** : rituels d'équipe, comités, revues de pipeline
4. **Outils & fragmentation** : recopies entre outils, exports/imports, tableurs parallèles
5. **Administratif résiduel** : devis, contrats, notes de frais, tâches de gestion

Pour **chaque activité identifiée**, poser la triple question de l'usage aval :
- **Qui lit cette donnée ?** (nommer une personne ou un comité, pas « la direction »)
- **Quelle décision en dépend ?** (si aucune décision identifiable : signal de chariot)
- **Que se passe-t-il si personne ne la remplit pendant un mois ?** (si « rien » : chariot)

Estimer avec l'utilisateur le **temps hebdo par commercial** pour chaque activité. En cas
d'incertitude, prendre une fourchette basse et le signaler.

### 1c. Cartographier la stack (prérequis de la manœuvre 2)

Lister les outils en usage : CRM de référence, outils de prospection, conversation intelligence
(déployé ou non), plateformes e-mail, tableurs, outils de reporting. Noter ce qui est **connecté**
(échanges automatiques entre outils) et ce qui est **fragmenté** (recopies manuelles). Un outil
déconnecté est un candidat chariot : 62 % des équipes déclarent que des outils déconnectés leur
font manquer des opportunités (Pipedrive, CRM Trends Report 2026).

---

## Étape 2 — Classement et diagnostic

### 2a. Classer chaque activité en trois colonnes

| Colonne | Définition | Test |
|---|---|---|
| **Charge utile** | Sert un deal en cours ou une passation | « Cette donnée aide à avancer une signature cette semaine ? » |
| **Charge de commandement** | Sert une décision de pilotage **identifiée** | « Un comité ou un manager nommable la lit et décide ? » |
| **Chariot** | Ne sert personne d'identifiable | « Aucun lecteur nommable, aucune décision dépendante » |

La saisie qui alimente un tableau de bord mort est un convoi de mulets ; la donnée qui sert le
deal est le paquetage du légionnaire. Confondre les deux catégories, c'est soit tout supprimer et
perdre la mémoire commerciale, soit tout garder et immobiliser la colonne.

### 2b. Calculer le diagnostic

- **Temps perdu** : somme des heures hebdo classées « chariot » × effectif commercial → heures
  par semaine, puis équivalent ETP (÷ 35 h) et coût annuel (× 45 semaines × coût chargé médian
  du profil, si le coût est fourni, sinon rester en heures/ETP).
- **Chariots priorisés** : ordonner par (temps hebdo par commercial × fréquence × nombre de
  personnes concernées). Les 2-3 premiers concentrent l'essentiel du gain.
- **Causes racines** à repérer : champs obligatoires excessifs, rituels de reporting hérités,
  outils déconnectés, absence d'arbitrage. Signaler toute saisie « qui n'existe que parce que
  l'outil la demande ».

---

## Étape 3 — Plan d'automatisation (manœuvre 2 de l'article)

> « Pour chaque donnée que vous exigez d'un commercial, posez la question du capteur avant celle
> du formulaire. Ce que la machine porte, l'homme ne le porte pas. »

### 3a. La question du capteur avant le formulaire

Pour chaque activité classée « chariot » ou « charge de commandement à forte saisie », appliquer
la cascade dans l'ordre :

1. **Supprimer** (si aucune décision aval identifiée) — gratuit, immédiat
2. **Capturer automatiquement** : la donnée d'activité (appels, e-mails, réunions, participants,
   prochaines étapes) n'a plus aucune raison d'être frappée au clavier par un être humain payé
   pour vendre
3. **Assister la saisie** : ramener la mise à jour dans l'espace de travail du commercial
4. **Agentiser** : un agent connecté à l'écosystème analyse les sources brutes et logge dans le CRM

### 3b. Associer chaque charge à une catégorie de capteur

Rester au niveau des **catégories d'outils** (jamais de prescription produit) :

| Charge détectée | Catégorie de capteur | Gain typique | Prérequis |
|---|---|---|---|
| Logging d'e-mails / réunions / appels | **Capture d'activité** (synchronisation automatique des échanges vers le CRM) | 2-4 h/semaine/commercial | CRM avec connecteur, règles de confidentialité |
| Transcription, résumé, prochaines étapes | **Conversation intelligence** (enregistrement + analyse des appels/réunions) | 1-3 h/semaine + qualité des CR | Adoption par les commerciaux, conformité RGPD |
| Mise à jour du pipeline pendant la journée | **Saisie assistée** (interface dans l'espace de travail quotidien) | 1-2 h/semaine | Compatibilité avec le CRM |
| Saisies répétitives transverses (CR → CRM → reporting) | **Intégrations natives / API** entre les outils | 1-3 h/semaine | Map des flux de données, autorité RevOps |
| Traitement de sources brutes variées (enregistrements, e-mails, CR) | **Agentique** (agents qui transforment et loggent) | 2-4 h/semaine | Gouvernance, arbitrage des passerelles |

Pour chaque recommandation retenue : **gain estimé** (h/semaine × commerciaux concernés), **coût
d'entrée** (faible/moyen/élevé), **prérequis**, **risque**. Signaler explicitement le garde-fou de
l'article : l'agent ne dispense pas de l'arbitrage — chaque passerelle ajoute de la complexité, et
c'est au commandement de décider lesquelles valent le coup, au risque de créer une usine à gaz
agentique contre-productive. Ne recommander une catégorie que si la charge qu'elle capture est
réellement présente et mesurée à l'étape 2.

### 3c. Arbitrage final

Présenter les recommandations en deux listes :
- **Coupes immédiates** (chariots purs) : à supprimer dans le trimestre, sans négociation
- **Capteurs à déployer** : par gain décroissant, avec le responsable et l'échéance

---

## Étape 4 — Plan de réforme

Traduire les décisions en plan 30-60-90 jours :

| Horizon | Actions types |
|---|---|
| **30 jours** | Supprimer les chariots purs, alléger les champs obligatoires (réglage administrateur d'une demi-journée sur la plupart des CRM), désigner le responsable du plan |
| **60 jours** | Déployer le premier capteur (catégorie au meilleur ratio gain/risque), mesurer le temps réellement récupéré |
| **90 jours** | Étendre aux charges de commandement, unifier les outils restants, mesurer la part du temps commercial en interaction client |

Définir **l'indicateur unique** : la part du temps commercial passée en interaction client, mesurée
trimestre après trimestre. Mentionner (sans la traiter) la perspective RevOps : un responsable
unique avec droit de veto sur tout nouvel outil sans intégration native avec le CRM de référence.

---

## Étape 5 — Sortie

### 5a. Format par défaut : Markdown

Rédiger le rapport « Inventaire du train de bagages » selon `references/TEMPLATE.md` :
`inventaire-train-bagages-[Organisation]-[DateJour].md`, sauvegardé dans `output_dir` déclaré
dans `TOOLS.md` (défaut : dossier courant).

### 5b. Format JSON (si spécifié dans TOOLS.md)

Produire `inventaire-train-bagages-[Organisation]-[DateJour].json` avec la structure :

```json
{
  "organisation": "...", "date": "...",
  "inventaire": [
    { "activite": "...", "frequence": "...", "heures_semaine_par_commercial": 0,
      "lecteur": "...", "decision": "...", "colonne": "charge_utile|charge_commandement|chariot" }
  ],
  "diagnostic": { "heures_perdues_semaine": 0, "etp_gaspilles": 0,
                  "chariots_priorises": ["..."] },
  "automatisations": [
    { "charge_cible": "...", "categorie_capteur": "...", "gain_estime_h_semaine": 0,
      "cout_entree": "faible|moyen|eleve", "prerequis": "...", "risque": "..." }
  ],
  "plan_reforme": { "j30": ["..."], "j60": ["..."], "j90": ["..."],
                    "indicateur": "part du temps en interaction client" }
}
```

Ce format permet de brancher l'audit sur des workflows automatisés (n8n, Make, scripts).

### 5c. Contrôle qualité avant livraison

- [ ] Chaque activité du relevé/des questions a une ligne dans l'inventaire
- [ ] Chaque ligne a une colonne et une justification d'une ligne
- [ ] Le diagnostic donne des chiffres (heures/semaine, ETP) pas des impressions
- [ ] Chaque chariot priorisé a une action (coupe immédiate ou capteur) avec gain estimé
- [ ] Le garde-fou anti usine à gaz figure dans les recommandations agentiques
- [ ] Le plan 30-60-90 a un responsable et un indicateur
- [ ] Langue conforme à `TOOLS.md` (français par défaut), pas de produit prescrit en dur

---

*Skill « Mules de Marius » — strategiecommerciale.eu. Doctrines : réforme de Marius (107 av.
J.-C.), Frontin (Stratagèmes IV), article « Vos commerciaux sont des gratte-papiers » (2026).*
