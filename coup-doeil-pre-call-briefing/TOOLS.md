# TOOLS.md — Manifeste d'outillage « Coup d'Œil »

Ce fichier déclare le **profil de votre organisation** et les **outils connectés** disponibles
pour enrichir le briefing. L'agent le lit en premier à chaque exécution.
**Modifiez-le une fois pour votre organisation** — il s'applique ensuite à tous les briefings.

---

## Configuration générale

```yaml
language: fr                    # fr | en
output_format: markdown         # markdown | json
output_dir: ./briefings         # dossier de sortie (défaut : dossier courant)
analysis_depth: standard        # standard | deep (deep = +3 recherches, 10 min+)
freshness_cutoff_months: 12     # rejeter toute source web de plus de N mois
```

---

## Profil de l'organisation (obligatoire — c'est ce qui rend la skill adaptée à VOTRE contexte)

```yaml
organisation:
  nom: "Votre entreprise"
  taille: "PME"                 # TPE | PME | ETI | Grand compte
  secteur: "SaaS B2B"           # ex : SaaS B2B, services financiers, industrie, santé…
  offre:
    - "Votre produit/service principal"
    - "Votre produit secondaire"
  typologie_clients: "ETI et grands comptes"   # qui vous achetez
  cycle_vente: "3-6 mois"       # court (<3 mois) | moyen (3-9) | long (>9)
  positionnement_prix: "premium"  # low-cost | milieu de gamme | premium
  concurrents_principaux:
    - "Concurrent A"
    - "Concurrent B"
  langue_clients: "fr"          # langue des comptes prospectés (pour les recherches)
```

> **Pourquoi c'est important** : les angles d'attaque, les objections probables et les
> questions sont calibrés sur CE profil. Une TPE qui vend aux PME n'aura pas les mêmes
> angles qu'un grand compte qui vend aux banques. Sans profil, la skill fonctionne en
> mode « générique » — moins efficace.

---

## Outils connectés (optionnels — décommentez et configurez selon votre stack)

### CRM (exemple : Salesforce, HubSpot, Dynamics, Pipedrive)

Récupère la fiche compte, les contacts, les opportunités ouvertes et l'historique d'activité.
Utile pour pré-remplir la Situation et les Participants.

```yaml
# tool: crm
# enabled: false
# type: api                 # api | mcp
# mcp_server_url: https://votre-instance.mcp-crm.example.com
# api_instructions: >
#   Comment interroger votre CRM (endpoint, requête, champs) :
#   ex : GET /accounts?name=X → fiche compte ; GET /opportunities?account_id=Y → deals ouverts.
# data_available:
#   - fiche_compte
#   - contacts_et_roles
#   - opportunites_ouvertes
#   - historique_activites
```

### Conversation Intelligence (exemple : Gong, Modjo, Chorus)

Récupère les transcriptions/résumés des derniers appels sur le compte.

```yaml
# tool: conversation_intelligence
# enabled: false
# type: api
# api_instructions: >
#   Comment récupérer les appels récents d'un compte (endpoint, période).
# data_available:
#   - appels_recents
#   - objections_entendues
#   - next_steps
```

### Email & Agenda (exemple : Gmail, Outlook)

Récupère les derniers échanges et les participants aux réunions.

```yaml
# tool: email_calendar
# enabled: false
# type: api
# api_instructions: >
#   Comment lister les derniers emails/réunions liés au domaine du prospect.
# data_available:
#   - derniers_echanges
#   - participants_reunions
```

### Webhook / API métier (cas particulier)

N'importe quel outil interne peut être déclaré de la même façon (type, instructions,
données disponibles). L'agent l'utilisera si les instructions sont suffisamment claires.

```yaml
# tool: nom_de_votre_outil
# enabled: false
# type: api
# api_instructions: >
#   Endpoint, authentification, requête type, champs retournés.
# data_available:
#   - donnee_1
#   - donnee_2
```

---

## Notes d'usage

- Décommenter un bloc `tool` ne suffit pas : le connecteur doit être réellement accessible
  dans votre environnement d'agent (MCP configuré, ou instructions d'API opérationnelles).
- **Mode dégradé gracieux** : sans aucun outil connecté, la skill fonctionne avec
  `web_search` seul — briefing plus générique mais complet.
- **Scalabilité** : un même dossier de skill sert toute l'organisation. Seul `TOOLS.md`
  change d'une équipe à l'autre (profil + connecteurs).
- **Confidentialité** : ne pas persister de données identifiantes hors du livrable demandé ;
  activer `anonymize: true` si le briefing doit circuler en interne élargi.
