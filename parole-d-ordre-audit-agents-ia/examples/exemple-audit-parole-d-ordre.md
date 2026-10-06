# AUDIT DE LA PAROLE D'ORDRE : Groupe Lartigue Distribution (fictif)

> **Exemple golden file** : sortie de référence de la skill « Parole d'Ordre » sur un cas
> entièrement fictif. Organisation, personnes, agents, chiffres et sources sont inventés ; les
> sources citées sont fictives et datées de moins de douze mois. L'exemple illustre la structure
> attendue, de l'inventaire au registre final.

---

## AUDIT DE LA PAROLE D'ORDRE

**Organisation :** Groupe Lartigue Distribution (fictif) · **Date :** 06/10/2026 · **Secteur régulé :** Non
**Agents audités :** 10 déclarés + 2 agents fantômes
**Propriétaire de l'audit :** Nadia Berthomieu, directrice des systèmes d'information
**Périmètre :** France, exercice 2026

---

## 1. INVENTAIRE DES AGENTS

| Agent | Usage | Accès | Propriétaire | Risque |
|---|---|---|---|---|
| Qualifieur leads | Qualifier les leads entrants du mid-market | CRM (lecture), scoring | A. Mercier (RevOps) | Moyen |
| Transcripteur d'appels | Rédiger les comptes rendus d'appels | Enregistrements, CRM (écriture) | A. Mercier (RevOps) | **Critique** |
| Veille concurrentielle | Résumer pages et communiqués concurrents | Web public (lecture) | L. Vidal (marketing) | Faible |
| Enrichisseur de contacts | Compléter les fiches contacts | Web public, CRM (écriture) | L. Vidal (marketing) | Moyen |
| Scoreur d'opportunités | Noter les opportunités selon le scoring validé | CRM (lecture/écriture) | A. Mercier (RevOps) | Moyen |
| Support client niveau 1 | Répondre aux questions de commande | Base commandes, FAQ | S. Nguyen (service client) | Moyen |
| Générateur de devis | Préparer un devis depuis le catalogue | CRM, catalogue tarifaire | P. Rousset (ADV) | **Critique** |
| Séquenceur d'e-mails | Envoyer des séquences de prospection | Messagerie, liste de contacts | N. Faure (SDR) | **Critique** |
| Synthèse de comptes | Produire une note de préparation d'appel | Web public, CRM (lecture) | N. Faure (SDR) | Faible |
| Nettoyeur de données | Dédoublonner et normaliser la base clients | CRM (écriture interne) | A. Mercier (RevOps) | Moyen |

> Trois agents sont critiques : ils disposent d'un accès en écriture ou d'un canal d'envoi vers
> l'extérieur (transcripteur, générateur de devis, séquenceur).

## 2. ANGLES MORTS IDENTIFIÉS

- **Agent tarifaire hérité** : agent de calcul de remise créé par un prestataire sorti en 2024,
  toujours actif sur une clé API partagée. Statut « à vérifier ». Risque critique par défaut.
- **Extension « résumé d'articles »** : extension de navigateur installée par le marketing,
  connectée à la fiche contact du CRM. Statut « à vérifier » (shadow IT).
- **Questions pour les détecter :** Qui connaît la liste des clés API actives et leur
  propriétaire ? Quels agents écrivent encore dans le CRM ? Quelles extensions de navigateur
  sont installées sur les postes commerciaux ? Un PoC a-t-il été laissé en production ?

## 3. AUDIT PAR AGENT (parole d'ordre)

| Agent | Qui le déclenche ? | Données visibles | Responsable | Statut |
|---|---|---|---|---|
| Qualifieur leads | Toute l'équipe commerciale | Données de contact | A. Mercier | À renforcer |
| Transcripteur d'appels | Tous les SDR | Enregistrements d'appels | A. Mercier | **Critique** |
| Veille concurrentielle | Équipe marketing | Web public | L. Vidal | OK |
| Enrichisseur de contacts | Équipe marketing | Contacts, CRM | L. Vidal | À renforcer |
| Scoreur d'opportunités | Équipe commerciale | CRM | A. Mercier | OK |
| Support client niveau 1 | Clients (accès ouvert) | Commandes, FAQ | S. Nguyen | À renforcer |
| Générateur de devis | ADV | Catalogue, CRM | P. Rousset | **Critique** |
| Séquenceur d'e-mails | SDR | Contacts, messagerie | N. Faure | **Critique** |
| Synthèse de comptes | SDR | Web public, CRM | N. Faure | OK |
| Nettoyeur de données | RevOps (planifié) | Base clients | A. Mercier | OK |
| Agent tarifaire (fantôme) | Inconnu | Tarifs, remises | Non identifié | **Critique** |
| Extension résumé (fantôme) | Équipe marketing | Pages web, contacts | Non identifié | **Critique** |

