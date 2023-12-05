---
permalink: /neural_network
title: "Neural network"
author_profile: true
---

Each agent has a distinct neural network.
This network is characterized by three properties:
* neural diversity
* plasticity: connexions between neurons can evolve during the life course of the agent (note that self-loops, i.e. a neuron firing to itself, are allowed)
* the plasticity rules are not fixed by the hand of the programmer, but rather are decoded from the genome

## Neural types
We distinguish between two types:
(1) functional types, which include input neurons, output neurons and interneurons, and (2) structural types, which describe how the neuron is processing its inputs.

A neuron can have multiple functional types but has only one structural type.
For example, a neuron can be both a sensory neuron and a motor neuron.

Sensory neural types separate into two families: internal and external.
External sensory types comprise neurons sensitive to light and neurons sensitive to sound.
Internal sensory types comprise neurons sensitive to life points, neurons sensitive to oxygen points, inventory, age and food level.
Motor types gather neurons involved in body displacement, item use, item drop, item craft, chatting, coopulating and acting on the world (mining, pushing a button, taking an object on the ground, etc).

For now, we have identified 8 structural neural types to implement in our networks.
We think neural diversity is crucial because it allows to save computational resources, as well as reducing the total number of neurons and connections used.
Indeed, distinct neural types perform distinct kinds of computation, as well as have distinct computational costs.
For example, a XOR operation requires three perceptron neurons (we exclude the two input neurons) to be implemented, while only one biological neuron is enough: [12:10](https://www.youtube.com/watch?v=hmtQPrH-gC4&t=1s&ab_channel=ArtemKirsanov).

Conversely, a convolutional neural network with 5 up to 8 layers of ReLu actived neurons is needed to simulate accurately a single biological neuron.
However, the neural network equivalent of the latter is 2000 faster at execution than the detailed system of differential equations used to modelize the biological neuron.

Thus, it would be of great use to build a map between structural types, defining $N(A&rarr>B)$ to be the minimal network made of neurons of type A that emulates a single neuron of type B.


## Plasticity

Il existe pour le moment 8 types fonctionnels:
* neurones artificiels (sans mémoire, avec fonction d'activation de type sigmoïde ou ReLu)
* neurones temporels (avec état interne donnant une mémoire, avec fonction d'activation de type Heaviside)
* neurones binaires (combinant ou superposant des opérations binaires de ses entrées, e.g. AND, OR, XOR, etc.)
* neurones mixtes (changent de type au cours de leur fonctionnement)
* neurones à états finis (ce sont en fait des machines à états finis (FSM))
* neurones stochastiques (e.g. on applique une fonction linéaire aux entrées du neurones puis on effectue une mesure, i.e. une projection sur une des sorties possibles ; ou alors le neurone possède un degré de liberté interne, comme un spin, qui évolue avec un terme de bruit et un terme de couplage avec les entrées)
* neurones ordonnés (une permutation des entrées donne une sortie différente, même à poids synaptiques tous égaux)
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
