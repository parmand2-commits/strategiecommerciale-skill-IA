# Formats de sortie

Trois livrables, trois formats. Le format se choisit selon l'usage, jamais selon l'habitude.

## Le brief hebdomadaire : markdown

C'est le format par défaut, et il ne change pas.

- il se lit sur un téléphone en deux minutes, ce qui est la seule façon qu'un brief hebdomadaire
  soit lu ;
- il se compare d'une semaine à l'autre : un diff montre ce qui a changé, un document mis en
  page ne le montre pas ;
- il se colle sans perte dans un espace de travail, un wiki, une messagerie ou un courriel ;
- il ne dépend d'aucun outil pour être produit, relu ou archivé.

Ajouter du HTML pour l'envoi par courriel est légitime. Convertir en traitement de texte ne
l'est pas : un brief qui prend la forme d'un document cesse d'être une note et devient une
pièce à classer.

## L'alerte : cinq lignes de texte, aucun fichier

Fait, preuve datée, score, décision, échéance. Dans le canal où travaille le propriétaire de la
décision. Une alerte en pièce jointe est une alerte non lue.

## Le dossier de veille trimestriel : markdown source, export possible

Deux cas seulement justifient un export en traitement de texte ou en PDF :

- le document quitte l'équipe et circule dans une instance où le markdown n'est pas lisible ;
- il doit être paginé, signé, ou joint à un livrable contractuel.

Dans ces cas, le markdown reste la source. On l'exporte, on ne le ressaisit pas. Un dossier
tenu à la main dans un traitement de texte dérive de la source en trois révisions.

## Si vous exportez

Spécifications minimales, à respecter à la lettre, sinon l'export est refusé :

| Élément | Spécification |
|---|---|
| Titre du document | une ligne, celui du brief ou du dossier, sans numérotation automatique |
| Corps | 11 points, interligne 1,15, marges 2,5 cm |
| Titres de niveau 2 | 14 points, gras, couleur encre |
| Tableaux | en-tête gras, filets horizontaux seuls, aucune couleur de remplissage |
| Sources | en pied, en 8 points, URL en clair et date de relevé |
| Pagination | en pied de page, à droite, à partir de la deuxième page |
| Longueur | brief : une page. Dossier trimestriel : cinq pages maximum |

Le contenu ne change pas d'un format à l'autre. Ce qui change est la mise en page, et elle ne
doit jamais porter d'information que le texte ne porte pas déjà.

## Ce qu'il ne faut pas faire

- Envoyer un brief en pièce jointe alors qu'il tient dans le corps d'un message.
- Produire un dossier trimestriel en markdown puis le coller dans un traitement de texte à la
  main : la conversion manuelle est la première cause de divergence entre la source et le
  document diffusé.
- Choisir le format avant de savoir qui lit et dans quel contexte. La question n'est pas
  « quel est le meilleur format », elle est « où ce document sera-t-il lu, et par qui ».