## 4. LA RÈGLE DES DEUX (actions irréversibles)

| Action irréversible | Agent | Seconde clé (validateur) | Indépendant ? | Trace |
|---|---|---|---|---|
| Envoi d'un e-mail client | Séquenceur d'e-mails | Humain (SDR senior) | Oui (jeton, prompt, objectif distincts) | Journal d'envoi |
| Émission d'un devis | Générateur de devis | Humain (ADV) | Oui | Historique devis |
| Calcul et application d'une remise | Agent tarifaire (fantôme) | Aucune | **Non** | Aucune |
| Écriture d'un compte rendu client | Transcripteur d'appels | Agent vérificateur | **Non** (même prompt) | Journal CRM |

> Le transcripteur écrit dans un enregistrement client partagé, et l'agent vérificateur reprend
> le même prompt : la seconde clé n'est pas indépendante. À corriger.

## 5. SURVEILLANCE DU RAISONNEMENT ET AUTONOMIE

### 5a. Alertes de raisonnement

| Agent | Outil hors périmètre | Reprise en boucle | Écriture imprévue (ressource partagée) |
|---|---|---|---|
| Transcripteur d'appels | Non détecté | Non détecté | Oui : notes partagées d'équipe |
| Séquenceur d'e-mails | Non détecté | Non détecté | Non détecté |
| Agent tarifaire (fantôme) | Oui : API catalogue hors mandat | Non détecté | Oui : table de remises commune |
| Extension résumé (fantôme) | Non tracé | Non détecté | Oui : fiche contact du CRM |

### 5b. Dosage de l'autonomie

| Agent | Degré (1 lecture, 2 rédaction, 3 écriture approuvée, 4 autonomie) | Propriétaire | Retour arrière |
|---|---|---|---|
| Veille concurrentielle | 1 | L. Vidal | Sans objet |
| Synthèse de comptes | 1 | N. Faure | Sans objet |
| Transcripteur d'appels | 3 | A. Mercier | Version précédente du compte rendu |
| Générateur de devis | 3 | P. Rousset | Devis non envoyé |
| Séquenceur d'e-mails | 3 | N. Faure | Séquence suspendue |
| Nettoyeur de données | 4 (tâche interne réversible) | A. Mercier | Sauvegarde avant traitement |
| Agent tarifaire (fantôme) | Inconnu | Non identifié | Inconnu |

### 5c. Audit du critère de notation

| Agent | Ce qui est noté | Effet pervers possible | Correction |
|---|---|---|---|
| Qualifieur leads | Nombre de leads transmis | Volume au détriment de la qualité | Noter le taux d'acceptation aval |
| Séquenceur d'e-mails | Taux de réponse | Relances forcées vers des comptes sensibles | Exclure les comptes en négociation |
| Transcripteur d'appels | Nombre de comptes rendus produits | Comptes rendus superficiels | Noter la complétude, revue par échantillon |

## 6. MANDAT D'AGENT (trois limites)

| Agent | Limite 1 | Limite 2 | Limite 3 | Seuil de remontée |
|---|---|---|---|---|
| Qualifieur leads | Ne jamais répondre aux demandes de prix | Ne jamais contacter un compte en négociation | Ne jamais modifier le scoring validé | Exception > 48 h |
| Séquenceur d'e-mails | Ne jamais écrire à un compte en négociation | Ne jamais envoyer plus de deux relances | Ne jamais joindre de tarif | Exception > 24 h |
| Support client niveau 1 | Ne jamais promettre un délai non garanti | Ne jamais accéder au dossier financier | Ne jamais modifier une commande | Exception > 4 h |

> Un mandat se cite de mémoire : trois limites par agent, pas trente règles.

## 7. CLOISONNEMENT ET QUARANTAINE

| Agent | Rôle (lecture/action) | Contenu externe ingéré | Quarantaine | Recoupement |
|---|---|---|---|---|
| Veille concurrentielle | Lecture | Oui (web public) | Oui | Deux sources minimum |
| Synthèse de comptes | Lecture | Oui (web public) | Oui | Deux sources minimum |
| Enrichisseur de contacts | Action | Oui (web public) | **Non** | Source unique |
| Extension résumé (fantôme) | Action | Oui (pages web) | **Non** | Aucun |
| Séquenceur d'e-mails | Action | Non | Sans objet | Sans objet |

> L'enrichisseur de contacts ingère du contenu externe et écrit dans le CRM sans quarantaine :
> il cumule lecture et action sur un contenu non vérifié. À cloisonner.

## 8. ADOPTION (point de contact, vallum, propriétaire métier)

