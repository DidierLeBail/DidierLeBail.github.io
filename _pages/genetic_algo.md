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
[Lamarckian evolution](https://en.wikipedia.org/wiki/Lamarckism), [epigenetics](https://en.wikipedia.org/wiki/Epigenetics) and sexual selection.

The latter solution is the easiest to implement:
recall that our agents are free to choose their mating partners.
As every agent is distinguishable from one another, there is the possibility that the wish for the ideal partner will emerge, meaning that agents will become selective in their mating choices.

We will discuss the implementation of the two other solutions later, because at this stage we lack of material.
Another important point -and easier to deal with right now- in a genetic algorithm is the encoding and decoding problem.
In Nature, we have the separation between a genotype (roughly strings) and a phenotype (the individual produced by a string).
The genetic operators like cross-over or mutations are applied to the genotype.
To evaluate how efficient a genotype is, we need first to compute its phenotype and then immerse it into an environment.
In particular, at environment fixed, two genotypes outputting the same phenotype will have the same fitness value.
It is thus important that every phenotype is equally likely in the genotype space:
the inverse image of the map genotype to phenotype should have a cardinal similar for every phenotype.
If phenotypes are much unbalanced, the evolution process would have a hard time finding a genotype that produces a not-dominant phenotype.
But here is the point: we have no way to know _a priori_ whether or not every phenotype is equally likely, or even better, whether interesting phenotypes are more likely.

Taking a step back, we have a bunch of parameters (genotype) that we input to a program (decoding process) to obtain another bunch of parameters (phenotype).
Why should we spend time and energy to design an elaborate decoding process?
For example, we could use what is called a direct encoding.
It consists in the genotype identified with the phenotype, i.e. the decoding process is the identity map.
Let us test this approach in the case of neural networks.
A genotype will be the data, for each neuron in the network, of its internal parameters, the identity of the neurons from which it receives inputs, and the identity of the neurons to which it sends outputs.
The genotype includes also the parameters (typically the weight) of each synapse existing in the network.

The first observation is an obstacle to scaling:
the genotype has the same size as the phenotype, but we would like to evolve large phenotypes.
This results in a very large search space (the space of genotypes), in which it will be difficult to find a good solution.
Actually, we should keep in mind that the only effective searches are searches in small spaces.
If you are given a large space, you should find a way to restrict your search as much as possible.
In a general setting, you might try hierarchical search:
you start with large steps in your space, eventually dismissing large regions of it, then exploring with finer steps the remaining regions.
However, this works only if the impression you had with large steps confirms with the smaller steps:
it could be that the solution is located in one of the large regions you have dismissed at first!
Being able to step back is thus crucial if you want our search to be effective:
diversity should be boosted as soon as all individuals perform similarly.

The second observation is the large number of steps needed to find a good solution with a direct encoding.
The mutation of one parameter of the genotype will lead to the modification of one parameter of the phenotype.
Imagine that the weight of a single synapse has changed in your brain.
What happens then?
Most likely nothing at all.
However, if you change a single nucleotide in your DNA, you may get phenotypes ranging from sane to unviable.
Yet this is not true for every nucleotide:
mutating some will not cause any significant changes at the phenotype level.
We see that in Nature, the phenotype search is made simultaneously at different scales, which speeds up the search greatly and facilitates diversity.
Note however that large scale search has a price:
it produces some unfit individuals (typically genetic diseases).

The two observations we have made point toward the same concepts of hierarchy and modularity.
In Nature, this is implemented in part by the separation of the decoding process in successive phases:\
DNA $&rarr;$ RNA $&rarr;$ peptids $&rarr;$ proteins $&rarr;$ cells $&rarr;$ organs $&rarr;$ organism\
This allows to break down the difficult task of synthesizing a complex organsim into a succession of more tractable tasks.
It is very reminiscent of deep networks:\
Although in theory, one hidden layer is enough to interpolate any function, in practice it is much more efficient to train a neural network with multiple layers.
After training, each of these layers appears to perform a relatively simple task.\
Hence, to be able to generate highly complex phenotypes, it might be worth to consider a sequential decoding process, with different chromosomes associated to each phase.

## decoding structure suited to the generation of neural networks

To generate a neural network in a sequential way, we could for example build the topology, i.e. a set of nodes and undirected edges.
In a second phase, we differentiate neurons in the various types described in [this page](/neural_network).
Then we make the edges directed and add weights on them.
In a final phase, we tune the internal parameters of the neurons and eventually correct the topology of the network.
To perform all of this, we need a programming language.\
What is the simplest algorithm that generates a network?\

### first step: simplest algorithmic generation process


## basic epigenetics

PASS

Three aspects of our agents' neural networks are subject to genetic evolution:
1. the initial architecture
2. the plasticity rules at fixed architecture
3. the rules for changing the architecture (making or removing connections between neurons, introduction or removal of neurons in the network, etc)

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




