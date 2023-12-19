---
permalink: /genetic_algo
title: "Genetic algorithm"
author_profile: true
---

The genetic algorithm we use allows the agents to become better at learning across generations.
Since we consider a combination of genetic search and individual learning, this algorithm is called a [memetic algorithm](https://en.wikipedia.org/wiki/Memetic_algorithm).

What requirements must be satisfied by our memetic algorithm, in order to achieve open-ended evolution up to general intelligence?
How elaborate must be the genetic algorithm?
Is it possible that it produces intelligent individuals without having any intelligence?
I believe that it is possible, on condition that the individuals can influence their own process of evolution.
Without this feedback loop, the complexity of the individuals will remain bounded by the complexity of the fixed evolution process.
For the complexity of individuals to grow without bounds, the evolution process itself must be adaptive too.
To endow the evolution process with a form of learning, either it has to be intelligent already, or it has to be boosted by intelligent individuals, here the individuals it produces.
This way, a positive feedback loop can be sustained, with an evolution process producing a bit more intelligent agents, and these agents improving the process at finding still more intelligent agents.
Moreover, the more intelligent the agents are, the better they will be at improving their evolution process.

How to implement this feedback loop?
Inspiring from Nature, at least three solutions are available:
Lamarckian evolution, epigenetics and sexual selection.

The latter solution is the easiest to implement:
recall that our agents are free to choose their mating partners.
As every agent is distinguishable from one another, there is the possibility that the wish for the ideal partner will emerge, meaning that agents will become selective in their mating choices.


Three aspects of our agents' neural networks are subject to genetic evolution:
1. the initial architecture
2. the plasticity rules at fixed architecture
3. the rules for changing the architecture (making or removing connections between neurons, introduction or removal of neurons in the network, etc)

Although this is not yet implemented, we would like to consider Lamarckian learning, meaning that some skills that an agent learns through his life are transferred back to the genome of his offspring.

The key aspects of our memetic algorithm are the following:
* complexification (we start from simple phenotypes, then increasingly complex)
* speciation to preserve innovations
* Lamarckian learning and epigenetics
* the evolution strategy is itself subject to evolution


## coding the architecture
pass

## coding the plasticity rules
pass

## coding the rules for changing the architecture
pass




