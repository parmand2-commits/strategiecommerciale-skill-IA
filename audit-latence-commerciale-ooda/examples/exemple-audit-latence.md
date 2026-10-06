# Rapport de latence commerciale : exemple complet

> **Exemple golden file** : sortie de référence de la skill « Audit de latence commerciale OODA »
> sur un cas fictif. Il illustre la structure attendue : quatre latences mesurées sur vingt
> dossiers d'un même segment, classement du tempo, écart de conversion et chantier retenu.
> Les comptes et les montants sont fictifs ; les repères externes sont sourcés et datés.

---

## AUDIT DE LATENCE COMMERCIALE

**Segment audité :** ETI industrie, comités de trois à cinq fonctions
**Date de l'audit :** 05/10/2026
**Corpus :** 20 opportunités (cible atteinte), closes ou en cours
**Période couverte :** 01/09/2025 au 30/09/2026
**Sources de données :** export CRM (dates d'étape, réunions, accord verbal, signature) ; valeurs
de dossiers fournies ; aucune donnée inventée, aucune date estimée non signalée

---

## 1. MESURE DES QUATRE LATENCES

| Dossier | Observer (h ouvrées) | S'orienter (sources tierces) | Décider (rapport interne/vendeur) | Agir (jours accord vers signature) | Alerte |
|---------|----------------------|------------------------------|-----------------------------------|------------------------------------|--------|
| D01 | 4 | 3 | 1,5 | 9 | aucune |
| D02 | 30 | 2 | 2,0 | 21 | Observer |
| D03 | 6 | 1 | 3,0 | 45 | Agir |
| D04 | 52 | 0 | 4,5 | 62 | Observer, S'orienter, Décider, Agir |
| D05 | 3 | 2 | 1,0 | 8 | aucune |
| D06 | 28 | 1 | 2,5 | 18 | Observer |
| D07 | 8 | 3 | 1,5 | 12 | aucune |
| D08 | 44 | 0 | 5,0 | 58 | Observer, S'orienter, Décider, Agir |
| D09 | 5 | 2 | 2,0 | 25 | aucune |
| D10 | 20 | 1 | 3,5 | 33 | Décider, Agir |
| D11 | 2 | 4 | 1,0 | 6 | aucune |
| D12 | 36 | 0 | 4,0 | 41 | Observer, S'orienter, Décider, Agir |
| D13 | 7 | 2 | 2,5 | 15 | aucune |
| D14 | 48 | 1 | 3,5 | 70 | Observer, Décider, Agir |
| D15 | 4 | 3 | 1,5 | 10 | aucune |
| D16 | 26 | 0 | 4,5 | 30 | Observer, S'orienter, Décider |
| D17 | 9 | 2 | 2,0 | 22 | aucune |
| D18 | 33 | 0 | 3,0 | 39 | Observer, S'orienter, Agir |
| D19 | 3 | 2 | 1,5 | 14 | aucune |
| D20 | 55 | 0 | 5,5 | 65 | Observer, S'orienter, Décider, Agir |

### Synthèse par latence

| Latence | Seuil d'alerte | Médiane observée | Dossiers en alerte | Écart au seuil |
|---------|----------------|------------------|--------------------|----------------|
| Observer | 24 heures ouvrées | 14,5 h | 9/20 | 9 dossiers franchissent 24 h, l'un atteint 55 h |
| S'orienter | aucune source tierce | 1,0 source | 6/20 | 6 dossiers à zéro source tierce |
| Décider | rapport 3 | 2,5 | 7/20 | jusqu'à 5,5, soit un rapport presque double |
| Agir | 30 jours | 23,5 jours | 8/20 | jusqu'à 70 jours sans raison documentée |

**Onze dossiers sur vingt franchissent au moins un seuil.** Les neuf dossiers sans alerte se
répartissent tous dans les colonnes vendeur et mixte, aucun dans la colonne comité : la latence
n'est pas un détail de confort, elle recoupe qui mène la boucle.

---

## 2. CLASSEMENT SELON QUI MÈNE LA BOUCLE

| Dossier | Mène la boucle | Étage qui décroche | Lecture |
|---------|----------------|--------------------|---------|
| D01 | Vendeur | aucun | Tempo maîtrisé de bout en bout |
| D02 | Vendeur | Observer | Signal traité tard, mais boucle rattrapée ensuite |
| D03 | Comité | Agir | Blocage sur la signature après accord verbal |
| D04 | Comité | Observer, S'orienter, Décider, Agir | Alerte sur les quatre étages, dossier perdu |
| D05 | Vendeur | aucun | Tempo maîtrisé |
| D06 | Mixte | Observer | Le vendeur reprend la main après un signal tardif |
| D07 | Vendeur | aucun | Tempo maîtrisé |
| D08 | Comité | Observer, S'orienter, Décider, Agir | Alerte sur les quatre étages, dossier perdu |
| D09 | Vendeur | aucun | Tempo maîtrisé |
| D10 | Comité | Décider, Agir | Comité qui délibère sans vous, signature étirée |
| D11 | Vendeur | aucun | Tempo maîtrisé |
| D12 | Comité | Observer, S'orienter, Décider, Agir | Alerte sur les quatre étages, dossier perdu |
| D13 | Mixte | aucun | Répartition équilibrée des transitions |
| D14 | Comité | Observer, Décider, Agir | Dossier perdu, latence cumulée |
| D15 | Vendeur | aucun | Tempo maîtrisé |
| D16 | Comité | Observer, S'orienter, Décider | En cours, orientation abandonnée au fournisseur |
| D17 | Mixte | aucun | Répartition équilibrée des transitions |
| D18 | Comité | Observer, S'orienter, Agir | En cours, dossier à réorienter |
| D19 | Vendeur | aucun | Tempo maîtrisé |
| D20 | Comité | Observer, S'orienter, Décider, Agir | Alerte sur les quatre étages, dossier perdu |

**Répartition :** 8 dossiers menés par le vendeur, 9 par le comité, 3 mixtes.

Le profil le plus coûteux est réuni par les dossiers D04, D08, D12 et D20 : menés par le comité
et sans aucune source tierce. Le vendeur y porte le cadrage et les critères de comparaison, ce qui
revient à faire le travail de l'acheteur, et la boucle se referme sans lui.

---

## 3. ÉCART DE CONVERSION

Calcul sur les 18 dossiers clos (2 dossiers en cours exclus, D16 et D18).

| Colonne | Dossiers clos | Gagnés | Taux de conversion |
|---------|---------------|--------|--------------------|
| Menés par le vendeur | 8 | 6 | 75,0 % |
| Menés par le comité | 7 | 2 | 28,6 % |
| Mixtes (repère) | 3 | 2 | 66,7 % |

**Écart de conversion :** 46,4 points de pourcentage entre les dossiers menés par le vendeur et
ceux menés par le comité.

Source : audit interne, corpus de 20 dossiers du segment ETI industrie, période du 01/09/2025 au
30/09/2026, export CRM du 05/10/2026.

---

## 4. COÛT DE LA LATENCE

- **Écart de conversion :** 46,4 points de pourcentage (audit interne, 05/10/2026)
- **Dossiers concernés (sur le corpus) :** 9 menés par le comité
- **Traduction annuelle, base de calcul explicite :** volume annuel du segment 60 opportunités,
  dont 45 % menées par le comité, soit 27 dossiers ; 27 × 0,464 = environ 12,5 dossiers perdus par
  an ; valeur moyenne du dossier 45 000 € ; 12,5 × 45 000 = environ 560 000 € par an

**Repères externes (sourcés et datés) :**

- Selon Gartner (communiqué du 19 mai 2026, enquête auprès de 210 directeurs commerciaux et
  dirigeants, recueil de janvier à février 2026), les outils d'IA font gagner 4,8 heures par
  semaine à un vendeur, 72 % des organisations réinvestissent peu ce temps, et celles qui le
  réinvestissent sont 3,1 fois plus susceptibles de dépasser leurs objectifs de conversion.
- Selon Gartner (communiqué du 25 juin 2025, enquête auprès de 632 acheteurs B2B, recueil d'août
  à septembre 2024), 61 % des acheteurs préfèrent une expérience d'achat sans commercial et 73 %
  évitent les sollicitations non pertinentes. Source de plus de douze mois : chiffre non
  reconfirmé à la date de l'audit.
- Selon InsideSales (Lead Response Study 2021, 5,7 millions de leads entrants, plus de 400
  entreprises), 0,1 % des leads reçoivent un contact en moins de cinq minutes et 57,1 % des
  premières tentatives d'appel arrivent plus d'une semaine après le lead. Source de plus de douze
  mois : chiffre non reconfirmé à la date de l'audit.

---

## 5. CHANTIER RETENU

**Latence ciblée :** S'orienter
**Pourquoi elle :** c'est l'étage qui commande le reste. Six dossiers sur vingt n'ont aucune source
tierce, et c'est le profil qui recoupe l'écart de conversion le plus large. Traiter l'observation
sans l'orientation déplacerait le problème sans le résoudre.
**Action concrète :** produire un document de travail citable en réunion interne, qui répond aux
questions du comité en votre absence, et en vérifier la citation dans les comptes rendus internes
du dossier suivant.
**Propriétaire :** champion du dossier, appuyé par le marketing produit (rôle, pas d'identité
personnelle)
**Date de réinstrumentation :** 05/11/2026, sur le même segment et le même périmètre, sans élargir

---

*Rapport généré par la skill « Audit de latence commerciale OODA », inspirée de l'article
« Boucle OODA : reprendre le tempo de la décision commerciale » (strategiecommerciale.eu). Cas
fictif : les comptes et montants sont illustratifs.*
