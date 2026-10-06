# Rapport de visibilité IA : exemple complet

> **Exemple golden file** : sortie de référence de la skill « Audit de visibilité IA » sur un cas
> fictif. Il illustre la structure attendue : inventaire du balisage sur la page servie, contenu
> citable manquant, mesure de dix à quinze questions sur trois assistants, chantier à ouvrir. La
> marque, les pages, les relevés et les citations sont fictifs ; les repères externes sont sourcés
> et datés.

---

## AUDIT DE VISIBILITÉ IA

**Marque auditée :** Atelier Flux, domaine atelier-flux.fr
**Date de l'audit :** 06/10/2026
**Périmètre d'URL :** 6 pages (société, offres, tarification, références, conformité, questions
fréquentes)
**Assistants de mesure :** assistant 1, assistant 2, assistant 3
**Mois de référence :** 09/2026, premier relevé, aucune comparaison disponible
**Sources de données :** pages publiques servies du 06/10/2026 ; saisie manuelle des douze questions
le 06/10/2026 ; origine des questions : commerciaux et support (entretien du 05/10/2026). Aucune
donnée inventée, aucune page non vérifiée présentée comme conforme.

---

## 1. INVENTAIRE DU BALISAGE

| Page | Type JSON-LD détecté | Conforme à Schema.org | Champs obligatoires manquants | Erreurs bloquantes | Méthode de vérification | Statut |
|------|----------------------|-----------------------|-------------------------------|--------------------|-------------------------|--------|
| / | Organization | partiel | legalName, sameAs | aucune | page servie, bloc `application/ld+json` | partiel |
| /offres | Service | partiel | areaServed, offers | aucune | page servie | partiel |
| /tarifs | aucun | sans objet | Organization, Product ou Service | sans objet | page servie | absent |
| /references | aucun | sans objet | Review | sans objet | page servie | absent |
| /conformite | aucun | sans objet | Organization | sans objet | page servie | absent |
| /questions-frequentes | FAQPage | partiel | 4 des 12 questions couvertes | aucune | page servie | partiel |

### Synthèse du balisage

| Type attendu | Attendu | Pages conformes | Pages partielles | Pages absentes |
|--------------|---------|-----------------|------------------|----------------|
| Organization | Obligatoire | 0 | 1 | 1 |
| Product ou Service | Obligatoire | 0 | 1 | 1 |
| FAQPage | Obligatoire si questions fréquentes | 0 | 1 | 0 |
| Review | Optionnel | 0 | 0 | 1 |

**Lecture.** Aucune page n'est pleinement conforme. Le profil le plus coûteux est celui du balisage
partiel : présent, donc jugé fait, mais incomplet sur les champs qui décident de la citation
(legalName et sameAs pour l'identité, areaServed et offers pour l'offre). La page de tarification et
la page de conformité ne déclarent rien : un agent qui les parcourt reconstitue seul ce que la marque
est.

---

## 2. CONTENU CITABLE

| Question | Réponse courte existante | Autonome hors contexte | Chiffre daté et attribué | Page porteuse | Action |
|----------|--------------------------|------------------------|--------------------------|---------------|--------|
| Quel logiciel de planification logistique pour une ETI industrielle ? | non | sans objet | non | aucune | créer la réponse courte |
| Combien coûte un logiciel de planification logistique ? | non | sans objet | non | aucune | créer la réponse courte |
| Quelle différence entre planification et ordonnancement ? | oui | oui | non | /questions-frequentes | ajouter un chiffre attribué |
| Comment intégrer un planificateur à un ERP existant ? | non | sans objet | non | aucune | créer la réponse courte |
| Quel gain de délai sur la préparation de commandes ? | non | sans objet | non | aucune | créer la réponse courte, avec mesure client datée |
| Quelles certifications de sécurité pour un SaaS logistique ? | non | sans objet | non | aucune | créer la réponse courte |
| Le logiciel gère-t-il le multi-entrepôt ? | oui | oui | non | /questions-frequentes | ajouter un chiffre attribué |
| Quel délai de déploiement pour une ETI ? | non | sans objet | non | aucune | créer la réponse courte |
| Comment migrer depuis un fichier de tableur ? | non | sans objet | non | aucune | créer la réponse courte |
| Quels clients de référence dans l'industrie ? | non | sans objet | non | aucune | créer la réponse courte, avec références datées |
| Le logiciel est-il conforme au RGPD ? | non | sans objet | non | aucune | créer la réponse courte et la page de conformité |
| Proposez-vous un accompagnement au changement ? | oui | partiel | non | /offres | rendre autonome et ajouter un chiffre attribué |

**Lecture.** Douze questions, deux réponses courtes réellement citables, aucune avec un chiffre daté
et attribué. Neuf questions n'ont aucune page porteuse : la matière que la machine peut extraire est
quasi absente, ce qui explique le taux de citation mesuré au paragraphe 3.

### État du fichier llms.txt

| Fichier | Présence | Dernière mise à jour | URL listées / périmètre | Écarts constatés |
|---------|----------|----------------------|-------------------------|------------------|
| /llms.txt | absent | inconnue | 0/6 | les six pages d'identité sont absentes du dispositif |

Un fichier llms.txt absent est consigné absent. Il n'a pas été créé en cours d'audit.

---

## 3. MESURE

