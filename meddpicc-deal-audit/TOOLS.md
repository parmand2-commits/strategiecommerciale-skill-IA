# TOOLS.md — Manifeste d'outillage MEDDPICC

Ce fichier déclare les outils disponibles pour enrichir l'audit MEDDPICC.
**Modifiez ce fichier** pour activer vos propres connexions MCP ou ajuster les préférences de sortie.
L'agent lira ce fichier en premier à chaque exécution.

---

## Configuration générale

```yaml
language: fr                    # fr | en
output_format: markdown         # markdown | json | document (.docx)
output_dir: ./audits            # dossier de sortie (défaut : dossier courant)
analysis_depth: standard        # standard | deep (deep = recherches supplémentaires, 10 min+)
freshness_cutoff_months: 12     # rejeter toute source web de plus de N mois
anonymize: false                # true = masquer noms de comptes/contacts dans le livrable
```

---

## Outils activés

### web_search (activé par défaut)

Recherche web générale. Utilisé pour corroborer les informations du commercial avec des sources
publiques : rapports annuels, interviews de dirigeants, communiqués de presse, offres d'emploi,
couverture analystes.

Paramètres :
- Priorité aux sources primaires (site IR de l'entreprise, Reuters, Bloomberg, FT, Les Échos)
- Rejeter tout résultat sans date visible
- Minimum 5 recherches avant de rédiger

```yaml
tool: web_search
enabled: true
priority: 1
```

---

## Outils optionnels — Décommentez et configurez selon votre stack

### CRM (exemple : Salesforce, HubSpot, Dynamics)

Récupère la fiche compte, l'historique d'activité, les opportunités liées, les contacts enregistrés.
Utile pour pré-remplir les dimensions Economic Buyer, Champion, Decision Process.

```yaml
# tool: crm
# enabled: false
# mcp_server_url: https://votre-instance.mcp-crm.example.com
# description: >
#   Accès en lecture à Salesforce. Permet de récupérer la fiche compte (Account),
#   les contacts associés (Contacts), l'historique d'activité (Activity History),
#   et les données d'opportunité (Opportunity). Requêtes SOQL acceptées.
# data_available:
#   - fiche_compte
#   - contacts_et_roles
#   - historique_activites
#   - opportunites_liees
#   - notes_commerciales
```

### Conversation Intelligence (exemple : Gong, Chorus, Modjo)

Récupère les transcriptions et résumés des appels récents. Utile pour extraire les signaux
de douleur (Identify Pain), les objections sur les Decision Criteria, et les prises de parole
de l'Economic Buyer.

```yaml
# tool: conversation_intelligence
# enabled: false
# mcp_server_url: https://votre-instance.mcp-gong.example.com
# description: >
#   Accès en lecture à Gong. Permet de récupérer les transcriptions des 10 derniers appels
#   sur le compte, les résumés automatiques, les next steps identifiés et les moments clés.
# data_available:
#   - transcriptions_appels
#   - resumes_appels
#   - mentions_concurrents
#   - objections_identifiees
#   - next_steps_enregistres
```

### Email & Agenda (exemple : Gmail, Outlook via MCP)

Récupère les derniers échanges avec le prospect. Utile pour valider le Decision Process
(quels interlocuteurs impliqués, rythme des échanges) et le Paper Process (mentions légales,
procurement, sécurité).

```yaml
# tool: email_calendar
# enabled: false
# mcp_server_url: https://votre-instance.mcp-email.example.com
# description: >
#   Accès en lecture aux emails et événements agenda liés au domaine du prospect.
#   Permet d'identifier les participants aux réunions, la fréquence des échanges,
#   les mentions de budget, timeline, ou processus juridique.
# data_available:
#   - derniers_emails_prospect
#   - reunions_passees_futures
#   - participants_identifies
```

### Sales Enablement (exemple : Highspot)

Récupère les contenus partagés avec le prospect et les signaux d'engagement.
Utile pour mesurer l'implication du Champion (a-t-il partagé le contenu en interne ?)
et la maturité des Decision Criteria (a-t-il demandé des études de cas spécifiques ?).

```yaml
# tool: sales_enablement
# enabled: false
# mcp_server_url: https://mcp.highspot.com/mcp
# description: >
#   Accès en lecture à Highspot. Permet de récupérer les contenus partagés avec le prospect,
#   les vues et partages internes (signal d'engagement du Champion), et les pitches envoyés.
# data_available:
#   - contenus_partages
#   - engagements_prospect
#   - pitches_envoyes
```

---

## Ajouter un outil personnalisé

Pour déclarer un nouvel outil MCP, copier ce bloc et le remplir :

```yaml
# tool: nom_de_votre_outil
# enabled: false
# mcp_server_url: https://url-de-votre-serveur-mcp
# description: >
#   Description de ce que cet outil permet de récupérer.
#   L'agent utilisera cette description pour décider quand l'appeler.
# data_available:
#   - type_de_donnee_1
#   - type_de_donnee_2
```

---

## Notes d'usage

- Décommenter un bloc `tool` ne suffit pas à activer un MCP : le serveur MCP doit être
  correctement configuré dans votre environnement d'agent (Claude Code, Cursor, n8n, etc.
  selon votre configuration).
- Plusieurs outils peuvent être activés simultanément. L'agent décidera lequel interroger
  selon la dimension en cours d'analyse.
- En l'absence de tout outil MCP actif, l'agent fonctionne en mode `web_search` uniquement.
  L'audit reste complet mais s'appuie uniquement sur les sources publiques.
- **Confidentialité** : un audit contient des données prospect sensibles. Ne pas persister
  d'informations identifiantes (noms de comptes, contacts) hors du livrable demandé,
  et activer `anonymize: true` si le livrable doit circuler en interne élargi.
