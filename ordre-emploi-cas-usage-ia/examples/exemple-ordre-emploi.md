# ORDRE D'EMPLOI DES CAS D'USAGE IA : Exemple complet

> **Exemple golden file** : sortie de référence de la skill « Ordre d'Emploi » sur le scénario de
> test fixture-07 (ETI SaaS B2B, 24 commerciaux, trois licences d'IA en cours). Cet exemple
> illustre la structure attendue : registre des ordres d'emploi, tableau de mesure à cinq
> colonnes, mandat de l'état-major permanent. Les données sont fictives.

---

## REGISTRE DES ORDRES D'EMPLOI

**Fonction :** Direction commerciale de VentisPro (fictif)
**Date :** 05/10/2026
**Titulaire RevOps :** responsable des opérations commerciales (nommé le 15/09/2026)
**Processus cadrés :** 3
**Licences concernées :** 3

---

## 1. ORDRES D'EMPLOI

### Ordre d'emploi : préparer la note de contexte d'un rendez-vous

| Champ | Contenu |
|---|---|
| **Tâche confiée** | Préparer la note de contexte avant un rendez-vous client, à partir des échanges et des données de compte |
| **Rôle qui la porte** | Le commercial qui tient le rendez-vous |
| **Sortie attendue** | Une note d'une page, disponible la veille du rendez-vous |
| **Contrôle qui la valide** | Le manager d'équipe vérifie la note la veille, sur les sources citées ; le compte rendu du rendez-vous est déposé dans les 24 heures |
| **Propriétaire du résultat** | Directeur commercial, pour ce processus |

### Ordre d'emploi : rédiger le compte rendu d'un appel

| Champ | Contenu |
|---|---|
| **Tâche confiée** | Rédiger le compte rendu d'un appel à partir de la transcription et des notes du commercial |
| **Rôle qui la porte** | Le commercial qui a tenu l'appel |
| **Sortie attendue** | Un compte rendu structuré (décisions, objections, prochaines étapes), disponible dans les 24 heures |
| **Contrôle qui la valide** | Le commercial relit et valide avant dépôt ; le manager contrôle l'exhaustivité des prochaines étapes en revue hebdomadaire |
| **Propriétaire du résultat** | Directeur commercial, pour ce processus |

### Ordre d'emploi : rédiger un e-mail de relance

| Champ | Contenu |
|---|---|
| **Tâche confiée** | Rédiger un e-mail de relance après une proposition restée sans réponse |
| **Rôle qui la porte** | (à nommer) |
| **Sortie attendue** | Un e-mail de relance, envoyé sous cinq jours ouvrés |
| **Contrôle qui la valide** | (à définir) |
| **Propriétaire du résultat** | Directeur commercial, pour ce processus |

> Règle de coupe appliquée en amont : le troisième ordre d'emploi n'a **aucun rôle consommateur
> nommé**. Il n'autorise pas la mise en service de l'outil et passe au tableau de mesure comme
> candidat à la résiliation.

---

## 2. TABLEAU DE MESURE PAR RÔLE

**Sources du tableau :** matière conversationnelle (usage réel), tableaux de bord du CRM
(fréquence), revue de pipeline (résultat).

| Rôle | Tâche | Output | Usage (par semaine) | Décision du trimestre |
|---|---|---|---|---|
| Commercial qui tient le rendez-vous | Préparer la note de contexte d'un rendez-vous | 18 notes par semaine, consommées par le commercial et le manager d'équipe | 18 | **Reconduite** (sortie consommée, décision de préparation prise la veille) |
| Commercial qui a tenu l'appel | Rédiger le compte rendu d'un appel | 26 comptes rendus par semaine, consommés par le commercial et la revue de pipeline | 26 | **Reconduite** (sortie consommée, prochaines étapes validées en revue) |
| (aucun rôle nommé) | Rédiger un e-mail de relance | 5 e-mails par semaine, non repris dans le pipeline | 5 | **Coupée** (aucun rôle nommé ne consomme la sortie) |
| Manager d'équipe | Synthèse des objections de la semaine | 1 synthèse par semaine, consommée par l'état-major commercial | 1 | **Réaffectée** à la préparation des points de formation (ordre d'emploi réécrit le 02/10/2026) |

> Lecture du tableau : les deux premières lignes décrivent une adoption utile, la troisième
> décrit une subvention versée à un éditeur. Le verdict est tombé au trimestre suivant la mise
> en service, avant l'échéance du contrat.

---

## 3. MANDAT DE L'ÉTAT-MAJOR PERMANENT

| Élément | Valeur |
|---|---|
| **Composition** | Responsable RevOps (nommé le 15/09/2026) et responsable sales enablement |
| **Cadence** | Une heure par semaine, le mardi à 9 h |
| **Point 1 : ce que la mesure a montré** | 18 notes de contexte et 26 comptes rendus par semaine ; 5 relances sans consommateur |
| **Point 2 : la décision unique** | Résilier la licence de relance ; réaffecter la synthèse d'objections à la préparation de formation |
| **Point 3 : ce qui change pour le terrain** | Ordre d'emploi « note de contexte » mis à jour ; module de formation « préparation de rendez-vous » aligné le 02/10/2026 |

**Test de fin de trimestre :**
- Processus avec un ordre d'emploi à jour : 2 sur 3
- Licences avec un rôle nommé qui consomme leur sortie : 1 sur 3

> Coût du dispositif : deux heures d'encadrement par semaine et une page par processus. Le
> troisième processus, dépourvu de rôle consommateur, sort du dispositif par la coupe.

---

## 4. VALEURS DE RÉFÉRENCE

| Donnée | Valeur | Source | Date |
|---|---|---|---|
| Entreprises qui utilisent l'IA | 90 % | Enquête HubSpot relayée par Forbes (John Koetsier) | 16 septembre 2026 |
| Entreprises à résultats transformateurs | 6 % | Enquête HubSpot relayée par Forbes (John Koetsier) | 16 septembre 2026 |
| Passage à l'échelle sur plusieurs business units | 22 % | Gartner (1 303 responsables interrogés) | 1er septembre 2026 |
| Responsables ignorant la dépense IA de leur fonction en 2025 | 11 % | Gartner (même enquête) | 1er septembre 2026 |
| Initiatives à retour positif là où le retour est suivi | 81 % | Gartner (même enquête) | 1er septembre 2026 |
| Initiatives dont le taux de retour est ignoré chez ceux qui suivent de loin | 29 % | Gartner (même enquête) | 1er septembre 2026 |

> Périmètre : ces chiffres sont des mesures d'enquête, pas des prévisions ; ils sont cités avec
> l'échantillon déclaré par chaque source, sans généralisation au-delà.

---

*Ordre d'emploi généré par la skill « Ordre d'Emploi » de la collection strategiecommerciale.eu.
Un ordre d'emploi sans rôle consommateur nommé n'autorise pas la mise en service de l'outil.*
