# La boucle automatisée

`boucle.py` fait le travail déterministe de la veille et rien d'autre : récupérer les pages,
calculer une empreinte du texte utile, comparer avec l'état de la veille, cumuler les passages
d'une même journée, repérer les sources cassées, écrire le dossier de faits et un squelette de
brief.

Il ne note pas l'importance d'un signal, il ne rédige pas, il ne décide pas. C'est le travail de
l'agent et de la grille. La raison est simple : une note automatique fige la grille dans du
code, et un agent qui récupère les pages lui-même paie des jetons pour faire du HTTP puis
hallucine des contenus.

## Ce qu'il produit

```
out/<AAAA-MM-JJ>/evenements.json      faits du jour, cumulés sans doublon
out/<AAAA-MM-JJ>/brief-squelette.md   trame pré-remplie pour l'agent
etat.json                             empreintes, premières vues, échecs, sources dégradées
```

Chaque événement porte le concurrent, la famille de source, l'URL, le statut HTTP, le titre de
la page, l'empreinte, une irréversibilité proposée (poids de la famille) et une spécificité
proposée (nombre de pages touchées dans la même famille au même relevé). Le critère d'impact
reste vide : il dépend de la stratégie de l'entreprise, pas de la page.

## Usage

```bash
python3 boucle.py --config config.json
python3 boucle.py --config config.json --dry       # ne rien écrire, afficher le résumé
python3 boucle.py --config config.json --force     # ignorer l'état, tout est neuf
```

Codes de sortie : 0 en marche normale, y compris avec des sources cassées, 2 seulement si
toutes les sources tombent. Une source cassée est un signal à remonter, pas une panne de la
boucle : un ordonnanceur qui alerte à chaque échec finit ignoré.

## Ajouter une source

Trois portes, une seule qui contrôle.

Par la commande, et c'est le chemin recommandé, parce qu'elle refuse ce qui doit être refusé :

```bash
python3 boucle.py --config config.json --ajouter-source \
    --concurrent "Concurrent A" --famille tarifs \
    --url https://exemple.fr/tarifs --proprietaire pricing
```

Elle vérifie que la famille existe, que l'URL commence par http, que la source n'est pas déjà
présente ailleurs dans le registre, et elle crée le concurrent s'il n'existe pas encore. Elle
écrit la configuration de façon atomique et renvoie un code non nul en cas de refus.

Par la conversation, quand l'agent a accès au fichier : c'est acceptable pour une source
ajoutée en passant, à condition que l'agent passe ensuite par la même commande. Une URL ajoutée
à la main dans une conversation et jamais écrite nulle part n'existe pas.

Par l'édition directe du fichier, pour un lot de sources ou une reprise de registre. La forme
courte, une simple URL, suffit : la source est alors réputée critique et rattachée au
propriétaire du concurrent. La forme longue porte un propriétaire et une criticité explicites.

```json
{
  "nom": "Concurrent A",
  "proprietaire": "avant-vente",
  "sources": {
    "tarifs": [{"url": "https://exemple.fr/tarifs", "proprietaire": "pricing", "critique": true}],
    "produit": ["https://exemple.fr/nouveautes"]
  }
}
```

Le registre se relit sans rien tenir à la main :

```bash
python3 boucle.py --config config.json --registre
```

Il affiche concurrent, famille, source, propriétaire et criticité. C'est cette liste unique qui
alimente la collecte et le taux de couverture, et non une seconde liste tenue dans un tableur.

## Configuration

Copier `config.exemple.json`, remplacer les concurrents et les URL. Les clés utiles :
`pause_secondes` entre deux requêtes, `delai_max_secondes` par requête, et
`seuil_echecs_source_degradee`, fixé à 3.

Le registre des sources reste la référence : chaque URL de la configuration doit avoir un
propriétaire dans le registre, sinon personne ne verra qu'elle a disparu.

## Ordonnancement

Trois entrées suffisent, quel que soit l'ordonnanceur disponible sur la machine ou dans la
plateforme d'automatisation.

| Entrée | Quand | Ce qui tourne |
|---|---|---|
| collecte et qualification | chaque jour tôt | `boucle.py`, puis l'agent sur `evenements.json` |
| brief | lundi matin | l'agent assemble la semaine, applique le maximum de trois signaux |
| tableau de bord | premier du mois | l'agent calcule les six indicateurs |

Une surveillance horaire ne se justifie que sur trois à cinq URL pendant une fenêtre de
lancement. Partout ailleurs, elle produit des requêtes et du bruit sans gain de décision.

## Ce que la boucle ne voit pas

Elle ne voit pas les pages derrière une authentification, les documents commerciaux, les prix
négociés, ni ce qui se dit dans un salon. Ces informations restent du ressort de l'entretien et
de la revue de perte, et c'est la revue de perte qui les rend mesurables.
