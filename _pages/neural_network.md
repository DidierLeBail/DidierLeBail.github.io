---
permalink: /neural_network
title: "Neural network"
author_profile: true
---

Each agent has a distinct neural network.
This network is characterized by three properties:
* neural diversity
* plasticity: connexions between neurons can evolve during the life course of the agent
* the plasticity rules are not fixed by the hand of the programmer, but rather are decoded from the genome

## Neural types
We distinguish between two types:
(1) functional types, which include input neurons, output neurons and others, and (2) structural types, which describe how the neuron is processing its inputs.

A neuron can have multiple functional types but has only one structural type.
For example, a neuron can be both a sensory neuron and a motor neuron.



## Plasticity

Dans notre projet d'obtenir une intelligence générale, on considère une population de "lapins", chaque lapin possédant un réseau de neurones commandant un corps immergé dans un environnement virtuel.
Cette partie vise à décrire les propriétés de ce réseau de neurones.

La première couche de ce réseau constitue les neurones sensoriels.
Il en existe trois types:
photoneurones, sensibles à la lumière, les phononeurones, sensibles au son, et les neurones de la faim, qui renseignent le lapin sur la quantité des ressources disponibles dans son organisme.

La couche de sortie du réseau constitue les motoneurones.
Il en existe deux types:
les neurones musculaires, qui déclenchent un mouvement du corps du lapin, et les neurones de la parole, qui permettent au lapin d'émettre des sons.

Notons qu'un neurone peut posséder plusieurs types à la fois.
Le cerveau d'un lapin n'a pas d'architecture pré-spécifiée:
celle-ci sera sculptée par un algo génétique et par le vécu du lapin (cerveau plastique).
Le cerveau d'un lapin est aussi hétérogène:
il peut rassembler en son sein des neurones fonctionnant selon des principes différents, appelés types fonctionnels.

Il existe pour le moment 8 types fonctionnels:
* neurones artificiels (sans mémoire, avec fonction d'activation de type sigmoïde ou ReLu)
* neurones temporels (avec état interne donnant une mémoire, avec fonction d'activation de type Heaviside)
* neurones binaires (combinant ou superposant des opérations binaires de ses entrées, e.g. AND, OR, XOR, etc.)
* neurones mixtes (changent de type au cours de leur fonctionnement)
* neurones à états finis (ce sont en fait des automates cellulaires, ou machines à états finis (FSM))
* neurones stochastiques (e.g. on applique une fonction linéaire aux entrées du neurones puis on effectue une mesure, i.e. une projection sur une des sorties possibles ; ou alors le neurone possède un degré de liberté interne, comme un spin, qui évolue avec un terme de bruit et un terme de couplage avec les entrées)
* neurones non commutatifs (une permutation des entrées donne une sortie différente, même à poids synaptiques tous égaux)
* neurones d'ordre supérieur (arité strictement supérieure à 2)

Contrairement aux types sensoriels et moteurs, un neurone ne possède qu'un seul type fonctionnel à la fois.
Les neurones sont organisés en un réseau dynamique dont l'architecture initiale et les lois d'évolution sont encodées génétiquement.

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

The abbreviation CSS stands for "Cascading Style Sheets".

*[CSS]: Cascading Style Sheets

### Cite Tag

"Code is poetry." ---<cite>Automattic</cite>

### Code Tag

You will learn later on in these tests that `word-wrap: break-word;` will be your best friend.

### Strike Tag

This tag will let you <strike>strikeout text</strike>.

### Emphasize Tag

The emphasize tag should _italicize_ text.

### Insert Tag

This tag should denote <ins>inserted</ins> text.

### Keyboard Tag

This scarcely known tag emulates <kbd>keyboard text</kbd>, which is usually styled like the `<code>` tag.

### Preformatted Tag

This tag styles large blocks of code.

<pre>
.post-title {
  margin: 0 0 5px;
  font-weight: bold;
  font-size: 38px;
  line-height: 1.2;
  and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
}
</pre>

### Quote Tag

<q>Developers, developers, developers&#8230;</q> &#8211;Steve Ballmer

### Strong Tag

This tag shows **bold text**.

### Subscript Tag

Getting our science styling on with H<sub>2</sub>O, which should push the "2" down.

### Superscript Tag

Still sticking with science and Isaac Newton's E = MC<sup>2</sup>, which should lift the 2 up.

### Variable Tag

This allows you to denote <var>variables</var>.