| Cas d'usage | Point de contact | Niveau de maturité (1 à 4) | Propriétaire métier | Usage hebdo mesuré |
|---|---|---|---|---|
| Préparation d'appel | Fiche contact du CRM | 2 (assistance) | N. Faure | 71 % |
| Compte rendu d'appel | Objet opportunité du CRM | 3 (exécution encadrée) | A. Mercier | 64 % |
| Devis | Objet opportunité du CRM | 3 (exécution encadrée) | P. Rousset | 58 % |
| Veille concurrentielle | Portail marketing isolé | 1 (observation) | L. Vidal | 12 % |

**Vallum de gouvernance des données :** qui accède à quoi (rôles lecture, écriture et validation
séparés) · quelles actions d'agent sont tracées (journal d'écriture et d'envoi) · qui valide
(propriétaire métier nommé) · comment sortir (procédure de décommissionnement écrite).

> La veille concurrentielle est logée dans un portail isolé (usage 12 %) : c'est la garnison
> restée en retrait, elle gêne sa propre armée. À déplacer au point de contact réel.

## 9. PLAN D'ACTION PRIORISÉ

| Priorité | Action | Responsable | Échéance |
|---|---|---|---|
| **Critique** | Décommissionner l'agent tarifaire hérité et révoquer la clé API partagée | N. Berthomieu | 31/10/2026 |
| **Critique** | Désinstaller l'extension résumé et retirer son accès au CRM | N. Berthomieu | 31/10/2026 |
| **Critique** | Poser une seconde clé indépendante sur l'envoi d'e-mails et l'émission de devis | A. Mercier | 15/11/2026 |
| **Critique** | Rendre indépendant le validateur du transcripteur (jeton et prompt distincts) | A. Mercier | 15/11/2026 |
| Moyen | Quarantainer le contenu externe de l'enrichisseur avant écriture | L. Vidal | 30/11/2026 |
| Moyen | Corriger les critères de notation du qualifieur et du séquenceur | A. Mercier | 30/11/2026 |
| Faible | Déplacer la veille concurrentielle au point de contact réel | L. Vidal | 31/12/2026 |
| Faible | Consigner les 12 agents au registre, dont les deux fantômes décommissionnés | A. Mercier | 31/12/2026 |

## 10. REGISTRE DES AGENTS (livrable final)

| Nom | Version | Propriétaire | Accès (données + systèmes) | Autonomie | Seconde clé | Revue | Incidents |
|---|---|---|---|---|---|---|---|
| Qualifieur leads | 2.1 | A. Mercier | Contacts, CRM (écriture) | 2 | Humain (RevOps) | Mensuelle | Aucun |
| Transcripteur d'appels | 1.4 | A. Mercier | Appels, CRM (écriture) | 3 | Agent vérificateur | Mensuelle | 1 (boucle) |
| Veille concurrentielle | 1.0 | L. Vidal | Web public | 1 | Sans objet | Trimestrielle | Aucun |
| Enrichisseur de contacts | 3.2 | L. Vidal | Web public, CRM (écriture) | 2 | Humain (marketing) | Mensuelle | Aucun |
| Scoreur d'opportunités | 2.0 | A. Mercier | CRM (écriture) | 2 | Humain (RevOps) | Mensuelle | Aucun |
| Support client niveau 1 | 1.6 | S. Nguyen | Commandes, FAQ | 2 | Humain (service client) | Mensuelle | Aucun |
| Générateur de devis | 1.2 | P. Rousset | Catalogue, CRM | 3 | Humain (ADV) | Mensuelle | Aucun |
| Séquenceur d'e-mails | 2.3 | N. Faure | Contacts, messagerie | 3 | Humain (SDR senior) | Hebdomadaire | 1 (envoi) |
| Synthèse de comptes | 1.1 | N. Faure | Web public, CRM (lecture) | 1 | Sans objet | Trimestrielle | Aucun |
| Nettoyeur de données | 1.0 | A. Mercier | Base clients | 4 | Sans objet (interne) | Trimestrielle | Aucun |
| Agent tarifaire (fantôme) | inconnue | Non identifié | Tarifs, remises | Inconnu | Aucune | Sans objet | 1 (hors périmètre) |
| Extension résumé (fantôme) | 0.9 | Non identifié | Pages web, CRM | Inconnu | Aucune | Sans objet | Aucun |

Champs du registre portés par la version complète : nom, version, propriétaire, accès (données
et systèmes), niveau d'autonomie, seconde clé, déclencheurs, données traitées, revue périodique,
procédure de décommissionnement, incidents.

---

*Audit généré par la skill « Parole d'Ordre », strategiecommerciale.eu. Cas entièrement fictif :
organisation, personnes, agents, chiffres et sources sont inventés.*
