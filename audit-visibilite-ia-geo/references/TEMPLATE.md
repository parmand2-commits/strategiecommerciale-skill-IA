# TEMPLATE.md : Rapport de visibilité IA, [Marque], [Date]

> **Note pour l'agent** : gabarit de sortie. Remplir chaque champ, supprimer les annotations une fois
> le rapport rédigé. Les commentaires entre `<!-- -->` expliquent chaque champ et ne doivent pas
> apparaître dans la sortie finale.

---

## AUDIT DE VISIBILITÉ IA

<!-- En-tête du rapport : marque, date, périmètre, assistants, mois de référence. -->Un domaine, un
périmètre d'URL figé.

**Marque auditée :** [nom], domaine [domaine]
**Date de l'audit :** [JJ/MM/AAAA]
**Périmètre d'URL :** [N] pages (société, offres, tarification, références, conformité, questions
fréquentes)
**Assistants de mesure :** [assistant 1], [assistant 2], [assistant 3]
**Mois de référence :** [MM/AAAA], comparaison avec le relevé du [MM/AAAA] si disponible
**Sources de données :** [pages publiques servies / relevé de mesure / entretien], avec leur nature

---

## 1. INVENTAIRE DU BALISAGE

<!-- Vérification sur la page réellement servie, jamais sur le modèle ni sur le code source de
     l'éditeur. Un balisage absent de la page servie est compté absent. -->

| Page | Type JSON-LD détecté | Conforme à Schema.org | Champs obligatoires manquants | Erreurs bloquantes | Méthode de vérification | Statut |
|------|----------------------|-----------------------|-------------------------------|--------------------|-------------------------|--------|
| [/] | [Organization] | [oui / non] | [aucun / liste] | [aucune / liste] | [page servie, bloc `application/ld+json`] | [conforme] |
| [/offres] | [aucun] | [sans objet] | [Organization, Product ou Service] | [sans objet] | [page servie] | [absent] |
| [/tarifs] | [Product] | [partiel] | [offers, priceCurrency] | [aucune] | [page servie] | [partiel] |
| … | | | | | | |

<!-- Statuts possibles : conforme, partiel, absent, non vérifiable sur la page servie.
     Types attendus : Organization (obligatoire), Product ou Service (obligatoire, l'un des deux),
     FAQPage (obligatoire dès que des questions fréquentes existent), Review (optionnel). -->

### Synthèse du balisage

<!-- Une ligne par type attendu. Le nombre de pages conformes, partielles et absentes rend le
     diagnostic. -->

| Type attendu | Attendu | Pages conformes | Pages partielles | Pages absentes |
|--------------|---------|-----------------|------------------|----------------|
| Organization | Obligatoire | [N] | [N] | [N] |
| Product ou Service | Obligatoire | [N] | [N] | [N] |
| FAQPage | Obligatoire si questions fréquentes | [N] | [N] | [N] |
| Review | Optionnel | [N] | [N] | [N] |

---

## 2. CONTENU CITABLE

<!-- Une ligne par question figée. Seuil de réponse courte : moins de soixante mots lisibles
     isolément, hors de son contexte, avec au moins un chiffre attribué à une source datée. -->

| Question | Réponse courte existante | Autonome hors contexte | Chiffre daté et attribué | Page porteuse | Action |
|----------|--------------------------|------------------------|--------------------------|---------------|--------|
| [question 1] | [oui / non] | [oui / non] | [oui (source, date) / non] | [/url ou aucune] | [à produire / à corriger / rien] |
| [question 2] | [non] | [sans objet] | [non] | [aucune] | [créer la réponse courte] |
| … | | | | | |

### État du fichier llms.txt

| Fichier | Présence | Dernière mise à jour | URL listées / périmètre | Écarts constatés |
|---------|----------|----------------------|-------------------------|------------------|
| /llms.txt | [présent / absent] | [JJ/MM/AAAA ou inconnue] | [N]/[N] | [pages d'identité non listées, etc.] |

<!-- Un llms.txt absent est consigné absent, jamais créé sans validation explicite. -->

---

## 3. MESURE

<!-- Une ligne par question, trois sous-colonnes par assistant : présence, rang, formulation.
     Mêmes formulations et mêmes assistants à chaque passage. -->

| Question | [assistant 1] présence | [assistant 1] rang | [assistant 1] formulation | [assistant 2] présence | [assistant 2] rang | [assistant 2] formulation | [assistant 3] présence | [assistant 3] rang | [assistant 3] formulation | Concurrent cité |
|----------|------------------------|--------------------|---------------------------|------------------------|--------------------|---------------------------|------------------------|--------------------|---------------------------|-----------------|
| [question 1] | [citée] | [1er] | [termes relevés] | [citée] | [2e] | [termes relevés] | [non citée] | [absent] | [sans objet] | [non] |
| [question 2] | [non citée] | [absent] | [sans objet] | [citée] | [3e] | [termes relevés] | [non citée] | [absent] | [sans objet] | [oui, nom] |
| … | | | | | | | | | | |

<!-- Valeurs de présence : citée, non citée. Valeurs de rang : 1er, 2e, 3e, au-delà, absent.
     La colonne « concurrent cité » signale les questions où un concurrent apparaît à votre place. -->

### Synthèse par assistant

<!-- Taux de présence = questions citées rapportées au total. L'écart au mois précédent est la
     seule preuve de progrès. -->

| Assistant | Questions citées / total | Taux de présence | Rang médian | Écart au mois précédent |
|-----------|--------------------------|------------------|-------------|-------------------------|
| [assistant 1] | [N]/[N] | [X %] | [X] | [+X point, -X point, stable] |
| [assistant 2] | [N]/[N] | [X %] | [X] | [idem] |
| [assistant 3] | [N]/[N] | [X %] | [X] | [idem] |

**Questions perdues au profit d'un concurrent :** [liste des questions où un concurrent est cité à
votre place, avec l'assistant concerné et l'action de contenu ou de balisage déclenchée].

---

## 4. CHANTIER À OUVRIR

<!-- Le chantier de mesure se poursuit chaque mois. Un seul des deux autres chantiers est ouvert par
     cycle, en visant l'écart le plus large rapporté à l'effort. -->

**Chantier retenu :** [balisage / contenu citable]
**Pourquoi lui :** [l'écart le plus large rapporté à l'effort, 2 phrases maximum]
**Action concrète :** [ce qui change, à quelle échéance]
**Propriétaire :** [rôle, pas d'identité personnelle]
**Date de réinstrumentation :** [JJ/MM/AAAA], soit un mois après, sur le même périmètre d'URL et les
mêmes questions

---

## 5. REPÈRES EXTERNES

<!-- Chiffres sourcés et datés uniquement. Toute source de plus de douze mois est signalée comme non
     confirmée à la date de l'audit. -->

- [repère 1, source nommée, date]
- [repère 2, source nommée, date]
- [repère 3, source nommée, date, signalée non confirmée si plus de douze mois]

---

*Rapport généré par la skill « Audit de visibilité IA », inspirée de l'article « Visibilité IA :
soyez vu avant d'être shortlisté, comme à Midway » (strategiecommerciale.eu).*
