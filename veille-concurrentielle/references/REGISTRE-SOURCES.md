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

## Où vit le registre

Une seule liste, jamais deux. Le registre est porté par la configuration de la collecte
(`runner/config.json`), et se relit sans ressaisie :

```bash
python3 boucle.py --config config.json --registre
```

Cette commande affiche concurrent, famille, source, propriétaire et criticité. C'est cette
liste qui alimente la collecte et le taux de couverture. Un registre tenu à part dans un
tableur dérive toujours, et la dérive n'est visible qu'au moment où la couverture baisse.

Pour ajouter une source, la commande contrôle avant d'écrire :

```bash
python3 boucle.py --config config.json --ajouter-source \
    --concurrent "Concurrent A" --famille tarifs \
    --url https://exemple.fr/tarifs --proprietaire pricing
```

Elle refuse une famille inconnue, une URL sans schéma http, et une source déjà présente. Une
source ajoutée de vive voix dans une conversation doit passer par la même commande : ce qui
n'est pas écrit n'existe pas.

Forme de la configuration, pour un ajout par lot :

```json
{
  "concurrents": [
    {
      "nom": "Concurrent A",
      "priorite": "cible",
      "proprietaire": "avant-vente",
      "note": "surveiller le milieu de gamme et les intégrations",
      "sources": {
        "tarifs": [{"url": "https://exemple.fr/tarifs", "proprietaire": "pricing", "critique": true}],
        "produit": ["https://exemple.fr/nouveautes"]
      }
    }
  ]
}
```

Une source écrite en forme courte, une simple URL, est réputée critique et rattachée au
propriétaire du concurrent. La forme longue sert aux cas où le propriétaire ou la criticité
diffèrent, ce qui est fréquent : une page tarifaire appartient au pricing, une page produit à
l'avant-vente.

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