Douze questions posées le 06/10/2026, mêmes formulations, dans l'ordre, sur les trois assistants
retenus.

| Question | A1 présence | A1 rang | A1 formulation | A2 présence | A2 rang | A2 formulation | A3 présence | A3 rang | A3 formulation | Concurrent cité |
|----------|-------------|---------|----------------|-------------|---------|----------------|-------------|---------|----------------|-----------------|
| Q1 | citée | 2e | plateforme de planification logistique | non citée | absent | sans objet | non citée | absent | sans objet | oui |
| Q2 | non citée | absent | sans objet | non citée | absent | sans objet | citée | 3e | éditeur de logiciels logistiques | oui |
| Q3 | citée | 1er | solution d'ordonnancement | citée | 1er | outil de planification | citée | 2e | logiciel de planification | non |
| Q4 | citée | 3e | connecteur ERP | non citée | absent | sans objet | non citée | absent | sans objet | oui |
| Q5 | non citée | absent | sans objet | non citée | absent | sans objet | non citée | absent | sans objet | oui |
| Q6 | non citée | absent | sans objet | citée | 2e | éditeur certifié sécurité | non citée | absent | sans objet | non |
| Q7 | citée | 1er | gestion multi-entrepôt | citée | 2e | plateforme multi-sites | citée | 1er | solution multi-entrepôt | non |
| Q8 | non citée | absent | sans objet | non citée | absent | sans objet | non citée | absent | sans objet | oui |
| Q9 | non citée | absent | sans objet | citée | 3e | outil de reprise de données | non citée | absent | sans objet | non |
| Q10 | non citée | absent | sans objet | non citée | absent | sans objet | non citée | absent | sans objet | oui |
| Q11 | citée | 2e | conformité RGPD | non citée | absent | sans objet | non citée | absent | sans objet | non |
| Q12 | non citée | absent | sans objet | non citée | absent | sans objet | non citée | absent | sans objet | non |

### Synthèse par assistant

| Assistant | Questions citées / total | Taux de présence | Rang médian | Écart au mois précédent |
|-----------|--------------------------|------------------|-------------|-------------------------|
| assistant 1 | 4/12 | 33,3 % | 2 | premier relevé |
| assistant 2 | 4/12 | 33,3 % | 2 | premier relevé |
| assistant 3 | 3/12 | 25,0 % | 2 | premier relevé |

Taux de présence calculé sur douze questions, source : relevé interne du 06/10/2026.

**Questions perdues au profit d'un concurrent :** Q1, Q2, Q4, Q5, Q8, Q10. Six des douze questions
citent un concurrent à la place de la marque. Les questions Q5 et Q8 portent sur des gains et des
délais : c'est exactement la matière qu'une réponse courte avec un chiffre daté et attribué
adresserait. Les formulations relevées sur Q1, Q2 et Q3 varient d'un assistant à l'autre, signe
d'entités mal déclarées plutôt que d'un déficit de notoriété.

---

## 4. CHANTIER À OUVRIER

**Chantier retenu :** contenu citable
**Pourquoi lui :** sur douze questions, deux réponses courtes sont réellement citables et aucune ne
porte un chiffre daté et attribué, alors que six questions sont perdues au profit d'un concurrent.
Le balisage est nécessaire mais ne cite pas la marque à lui seul : il rend lisible une matière qui
n'existe pas encore.
**Action concrète :** produire neuf réponses courtes, de moins de soixante mots, une par question sans
page porteuse, chacune avec un chiffre daté et attribué, en commençant par Q5 et Q8 ; déclarer ensuite
le balisage Organization et Service complet sur la page servie.
**Propriétaire :** marketing produit, appuyé par la direction commerciale pour sourcer les chiffres
client (rôle, pas d'identité personnelle)
**Date de réinstrumentation :** 06/11/2026, sur le même périmètre de six pages et les mêmes douze
questions, sans élargir

---

## 5. REPÈRES EXTERNES

- Selon TechCrunch (article de Sarah Perez, 5 août 2026), le trafic et les commandes issus de l'IA
  vers les boutiques de Shopify ont triplé en un an au deuxième trimestre 2026, et 75 % des achats
  attribués à l'IA se sont faits hors du top 100 des catégories.
- Selon Anteriad et Ascend2, via MarketScale (4 août 2026), cinquième benchmark annuel auprès de 631
  décideurs marketing, 45 % des marketeurs qui déploient l'attribution sur tout le tunnel dépassent
  significativement leurs objectifs, contre 24 % des autres.
- Selon Gartner (communiqué du 9 mars 2026, 646 acheteurs B2B interrogés, recueil août-septembre
  2025), 67 % des acheteurs B2B préfèrent une expérience sans commercial et 45 % déclarent avoir
  utilisé l'IA lors d'un achat récent.
- Selon Gartner (communiqué du 20 mai 2026, 645 acheteurs B2B), 69 % des acheteurs préfèrent faire
  valider auprès d'un commercial les informations générées par l'IA, et ils citent en moyenne sept
  sources d'information.

Ces repères situent l'enjeu, ils ne remplacent pas la mesure directe sur la marque auditée.

---

*Rapport généré par la skill « Audit de visibilité IA », inspirée de l'article « Visibilité IA :
soyez vu avant d'être shortlisté, comme à Midway » (strategiecommerciale.eu). Cas fictif : la marque,
les pages, les relevés et les citations sont illustratifs.*
