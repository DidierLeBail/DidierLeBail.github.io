---
permalink: /genetic_algo
title: "Genetic algorithm"
author_profile: true
---

The genetic algorithm we use allows the agents to become better at learning across generations.
Since we consider a combination of genetic search and individual learning, this algorithm is qualified as a [memetic algorithm](https://en.wikipedia.org/wiki/Memetic_algorithm).

What requirements must be satisfied by our memetic algorithm, in order to achieve open-ended evolution all the way up to general intelligence?
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
the inverse image of the map genotype to phenotype should have a similar cardinal for every phenotype.
If phenotypes were much unbalanced, the evolution process would have a hard time finding a genotype that produces a not-dominant phenotype.
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
Being able to step back is thus crucial if you want your search to be effective:
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

## decoding structure suited to the generation of our neural networks

To generate a neural network in a sequential way, we could for example build the topology, i.e. a set of nodes and undirected edges.
In a second phase, we differentiate neurons in the various types described in [this page](/neural_network).
Then we make the edges directed and add weights on them.
In a final phase, we tune the internal parameters of the neurons and eventually correct the topology of the network.
To perform all of this, we need a programming language.

In a generic setting, such a language can be viewed as a [context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar).
In a nutshell, it is the data of symbols and rewriting rules of the form:\
single symbol $&rarr;$ string of symbols

Those rules can be themselves concantenated into a single string, called the chromosome describing our grammar.
However, designing a grammar is not enough to generate a network.
Now we have to write an algorithm, i.e. a [syntactic tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) respecting the rules of our grammar that outputs the desired network.

This tree indicates which rewriting rules among the available ones in our grammar we pick at each stage of the network generation process.
The syntactic tree itself is also part of the genotype, as a chromosome separated from the one encoding the grammar.

Multiple grammars and trees can be stacked upon each other, the only condition being that the terminal symbols of the grammar at one layer are starting symbols for the grammar associated to the next layer.
This way, the segmentation of the whole decoding algorithm in a succession of simpler algorithms is successfully achieved.
Moreover, this structure can be generalized in a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph#:~:text=A%20directed%20acyclic%20graph%20is,a%20path%20with%20zero%20edges) in place of a linear sequence of layers.
Note however that using completely generic grammars is unlikely to give rise to an efficient decoding system ; the grammar of some layers must be designed by hand with care, then layers with generic grammars can be added at wish.
The layers whose grammar has been designed by hand are called the main layers.

Before we specify the main layers, let us recap the current genotype structure.
One part of it is named "DNA-like part", or "coding DNA" by analogy with Nature.
This part, that we will specify later, is sent as input to the decoding process.
The remaining genotype is split in two parts:
one codes for the decoding system, i.e. specifies the step-by-step construction of a neural network out of the DNA-like part of the genotype.
The genotype of the decoding system consists in a collection of layers (L<sub>1</sub>,...,L<sub>n</sub>), where L<sub>i</sub> takes the output of L<sub>i-1</sub> as input for $i\geq1$.
The first layer L<sub>1</sub> takes the DNA-like genotype as input and the last layer L<sub>n</sub> returns the neural network.
For any $1\leq i\leq n$, L<sub>i</sub> contains a syntactic tree if it is a main layer, and both a grammar and a syntactic tree else.
The third and last part of the genotype codes for the mutating system, i.e. specifies how to combine two genotypes with one another to yield two newborn genotypes.

## design of the main layers
Recall that the genotype is supposed to code for four structures:
1. the initial architecture
2. the plasticity rules at fixed architecture
3. the rules for changing the architecture (making or removing connections between neurons, introduction or removal of neurons in the network, etc)
4. the mutating system

However, for the sake of clarity, we will first consider the initial architecture as the whole phenotype that we want to synthesize.
We will refer to this partial genotype as genotype of level 1.
Then the genotype that we are interested in, which codes for the four structures, will be referred to as the genotype of level 4.

## level 1
The genotype of level 1 codes only for a high-level description of the initial architecture, which will be completed by local rules of evolution in the genotypes of levels 2 and 3.
The simplest way to build a network from such a high-level description is to use one of the various available libraries specialized in the generation of complex networks.
In our case, we will use some functions and objects from the [Python](https://www.python.org/) library [NetworkX](https://networkx.org/), thus defining a language in which algorithms can be written.
To improve the flexibility of this choice, we make the vocabulary of this language adaptive by allowing code blocks to be named as an elementary operator.
Those code blocks are selected as sub-trees of the syntactic tree that represents the algorithm generating the network.
They are selected, evolved and removed from the vocabulary by the genetic operators we will introduce in the mutating system section below.



## mutating system
Another important part of a genetic algorithm is how to produce new candidates.
For example, with random mutations, it is likely that most of the candidates will be dismissed, maybe even not viable.
Thus it is important to go beyond random mutations, and to develop a non-trivial mutation procedure.
Such a system should be composite:
* a generator that produces genotypes that are maximally different from every genotype ever tested
* a corrector that corrects those genotypes to avoid lethal genetic diseases

## basic epigenetics
What we call epigenetics are feedback loops from the phenotype to the genotype.
One loop results from sexual freedom, which allows the agents to decide by themselves which genetic combinations should constitute the next generation.
In addition to this loop, some piece of information should be explicitly transmitted from the phenotype of the parent to the phenotype of the child, so that the initial state of the newborn neural network does not result purely from genetic decoding.
We introduce to this end two functional types of neurons:
(1) ferry neurons and (2) trustee neurons.
As the names suggest, the ferry neurons of the mother will output signals to the trustee neurons of the child during the first stage of the child's development (see the [description of the agents](/agents)).

A future improvement would be that some part of the brain sends also signals to the mutating system, helping it explicitly to find promising mutations.
For example, some neurons could build a string of a limited number of characters during the life of the agent, and this string could be sent as one of the symbolic inputs to the mutating system.
To limit errors in the string, the editor neurons should be informed back of the string content at any time of the agent's life, so that they have the possibility to correct it.
