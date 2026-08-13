# TOOLS.md — Manifeste d'outillage « Logistique de Bradley »

Déclare le **profil de votre organisation** et les **outils connectés** pour l'audit
d'enablement. L'agent le lit en premier. **À configurer une fois.**

---

## Configuration générale

```yaml
language: fr                    # fr | en
output_format: markdown         # markdown | json
output_dir: ./audits-enablement # dossier de sortie
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
  effectif_commercial: 25       # nb de commerciaux (SDR + AE + AM)
  roles:
    - "SDR"
    - "AE"
    - "AM"
  cycle_vente: "3-6 mois"
  revenu_moyen_deal: 25000      # € — pour estimer le coût des gaps
  metriques_connues:            # si connues (sinon, hypothèses)
    win_rate: 0.22
    quota_attainment: 0.65
    duree_cycle_mois: 4
```

> Le profil permet de chiffrer les impacts (coût d'un onboarding long × revenu moyen,
> win rate × revenu moyen par deal). Sans profil, l'audit reste qualitatif.

---

## Outils connectés (optionnels)

### Sales Enablement Platform (Highspot, Seismic, Showpad…)

```yaml
# tool: enablement_platform
# enabled: false
# type: api | mcp
# api_instructions: >
#   Comment récupérer : contenus publiés (titre, date, type), taux d'usage par contenu,
#   recherche des commerciaux (requêtes, échecs), playbooks existants.
# data_available:
#   - contenus_publies
#   - usage_contenus
#   - recherches_commerciaux
#   - playbooks
```

### CRM (Salesforce, HubSpot…)

```yaml
# tool: crm
# enabled: false
# type: api | mcp
# api_instructions: >
#   Comment récupérer : win rate par étape, durée moyenne du cycle, quota attainment,
#   activités par commercial.
# data_available:
#   - metriques_vente
#   - etapes_cycle
```

### Conversation Intelligence (Gong, Modjo…)

```yaml
# tool: conversation_intelligence
# enabled: false
# type: api | mcp
# api_instructions: >
#   Comment récupérer les appels récents : objections récurrentes, questions que les
#   commerciaux ne savent pas traiter (signaux de playbooks manquants).
# data_available:
#   - objections_recurrentes
#   - questions_sans_reponse
```

---

## Notes d'usage

- **Mode dégradé gracieux** : sans outil connecté, l'audit se fait sur les réponses au
  questionnaire — qualitatif mais complet.
- **Scalabilité** : un dossier pour toute l'organisation ; TOOLS.md par équipe (effectif,
  métriques, connecteurs).
- **Confidentialité** : les métriques commerciales sont sensibles — `anonymize: true` si le
  rapport circule en interne élargi.
