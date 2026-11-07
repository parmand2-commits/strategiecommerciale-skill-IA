# TOOLS.md : manifeste d'outillage de la veille concurrentielle

Ce fichier déclare les outils disponibles et les préférences de sortie. L'agent le lit en
premier à chaque exécution. Modifiez-le pour brancher vos propres accès.

---

## Configuration générale

```yaml
language: fr                     # fr | en
output_format: markdown          # markdown | json
output_dir: ./veille             # dossier des sorties
cadence_quotidienne: "06:00"     # heure de la boucle de qualification
cadence_hebdomadaire: "lundi 07:00"
cadence_mensuelle: "1er du mois 07:00"
seuil_alerte: 7                  # score sur 9 declenchant une alerte immediate
seuil_publication: 4             # score minimal pour figurer dans le brief
signaux_max_par_brief: 3
fenetre_verification_heures: 48  # delai laisse pour corroborer un signal 4 a 6
langue_sources: [fr, en]
anonymiser_concurrents: false    # true = noms remplaces par C1, C2 dans le livrable
```

---

## Outils activés

### web_fetch (indispensable)

Récupération du contenu d'une page publique. Sert à vérifier un signal avant publication et à
produire la preuve datée. Toute affirmation publiée doit pouvoir être rattachée à une page
récupérée à une date connue.

Paramètres attendus : URL, date de relevé, empreinte du texte utile.

### web_search (recommandé)

Recherche d'une corroboration quand le signal n'a qu'une source. Deux sources concordantes
font passer la spécificité de 1 à 2. Ne jamais publier une note de spécificité supérieure à
celle que les sources justifient.

### filesystem (indispensable)

Lecture du dossier de faits produit par la boucle automatisée, écriture des sorties, mise à
jour de l'état de la veille. Arborescence attendue :

```
veille/
├── out/<AAAA-MM-JJ>/evenements.json     faits bruts, produits par la collecte
├── out/<AAAA-MM-JJ>/signaux.json        signaux qualifiés, produits par l'agent
├── out/<AAAA-MM-JJ>/alerte.md           alerte immédiate, si seuil atteint
├── briefs/<AAAA-SS>-brief.md            brief hebdomadaire
├── tableau-de-bord/<AAAA-MM>.md         tableau mensuel
└── etat.json                            empreintes, premières vues, sources dégradées
```

### webhook (optionnel)

Envoi du brief ou de l'alerte vers un canal de diffusion. Le contenu envoyé est le fichier
markdown, jamais un résumé reformulé par l'agent : ce qui est publié est ce qui a été relu.

### notification (optionnel)

Un signal noté 7 ou plus peut déclencher une notification au propriétaire de l'offre
concernée. Le message contient l'alerte de cinq lignes et le lien vers la source. Jamais de
notification vers un client, un prospect ou un partenaire.

---

## Ce qui n'est pas un outil

Un CRM, une plateforme d'enablement et un tableau de bord de direction sont des sources de
données, pas des outils d'action. L'agent les lit, ne les modifie jamais.

---

## Sortie par défaut

Un fichier markdown par livrable, nommé par date, dans le dossier configuré. Les signaux
qualifiés sont aussi écrits en JSON pour alimenter le tableau de bord sans ressaisie.
