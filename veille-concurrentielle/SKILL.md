---
name: veille-concurrentielle
version: 1.1.1
description: >
  Qualifier et mesurer une veille concurrentielle B2B : transformer des changements relevés
  sur des sources publiques en signaux notés, en briefs datés et en indicateurs de contribution.
  Quatre modes : boucle quotidienne de collecte et de qualification, brief hebdomadaire, revue
  de perte en cinq questions, installation du registre de sources et du tableau de bord à six
  indicateurs. Le livrable est un brief d'une page où chaque signal porte son score sur neuf,
  sa source datée et la décision qu'il change. Un signal sans source datée est rejeté.
  Déclencheurs : "veille concurrentielle", "intelligence concurrentielle", "qualifier un
  signal", "brief concurrentiel", "taux de surprise", "revue de perte", "un concurrent a changé
  ses prix", "agent de veille".
  Inspiré de l'article « Veille concurrentielle : mesurer ce que la cellule apporte vraiment »,
  qui applique au renseignement concurrentiel le chapitre 3 de Sun Tzu : mesurer la connaissance
  de l'autre, pas l'issue de la bataille.
  Compatible avec tout agent (ChatGPT, Gemini, Perplexity, Copilot) : sans système de skills,
  copier INSTRUCTIONS.md comme prompt système.
---

# Veille concurrentielle

Qualifie les changements observés chez les concurrents, les transforme en signaux notés, et
mesure la contribution de la veille sur la chaîne du renseignement plutôt que sur le win rate.

> **Principe doctrinal** : Sun Tzu, chapitre 3. Connaître l'autre et se connaître donne la
> certitude ; se connaître seul donne une victoire pour une défaite. Un win rate mesure la
> seconde moitié. Une cellule de veille est jugée sur un indicateur qui décrit ce que
> l'entreprise fait de ses moyens, jamais ce qu'elle sait de son adversaire. Cette skill
> instrumente la moitié manquante.

## Ce que la skill produit

Trois livrables, jamais autre chose :

1. **Un brief** d'une page, à fréquence fixe, avec trois signaux au maximum, chacun noté sur
   neuf, sourcé et daté, et la décision qu'il change. Le silence est un brief valide.
2. **Une alerte** de cinq lignes, réservée aux signaux qui atteignent sept sur neuf.
3. **Un tableau de bord** à six indicateurs, une fois par mois, qui dit où la chaîne casse.

## Ajouter une source

Le registre des sources est porté par la configuration de la collecte, et nulle part ailleurs.

```bash
python3 boucle.py --config config.json --ajouter-source \
    --concurrent "Concurrent A" --famille tarifs \
    --url https://exemple.fr/tarifs --proprietaire pricing
```

La commande refuse une famille inconnue, une URL sans schéma http et une source déjà présente,
puis écrit de façon atomique. Elle crée le concurrent s'il n'existe pas encore.

En conversation, l'agent peut proposer l'ajout, mais il passe par cette même commande : une
source citée dans un fil de discussion et jamais écrite n'existe pas, et sans propriétaire
personne ne verra qu'elle a disparu. Pour un lot de sources, l'édition directe du fichier est
légitime ; la forme courte, une simple URL, vaut source critique rattachée au propriétaire du
concurrent.

Relire le registre sans rien ressaisir :

```bash
python3 boucle.py --config config.json --registre
```

## Les quatre modes

### Mode boucle quotidienne

L'agent lit le dossier de faits produit par la collecte (voir `runner/`), puis, pour chaque
changement : vérifie la source, note les trois critères, décide publier, vérifier ou archiver,
et rédige. Il ne collecte pas lui-même quand la boucle automatisée tourne : il qualifie.

Sortie : `out/<date>/signaux.json` et, s'il y a lieu, `out/<date>/alerte.md`.

### Mode brief hebdomadaire

Assemble les signaux de la semaine, applique la règle des trois maximum, rappelle les alertes
déjà émises et leur suite, et produit le brief à partir de `references/TEMPLATE.md`. Le brief
se termine toujours par l'état du dispositif : signaux vus, signaux publiés, sources dégradées.

### Mode revue de perte

Cinq questions par affaire perdue, codage des réponses, calcul du taux de surprise. Ce mode
fonctionne sans collecte : il travaille sur les comptes rendus et sur les commerciaux.

### Mode installation

Construit le registre de sources, fixe les seuils, choisit les destinataires, et pose le
tableau de bord. À faire une fois, à réviser une fois par trimestre.

## La chaîne du renseignement en cinq étages

