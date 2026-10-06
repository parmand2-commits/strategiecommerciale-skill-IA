# TEMPLATE.md : Rapport de diagnostic tarifaire, [Offre], [Date]

> **Note pour l'agent** : gabarit de sortie. Remplir chaque champ, supprimer les annotations une
> fois le rapport rédigé. Les commentaires entre `<!-- -->` expliquent chaque champ et ne doivent
> pas apparaître dans la sortie finale.

---

## DIAGNOSTIC D'ARCHITECTURE TARIFAIRE

<!-- En-tête du rapport : offre, date, périmètre, sources de données. -->

**Offre diagnostiquée :** [nom de l'offre]
**Date du diagnostic :** [JJ/MM/AAAA]
**Périmètre :** [segments couverts], [nombre de comptes de la base installée]
**Grille en vigueur :** [unité facturée : siège / usage / tokens / résultat / hybride]
**Sources de données :** [facturation / analytics produit / entretien], avec leur nature

---

## 1. CARTOGRAPHIE DE LA VALEUR

<!-- Une ligne par composante de valeur (ce que le client obtient), pas par fonctionnalité.
     « Existe sans usage intensif » : oui / non / partiellement. -->

| Composante de valeur | Existe sans usage intensif | Mesure disponible | Unité facturable naturelle |
|----------------------|----------------------------|-------------------|----------------------------|
| [Socle de données] | [Oui] | [Non requise] | [Abonnement] |
| [Leads qualifiés] | [Non] | [Oui, télémétrie] | [Résultat livré] |
| … | | | |

---

## 2. PREMIÈRE QUESTION, QUELLE PART DE LA VALEUR EXISTE SANS USAGE INTENSIF

<!-- Test 80/20 : poser la question à l'éditeur et retenir sa réponse, signalée comme mesure
     ou comme estimation. -->

**Réponse au test 80/20 :** à 20 % de l'usage habituel, le client conserve [X] % du bénéfice perçu.
Réponse obtenue par [mesure / estimation des équipes produit, à signaler comme estimation].

**Part de valeur prévisible estimée :** [X] %

<!-- Seuils de méthode : 70 % et plus, valeur de socle, la base porte l'essentiel du prix ;
     entre 50 % et 70 %, valeur mixte ; moins de 50 %, valeur d'usage, la variable porte
     l'essentiel. Ces seuils sont ceux de la méthode, pas des données de marché. -->

| Lecture | Seuil de méthode | Situation de l'offre | Implication |
|---------|------------------|----------------------|-------------|
| Valeur de socle | part prévisible de 70 % et plus | [oui / non] | [la base porte l'essentiel du prix] |
| Valeur mixte | entre 50 % et 70 % | [oui / non] | [calibrer la variable sur la part variable] |
| Valeur d'usage | moins de 50 % | [oui / non] | [la variable porte l'essentiel du prix] |

**Contresens à nommer (s'il existe) :** [une phrase, ou « aucun contresens détecté »]

---

## 3. DEUXIÈME QUESTION, QUEL RISQUE D'EXÉCUTION L'ÉDITEUR ACCEPTE-T-IL DE PORTER

<!-- Une composante au résultat transfère le risque d'exécution du client vers l'éditeur.
     Deux capacités obligatoires. Si l'une manque, écarter la part au résultat. -->

| Capacité | Question de contrôle | État | Verdict |
|----------|----------------------|------|---------|
| Capacité de mesure | Le résultat est-il mesuré automatiquement, de façon fiable et vérifiable par le client ? | [oui / non] | [si non : part au résultat invérifiable] |
| Capacité d'action | L'éditeur a-t-il des leviers réels sur ce résultat ? | [oui / non] | [si non : remise déguisée] |

**Risque accepté :** [part de résultat envisagée, en pourcentage du prix, avec sa justification]

**Verdict sur la composante au résultat :** [retenue / écartée / réservée aux comptes éligibles],
[une phrase de justification]

---

## 4. TROISIÈME QUESTION, LE MODÈLE RESTE-T-IL LISIBLE

<!-- Trois tests sur le canevas de facture réel. Seuil de méthode : plus ou moins 10 % d'écart
     entre facture anticipée et facture reçue. -->

| Test | Question posée | Seuil de méthode | Résultat |
|------|-----------------|------------------|----------|
| Prévisibilité | Le client peut-il anticiper sa facture du mois suivant ? | Écart de plus ou moins 10 % | [conforme / non conforme] |
| Explicabilité | Peut-il citer les trois principaux facteurs de variation ? | Trois facteurs nommables | [conforme / non conforme] |
| Vérifiabilité | Peut-il vérifier lui-même les lignes déclencheuses ? | Chaque ligne consultable | [conforme / non conforme] |

**Coût de l'illisibilité :** [volume de réclamations de facturation sur douze mois], [délai moyen
de résolution], [rétention des comptes ayant contesté]. Si ces données sont absentes, l'indiquer et
rester qualitatif.

---

## 5. ARCHITECTURE PROPOSÉE À TROIS ÉTAGES

<!-- L'architecture suit la forme de la valeur diagnostiquée, pas un modèle dominant. -->

| Étage | Fonction | Calibrage proposé | Garde-fou |
|-------|----------|-------------------|-----------|
| Base réduite | Couvre l'accès au socle et les coûts fixes | [montant ou fourchette] | [abaisser la barrière d'entrée sans perdre la couverture] |
| Variable d'usage plafonnée | Capte la valeur réellement variable | [unité et plafond] | [plafond qui protège la prévisibilité] |
| Contrat de résultat | Lie une part de la rémunération à des objectifs précis | [part du prix, comptes concernés] | [conditions d'éligibilité strictes] |

**Conditions d'éligibilité du contrat de résultat :** capacité de mesure fiable, capacité d'action
réelle, données du client propres, engagement de son équipe, durée minimale. État pour l'offre
diagnostiquée : [conditions réunies / manquantes, préciser lesquelles].

---

## 6. MOUVEMENT RETENU

<!-- Un seul mouvement : reconfigurer un étage, ou confirmer la grille en l'état. -->

**Étage ou grille visé :** [base réduite / variable d'usage / contrat de résultat / grille maintenue]
**Pourquoi lui :** [deux phrases maximum, rapporté à la valeur diagnostiquée]
**Action concrète :** [ce qui change, qui le porte, à quelle échéance]
**Propriétaire :** [direction produit / direction financière / avant-vente], rôle, pas d'identité
personnelle
**Mesure d'effet :** [rétention des petits comptes / réclamations de facturation / part du revenu
variable / conversion de la base]
**Date de réinstrumentation :** [JJ/MM/AAAA], soit un trimestre après, sans élargir le périmètre

---

*Rapport généré par la skill « Diagnostic d'architecture tarifaire », inspirée de l'article
« Pricing SaaS 2026 : le paradoxe 97/94 expliqué » (strategiecommerciale.eu).*
