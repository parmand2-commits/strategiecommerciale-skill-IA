# Rapport de diagnostic tarifaire : exemple complet

> **Exemple golden file** : sortie de référence de la skill « Diagnostic d'architecture tarifaire »
> sur un cas fictif. Il illustre la structure attendue : cartographie de la valeur, trois questions
> argumentées, architecture à trois étages et mouvement retenu. Les comptes, les montants et les
> mesures internes sont fictifs ; les repères externes sont sourcés et datés.

---

## DIAGNOSTIC D'ARCHITECTURE TARIFAIRE

**Offre diagnostiquée :** plateforme de données et de reporting commercial (cas fictif)
**Date du diagnostic :** 05/10/2026
**Périmètre :** PME et ETI, 320 comptes de la base installée
**Grille en vigueur :** prix par siège, plus modules optionnels facturés à l'unité
**Sources de données :** export de facturation (répartition du revenu, réclamations), analytics
produit (distribution de l'usage), entretien avec les équipes produit et service client ; aucune
donnée inventée, aucune estimation non signalée

---

## 1. CARTOGRAPHIE DE LA VALEUR

| Composante de valeur | Existe sans usage intensif | Mesure disponible | Unité facturable naturelle |
|----------------------|----------------------------|-------------------|----------------------------|
| Socle de données consolidées | Oui | Non requise | Abonnement à la plateforme |
| Reporting récurrent | Oui | Non requise | Abonnement à la plateforme |
| Alertes sur signaux clients | Partiellement | Oui, télémétrie produit | Volume d'usage |
| Recommandations d'action | Non | Partielle, dépend du client | Résultat ou part de résultat |
| Économies réalisées par le client | Non | Non, non vérifiable en automatique | Aucune en l'état |

Les deux premières composantes portent l'essentiel de la valeur perçue ; les deux dernières sont
réelles mais variables. La cinquième n'est pas mesurable par l'éditeur, ce qui pèse sur la
deuxième question.

---

## 2. PREMIÈRE QUESTION, QUELLE PART DE LA VALEUR EXISTE SANS USAGE INTENSIF

**Réponse au test 80/20 :** à 20 % de l'usage habituel, un client conserve environ 75 % du bénéfice
perçu (estimation des équipes produit, à signaler comme estimation, non comme mesure).

**Part de valeur prévisible estimée :** 75 %

| Lecture | Seuil de méthode | Situation de l'offre | Implication |
|---------|------------------|----------------------|-------------|
| Valeur de socle | part prévisible de 70 % et plus | oui | La base porte l'essentiel du prix |
| Valeur mixte | entre 50 % et 70 % | non | Non retenue |
| Valeur d'usage | moins de 50 % | non | Non retenue |

**Contresens à nommer :** passer au prix à l'usage pur serait un contresens pour cette offre, car
les trois quarts du bénéfice sont obtenus sans usage intensif. La valeur variable existe, mais elle
ne commande pas le prix.

---

## 3. DEUXIÈME QUESTION, QUEL RISQUE D'EXÉCUTION L'ÉDITEUR ACCEPTE-T-IL DE PORTER

| Capacité | Question de contrôle | État | Verdict |
|----------|----------------------|------|---------|
| Capacité de mesure | Le résultat est-il mesuré automatiquement, de façon fiable et vérifiable par le client ? | non | Une part au résultat serait invérifiable, donc contestable |
| Capacité d'action | L'éditeur a-t-il des leviers réels sur ce résultat ? | partiel | Leviers sur l'adoption, aucun levier sur la performance commerciale du client |

**Risque accepté :** aucune part au résultat pour la masse des comptes. Le transfert de risque
dépasse ce que l'éditeur peut porter, faute de capacité de mesure et d'action sur les résultats
commerciaux du client.

**Verdict sur la composante au résultat :** réservée aux comptes éligibles. Une part au résultat
ouverte à tous serait une remise déguisée, accordée sous un nom qui la rend difficile à
comptabiliser.

---

## 4. TROISIÈME QUESTION, LE MODÈLE RESTE-T-IL LISIBLE

| Test | Question posée | Seuil de méthode | Résultat |
|------|-----------------|------------------|----------|
| Prévisibilité | Le client peut-il anticiper sa facture du mois suivant ? | Écart de plus ou moins 10 % | non conforme, écart de 18 % constaté entre devis et facture |
| Explicabilité | Peut-il citer les trois principaux facteurs de variation ? | Trois facteurs nommables | non conforme, les modules optionnels ne sont pas anticipés |
| Vérifiabilité | Peut-il vérifier lui-même les lignes déclencheuses ? | Chaque ligne consultable | conforme, les lignes d'abonnement sont consultables |

**Coût de l'illisibilité :** 140 réclamations de facturation sur les douze derniers mois (source :
export de facturation interne, période du 01/10/2025 au 30/09/2026), délai moyen de résolution de
9 jours ouvrés (même source), rétention de 78 % sur les comptes ayant contesté une facture contre
91 % sur l'ensemble de la base (même source).

