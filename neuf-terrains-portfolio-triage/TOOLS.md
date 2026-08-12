# TOOLS.md — Manifeste d'outillage « Neuf Terrains »

Déclare le **profil de votre organisation** et les **outils connectés** pour le tri du
portefeuille. L'agent le lit en premier à chaque exécution. **À configurer une fois.**

---

## Configuration générale

```yaml
language: fr                    # fr | en
output_format: markdown         # markdown | json
output_dir: ./triage            # dossier de sortie
analysis_depth: standard        # standard | deep
```

---

## Profil de l'organisation (obligatoire)

```yaml
organisation:
  nom: "Votre entreprise"
  taille: "PME"                 # TPE | PME | ETI | Grand compte
  secteur: "SaaS B2B"
  offre:
    - "Produit principal"
  typologie_clients: "ETI et grands comptes"
  cycle_vente: "3-6 mois"
  positionnement_prix: "premium"
  concurrents_principaux:
    - "Concurrent A"
    - "Concurrent B"
  seuil_deal_min: 20000         # en € — en dessous, terrain "dispersé" par défaut
  criteres_abandon:             # signaux pour recommander le décrochage
    - "aucun contact depuis 60+ jours"
    - "aucun champion identifié"
    - "budget non confirmé après 2 relances"
```

> Le profil permet de calibrer : seuil de valeur, critères d'abandon, poids des concurrents
> dans le classement. Sans profil, la skill reste générique.

---

## Outils connectés (optionnels)

### CRM (Salesforce, HubSpot, Dynamics, Pipedrive…)

```yaml
# tool: crm
# enabled: false
# type: api | mcp
# api_instructions: >
#   Comment extraire le portefeuille : ex : GET /opportunities?owner_id=me&stage=open
#   → [ { name, amount, stage, last_activity_date, champion } ]
# data_available:
#   - opportunites_ouvertes
#   - montants
#   - dernier_contact
```

### Autres outils (conversation intelligence pour détecter champions, email…)

Même format de bloc : `type`, `api_instructions`, `data_available`. L'agent utilise
l'outil si les instructions sont opérationnelles.

---

## Notes d'usage

- **Mode dégradé gracieux** : sans CRM connecté, trier sur les données fournies (copier-coller,
  CSV, notes). Le tri reste valide, moins riche.
- **Scalabilité** : le même dossier sert toute l'équipe — seul `TOOLS.md` change (profil,
  seuils, connecteurs).
- **Confidentialité** : ne pas persister les montants/noms hors du livrable ; `anonymize: true`
  si le tri doit circuler en interne élargi.
