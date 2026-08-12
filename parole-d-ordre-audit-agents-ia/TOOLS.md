# TOOLS.md — Manifeste d'outillage « Parole d'Ordre »

Déclare le **profil de votre organisation** (taille, secteur, réglementation) et les outils
connectés pour l'audit des agents IA. L'agent le lit en premier. **À configurer une fois.**

---

## Configuration générale

```yaml
language: fr                    # fr | en
output_format: markdown         # markdown | json
output_dir: ./audits-ia         # dossier de sortie
```

---

## Profil de l'organisation (obligatoire)

```yaml
organisation:
  nom: "Votre entreprise"
  taille: "PME"                 # TPE | PME | ETI | Grand compte
  secteur: "SaaS B2B"
  secteur_regule: false         # true si banque, assurance, santé, défense…
  dpo_dedie: false              # true si un DPO est en poste
  reglementations:
    - "RGPD"                    # RGPD, SOC2, ISO 27001, HIPAA, DORA…
  politiques_ia:
    - "charte IA interne"
    - "processus de validation des outils IA"
```

> Le profil règle la sévérité de l'audit : un secteur régulé avec DPO impose un registre
> exhaustif et des délais d'action stricts. Sans profil, la skill reste générique.

---

## Outils connectés (optionnels)

### Gouvernance / inventaire d'agents (si l'outil existe)

```yaml
# tool: registre_agents
# enabled: false
# type: api | mcp
# api_instructions: >
#   Comment lister les agents enregistrés : endpoint, champs (nom, propriétaire, accès, statut).
# data_available:
#   - liste_agents
#   - proprietaires
#   - acces_declares
```

### SSO / Identity Provider (Okta, Entra ID, Google Workspace…)

```yaml
# tool: sso
# enabled: false
# type: api
# api_instructions: >
#   Comment lister les applications/agents connectés au SSO et leurs owners.
# data_available:
#   - applications_connectees
#   - acces_utilisateurs
```

### Autres outils

Même format de bloc (`type`, `api_instructions`, `data_available`). L'agent utilise l'outil
si les instructions sont opérationnelles — sinon il pose les questions d'inventaire.

---

## Notes d'usage

- **Mode dégradé gracieux** : sans outil connecté, l'audit se fait par questions et analyse
  des réponses — il reste complet, moins automatisé.
- **Scalabilité** : un dossier pour toute l'organisation ; `TOOLS.md` change par entité
  (taille, secteur régulé, politique).
- **Confidentialité** : l'audit révèle des accès sensibles — `anonymize: true` si le rapport
  circule, ne jamais persister les secrets d'accès.