---

## 5. ARCHITECTURE PROPOSÉE À TROIS ÉTAGES

| Étage | Fonction | Calibrage proposé | Garde-fou |
|-------|----------|-------------------|-----------|
| Base réduite | Couvre l'accès au socle de données et les coûts fixes | Abonnement, environ 30 % sous l'ancien prix par siège | Abaisser la barrière d'entrée sans perdre la couverture des coûts |
| Variable d'usage plafonnée | Capte la valeur réellement variable, alertes et volume traité | Palier par volume d'événements, avec plafond mensuel | Le plafond protège la prévisibilité du client |
| Contrat de résultat | Lie une part de la rémunération à des objectifs commerciaux précis | Réservé à 15 comptes stratégiques au maximum, 10 % du prix | Conditions d'éligibilité strictes, jamais un produit de masse |

**Conditions d'éligibilité du contrat de résultat :** capacité de mesure fiable, capacité d'action
réelle, données du client propres, engagement de son équipe, durée minimale. État pour cette offre :
capacité de mesure manquante en automatique, données du client à auditer compte par compte. L'étage
reste fermé jusqu'à réunion de ces conditions.

---

## 6. MOUVEMENT RETENU

**Étage ou grille visé :** base réduite et variable d'usage plafonnée (un seul mouvement de
recomposition du socle)
**Pourquoi lui :** la valeur est majoritairement prévisible, la base doit donc porter l'essentiel du
prix, mais elle est aujourd'hui illisible et son entrée est trop haute. Reconfigurer le socle traite
la prévisibilité et la lisibilité ensemble.
**Action concrète :** publier une base réduite avec un plafond d'usage visible sur la facture,
retirer les modules optionnels non anticipés, et suivre l'effet sur les réclamations et la rétention
**Propriétaire :** direction produit, appuyée par la direction financière (rôle, pas d'identité
personnelle)
**Mesure d'effet :** rétention des petits comptes et volume de réclamations de facturation
**Date de réinstrumentation :** 05/01/2027, un trimestre après, sur le même périmètre

---

## Repères externes (sourcés et datés)

- Selon l'enquête Cruxy d'avril 2026 auprès de 300 dirigeants de sociétés SaaS, 97 % prévoient
  d'abandonner la tarification au siège dans les deux ans, tandis que 94 % déclarent dans la même
  enquête que la tarification au siège reflète bien la valeur actuelle de leur produit. La même
  enquête situe l'hybride à 43 % d'utilisation, projetée à 61 % pour la fin 2026 (relayée par
  CFOtech UK et SaaStr ; reprise dans l'article « Pricing SaaS 2026 : le paradoxe 97/94 expliqué »,
  publié le 19/08/2026).
- Sun Tzu, chapitre 6, « L'eau suit la forme du terrain » : le modèle suit la forme de la valeur de
  l'offre, pas la tendance du marché (article « Pricing SaaS 2026 : le paradoxe 97/94 expliqué »,
  publié le 19/08/2026).

Ces repères situent l'enjeu du marché. Le diagnostic ci-dessus porte sur la valeur de cette offre
précise, et il ne se déduit d'aucune enquête.

---

*Rapport généré par la skill « Diagnostic d'architecture tarifaire », inspirée de l'article
« Pricing SaaS 2026 : le paradoxe 97/94 expliqué » (strategiecommerciale.eu). Cas fictif : les
comptes, montants et mesures internes sont illustratifs.*
