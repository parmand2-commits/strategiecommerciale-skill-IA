# TEMPLATE.md : Rapport de latence commerciale, [Segment], [Date]

> **Note pour l'agent** : gabarit de sortie. Remplir chaque champ, supprimer les annotations une
> fois le rapport rédigé. Les commentaires entre `<!-- -->` expliquent chaque champ et ne doivent
> pas apparaître dans la sortie finale.

---

## AUDIT DE LATENCE COMMERCIALE

<!-- En-tête du rapport : segment, date, taille du corpus, période couverte. -->Un seul segment.

**Segment audité :** [nom du segment]
**Date de l'audit :** [JJ/MM/AAAA]
**Corpus :** [N] opportunités (cible : 20), closes ou en cours
**Période couverte :** [date de début] au [date de fin]
**Sources de données :** [CRM / export / entretien], avec leur nature

---

## 1. MESURE DES QUATRE LATENCES

<!-- Une ligne par dossier. Une colonne par latence. Le seuil est fixe, voir TOOLS.md. -->

| Dossier | Observer (h ouvrées) | S'orienter (sources tierces) | Décider (rapport interne/vendeur) | Agir (jours accord vers signature) | Alerte |
|---------|----------------------|------------------------------|-----------------------------------|------------------------------------|--------|
| [D01] | [0,5] | [2] | [2,0] | [12] | [aucune] |
| [D02] | [40] | [0] | [5,0] | [55] | [Observer, S'orienter, Décider, Agir] |
| … | | | | | |

<!-- Seuils d'alerte : Observer plus de 24 heures ouvrées ; S'orienter aucune source tierce ;
     Décider rapport supérieur à 3 ; Agir plus de 30 jours sans raison documentée. -->

### Synthèse par latence

<!-- Une ligne par latence. Le délai médian observé et l'écart au seuil rendent le diagnostic. -->

| Latence | Seuil d'alerte | Médiane observée | Dossiers en alerte | Écart au seuil |
|---------|----------------|------------------|--------------------|----------------|
| Observer | 24 heures ouvrées | [X] | [N]/20 | [+X h] |
| S'orienter | aucune source tierce | [X] sources | [N]/20 | [à 0 source : alerte] |
| Décider | rapport 3 | [X] | [N]/20 | [+X] |
| Agir | 30 jours | [X] jours | [N]/20 | [+X jours] |

---

## 2. CLASSEMENT SELON QUI MÈNE LA BOUCLE

<!-- Pour chaque dossier, établir qui a déclenché la majorité des transitions :
     le vendeur ou le comité. Un dossier ne peut être que dans une colonne. -->

| Dossier | Mène la boucle | Étage qui décroche | Lecture |
|---------|----------------|--------------------|---------|
| [D01] | [Vendeur / Comité / Mixte] | [Observer / S'orienter / Décider / Agir] | [une phrase] |
| … | | | |

**Répartition :** [N] dossiers menés par le vendeur, [N] par le comité, [N] mixtes.

<!-- Le profil le plus coûteux : mené par le comité et sans aucune source tierce. -->

---

## 3. ÉCART DE CONVERSION

<!-- Taux de conversion de chaque colonne du classement, puis l'écart en points de pourcentage. -->

| Colonne | Dossiers | Gagnés | Taux de conversion |
|---------|----------|--------|--------------------|
| Menés par le vendeur | [N] | [N] | [X %] |
| Menés par le comité | [N] | [N] | [X %] |

**Écart de conversion :** [X] points de pourcentage.

<!-- Si les valeurs de dossiers sont absentes, laisser en points de pourcentage et le signaler. -->

---

## 4. COÛT DE LA LATENCE

<!-- Deux niveaux : en points de pourcentage et en dossiers, puis en montant si les valeurs
     et le volume annuel sont fournis. Aucun montant sans base de calcul explicite. -->

- **Écart de conversion :** [X] points de pourcentage
- **Dossiers concernés (sur le corpus) :** [N] menés par le comité
- **Traduction annuelle (si valeurs fournies) :** écart [X] % × volume annuel [N] × valeur
  moyenne [€] = [€]. Base de calcul : [à expliciter]

**Repères externes (à citer avec source et date) :** [repère 1, source, date] ; [repère 2,
source, date]. Toute source de plus de douze mois est signalée comme non confirmée.

---

## 5. CHANTIER RETENU

<!-- Un seul chantier parmi les quatre. Viser la latence la plus longue rapportée à son coût. -->

**Latence ciblée :** [Observer / S'orienter / Décider / Agir]
**Pourquoi elle :** [la plus longue rapportée à son coût, 2 phrases maximum]
**Action concrète :** [ce qui change, qui le porte, à quelle échéance]
**Propriétaire :** [première ligne / champion et marketing produit / account executive / sales
manager], rôle, pas d'identité personnelle
**Date de réinstrumentation :** [JJ/MM/AAAA], soit un mois après, sans élargir le périmètre

---

*Rapport généré par la skill « Audit de latence commerciale OODA », inspirée de l'article
« Boucle OODA : reprendre le tempo de la décision commerciale » (strategiecommerciale.eu).*