| Étage | Ce que la veille produit | Indicateur |
|---|---|---|
| Couverture | la liste des sources réellement surveillées | taux de couverture |
| Détection | le signal, horodaté dès sa publication | délai de détection |
| Qualification | le tri entre mouvement et bruit | taux de bruit |
| Décision | la modification d'une décision commerciale | taux de décision instruite |
| Issue | l'affaire gagnée ou perdue | taux de surprise, puis win rate |

Le win rate est le dernier étage. Mesurer le dernier quand les quatre premiers sont vides
revient à constater un résultat sans connaître sa cause.

## La grille de qualification

Trois critères, notés de 1 à 3, total sur 9. Détail, exemples et cas limites dans
`references/GRILLE.md`.

| Critère | Question | 1 | 2 | 3 |
|---|---|---|---|---|
| Irréversibilité | le concurrent peut-il revenir en arrière à coût nul ? | oui, c'est un test | coût moyen | non, c'est engagé |
| Spécificité | mouvement ou rumeur ? | une page modifiée | deux sources concordantes | communiqué, dépôt, recrutement confirmé |
| Impact | quelle décision nommée change ? | aucune | une priorité de discours | une offre, un prix, un ciblage |

Règle de sortie : 7 à 9, publier et alerter ; 4 à 6, vérifier sous 48 heures avec une source
contradictoire ; 1 à 3, archiver sans diffuser.

## Le contrat de sortie

Le schéma complet est dans `references/contrat-sortie.json`. Trois règles de fond :

- **Provenance obligatoire** : chaque signal porte l'URL, la date de relevé et l'empreinte du
  texte. Un signal sans URL datée est rejeté, sans discussion.
- **Identifiant stable** : `url` plus `empreinte`. Le même fait ne peut pas être publié deux
  fois. Un signal déjà publié qui évolue garde son identifiant et change de version.
- **Silence explicite** : quand rien n'atteint 4, la sortie dit `"aucun signal au-dessus de 4
  cette semaine"` avec le nombre de pages vérifiées. Un brief vide non expliqué est un défaut.

## Garde-fous

- Ne jamais présenter une inférence comme un fait : ce qui n'est pas observé sur une page se
  déclare comme hypothèse.
- Signaler les sources dégradées : trois échecs consécutifs sur une même URL remontent en
  événement, sinon la couverture baisse en silence et le taux de couverture ment.
- Ne pas confondre volume et qualité : un agent qui produit trente alertes dont vingt-cinq de
  bruit a déplacé la charge de tri, il ne l'a pas supprimée.
- Ne jamais notifier un tiers (client, prospect, partenaire) et ne jamais écrire dans un CRM
  sans validation humaine.

## La boucle automatisée

`runner/boucle.py` fait le travail déterministe : récupérer les pages, calculer une empreinte
du texte utile, comparer avec l'état de la veille, cumuler les passages de la journée, repérer
les sources cassées, écrire le dossier de faits et un squelette de brief. Il ne note pas, il ne
rédige pas, il ne décide pas. L'agent reprend ensuite la qualification.

Le registre des sources vit dans cette configuration, et nulle part ailleurs : la commande
`--ajouter-source` contrôle la famille, l'URL et les doublons avant d'écrire, et la commande
`--registre` affiche la liste avec les propriétaires et la criticité. Le taux de couverture se
calcule sur les sources déclarées critiques, ce qui suppose qu'elles le soient.

Configuration : `runner/config.exemple.json`. Trois entrées d'ordonnancement suffisent :
quotidien tôt, brief hebdomadaire, tableau de bord mensuel. Une surveillance horaire ne se
justifie que sur trois à cinq URL pendant une fenêtre de lancement.

## Fichiers de référence

- `references/TEMPLATE.md` : le brief d'une page, structure imposée.
- `references/GRILLE.md` : grille détaillée, exemples par niveau, cas limites.
- `references/REGISTRE-SOURCES.md` : les huit familles de sources, ce qu'elles révèlent et ce
  qu'elles ne révèlent pas, leur fiabilité, leur cadence.
- `references/REVUE-PERTE.md` : les cinq questions, le codage, le calcul du taux de surprise.
- `references/INDICATEURS.md` : les six indicateurs, formule, source de donnée, seuil, piège.
- `references/contrat-sortie.json` : le schéma machine des sorties et les seuils de décision.
- `runner/README.md` : la boucle automatisée, sa configuration et son ordonnancement.
- `examples/BRIEF-EXEMPLE.md` : une sortie complète, cas réel composite.

## Ce que la skill ne fait pas

Elle ne remplace pas la décision commerciale : elle prépare le jugement. Elle ne garantit pas
l'exhaustivité des sources : elle rend la couverture mesurable. Elle ne promet pas de gagner
chaque affaire : elle promet qu'aucune affaire ne sera perdue par ignorance, ce qui est plus
modeste et plus vérifiable.
