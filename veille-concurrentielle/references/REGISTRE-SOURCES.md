# Registre de sources

Le registre est le seul actif durable d'une cellule de veille. Il survit au départ des
personnes. Sans lui, le taux de couverture est une impression ; avec lui, c'est un chiffre.

## Les huit familles

| Famille | Ce qu'elle révèle | Ce qu'elle ne dit pas | Fiabilité | Cadence de relevé |
|---|---|---|---|---|
| Tarifs et packaging | prix, paliers, essais, remises affichées | remises négociées, conditions réelles | très haute | quotidienne |
| Pages produit et documentation | périmètre, limites, nouveautés, dépréciations | ce qui est encore en test | haute | quotidienne |
| Offres d'emploi | recrutements, segments visés, technologies, croissance | si le poste est pourvu | haute | hebdomadaire |
| Communiqués et salle de presse | annonces officielles, partenariats, direction | ce qui est volontairement tu | très haute | quotidienne |
| Avis clients et comparateurs | irritants, motifs de perte, promesses tenues | ce que les clients ne disent pas | moyenne | hebdomadaire |
| Brevets et dépôts | intention de recherche, axes techniques | calendrier de mise sur le marché | haute, mais lente | mensuelle |
| Partenariats et intégrations | écosystème, canaux, dépendances | exclusivités réelles | haute | hebdomadaire |
| Salons et événements | cibles déclarées, discours public | ce qui se dit hors scène | moyenne | événementielle |

## Cadre de saisie

Pour chaque concurrent suivi :

```
concurrent: <nom>
priorite: cible | surveille | ignore
proprietaire: <fonction>
sources:
  tarifs: [<url>, <url>]
  produit: [<url>]
  recrutement: [<url>]
  communique: [<url>]
  avis: [<url>]
  brevets: [<url>]
  partenariat: [<url>]
  salon: [<url>]
note: <ce que l'on cherche en priorité chez ce concurrent>
```

## Règles de tenue

- **Une source, un propriétaire.** Une URL sans propriétaire est une URL qui sera abandonnée
  sans que personne ne s'en aperçoive.
- **Douze concurrents, six familles au démarrage.** Chercher l'exhaustivité la première semaine
  produit un registre que personne ne tient.
- **Déclarer les sources critiques.** Le taux de couverture se calcule sur les sources déclarées
  critiques, pas sur toutes. Sans cette distinction, l'indicateur devient un chiffre flatteur.
- **Retirer une source est une décision.** Elle se date et se motive, sinon la couverture baisse
  en silence.
- **Révision trimestrielle.** Un concurrent qui ne bouge plus depuis deux trimestres sort de la
  liste cible et passe en surveillance.

## Ce que le registre ne remplace pas

Il ne remplace ni l'entretien commercial, ni la revue de perte, ni le salon. Les sources
publiques disent ce que le concurrent veut montrer. La perte d'une affaire dit ce qu'il fait
vraiment.
