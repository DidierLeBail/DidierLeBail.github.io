---
permalink: /neural_network
title: "Neural network"
author_profile: true
---

Each agent has a distinct neural network.
This neural network can be seen as an algorithm that takes sensory information as input and returns motor commands as outputs.
These outputs depend also on previous inputs in time, so that it is simpler to think of a neural network like a black box or a computer that continously receives a time flow of inputs and continously spits a time flow of outputs, nearly anything being possible in-between.
In a nutshell, a neural network is the representation of a function or a program as a graph, where nodes output a function of the inputs they receive from other nodes or from an external source.
Neurons receiving data from an external source compose the input layer of the network, while neurons sending data to an outer receptor compose the output layer.
For a more involved introduction to neural networks, read [this page](https://en.wikipedia.org/wiki/Neural_network) from Wikipedia.
<!-- If you have already read the [Wikipedia](https://en.wikipedia.org/wiki/Neural_network) page about neural networks, or are familiar with the concept, and still asking yourself what a neural network is in a more abstract language, you might slip over to this [link](/esoteric_neural_network). -->

Although in theory, any kind of computation is possible at the nodes of a neural network, in almost every use case, these computations take the form of arithmetic operations on real numbers.
This may be seen as a limitation, but in practice it often enables differentiability of the network, i.e. tracing back the parameters responsible for a lack of performance and updating them.
However, since we made the choice of a non-differentiable computing system, restricting ourselves to arithmetic operations is not a strong requirement anymore.
Indeed, building a computing system based on arithmetic operations only may require a huge number of parameters to obtain some functions like long-term memory, the ability to perform mental computations, etc.
Given we want to simulate a population of 100 agents, we pay attention to minimize the computational cost of simulating one agent.
As a consequence, we use hybrid computing systems, parts of them consisting in a neural network and parts of them consisting in imperative code.
For example, a calculator is part of the agent's brain. This calculator receives neural signals that are converted in instructions (let us say 1+2).
The computation is performed by the calculator whose output (3 in our example) is converted into a time serie of 0 and 1, so that the neural component of the brain can handle it.
The interface between the calculator and the other components of the brain is let to evolution, both genetic and during the agent's life time.
We use various other non-neural components to interface with an agent's brain, but let us now focus on the neural component.

The neural network is characterized by three properties:
* neural diversity: many types of neurons cohabit in the same brain, which we hope allow to reduce the computational cost of the whole
* plasticity: connexions between neurons can evolve during the life course of the agent
* the plasticity rules are not fixed by the hand of the programmer, but are rather decoded from the genome
* unconstrained topology:
    * self-loops, i.e. a neuron firing to itself, are allowed
    * multiple edges from one neuron to another (parallel edges) are also allowed
    * edges are directed and weighted
    * a neuron can have no inputs (in-neighbours)
    * the requirements for the topology of a network are the following:
        * every neuron has at least one output (out-neighbour)
        * for every input neuron, there exists at least one path from that neuron to an output neuron
        * for every output neuron, there exists at least one path from an input neuron to that neuron

## Neuron
A neuron is a causal process taking as input a multivariate temporal serie and outputting a univariate temporal serie.
Said otherwise, a neuron processes some temporal streams of information, while outputting another.
A neuron can be represented as a one-node directed graph, with one out-edge and an arbitrary number of in-edges.
Generally, the information processing in a neuron is separated in three steps:
* aggregation or pre-processing step: usually it is the conversion of the multi-dimensional input into a scalar one, e.g. $(w_{i}x_{i})_{i}&rarr;b_i+\sum_i w_i x_i$ or $(w_i x_i)_i&rarr;\max_i(w_i x_i)$
* update, if any, the state variables: e.g. for a biological neuron, state variables include membrane potential or concentrations of ions
* deduce the output from the state variables: in most artificial neurons, it is done through the use of an activation function, e.g. a ReLu or a sigmoïd (most generally a non-polynomial operator)

## Neural types
We distinguish between two types:
(1) functional types, which include input neurons, output neurons and interneurons, and (2) structural types, which describe how the neuron is processing its inputs.

A neuron can have multiple functional types but has only one structural type.
For example, a neuron can be both a sensory neuron and a motor neuron.

Sensory neural types separate into two families: internal and external.
External sensory types comprise neurons sensitive to light and neurons sensitive to sound.
Internal sensory types comprise neurons sensitive to life points, neurons sensitive to oxygen points, inventory, age and food level.
Motor types gather neurons involved in body displacement, item use, item drop, item craft, chatting, copulating and acting on the world (mining, pushing a button, taking an object on the ground, etc).

For now, we have identified 7 structural neural types to implement in our networks.
We think neural diversity is crucial because it allows to save computational resources, as well as reducing the total number of neurons and connections used.
Indeed, distinct neural types perform distinct kinds of computation, as well as have distinct computational costs.
For example, a XOR operation requires three perceptron neurons (we exclude the two input neurons) to be implemented, while only one biological neuron is enough: [12:10](https://www.youtube.com/watch?v=hmtQPrH-gC4&t=1s&ab_channel=ArtemKirsanov).

Conversely, a convolutional neural network with 5 up to 8 layers of ReLu actived neurons is needed to simulate accurately a single biological neuron.
However, the neural network equivalent of the latter is 2000 faster at execution time than the detailed system of differential equations used to modelize the biological neuron.
Thus, it would be of great use to build a map between structural types, defining $N(A&rarr;B)$ to be the minimal network made of neurons of type A that emulates a single neuron of type B.
Then both types A and B should be considered if $N(A&rarr;B)$ has a greater computational cost than B and $N(B&rarr;A)$ has a greater computational cost than A.

Here are the 7 structural types we have identified so far:
* perceptron: no internal state, deterministic activation function (sigmoid, ReLu, Heaviside, etc)
* temporal: the output is a function of the internal state, whose derivative is a function of the neuron inputs. An example of such neuron is the [integrate-and-fire model](https://neuronaldynamics.epfl.ch/online/Ch6.S1.html).
* boolean: the output is a [boolean function](https://en.wikipedia.org/wiki/Boolean_function) of the inputs
* stochastic: the output is a random variable. The simplest example of such neuron is obtained by considering the activation function as returning a probability to fire.
* ordered: usually, a neuron takes as input the biased aggregation of its inputs, i.e. the number $b_{i}+\sum_{i}w_{i}x_{i}$. However, this aggregation is actually a pre-processing step that is part of the neuron's computation, and other pre-processing steps could be imagined. One of the simplest is to return the maximum value, i.e. the number $\max_{i}(w_{i}x_{i})$. Another possibility is to return a vector instead of a number. This allows the neuron to distinguish between its inputs, resulting in a distinct output when two inputs are swapped with another, even in the case of equal synaptic weights. One simple implementation of this is to return the vector $(w_{i}x_{i})_{i}$ after the pre-processing step.
* rewriter: the output is the result of rewriting rules applied to the input viewed as a string of 0 and 1. Intermediate symbols can be introduced and terminal symbols are alias versions of the 0 and 1 (the output of this neuron is also a string of 0 and 1 so to avoid confusing the starting symbols 0 and 1 with the terminal symbols, we introduce aliases).
* transitory: the neuron has a structural type other than transitory that can change according to specified rules

## Plasticity
The plasticity of a computing system is its ability to adapt to perform either (1) the same task with fewer computational resources or (2) to perform a new task without forgetting its current abilities.
In a neural network, plasticity can involve changes in _topology_, e.g. the creation/removal of new synapses or neurons, _parameters_, e.g. the modification of synaptic weights or neural parameters, or _resources_, e.g. the shut down of some brain area in order to save computational resources.

Together, these three forms of plasticity aim at saving resources so that the simulation of larger brains is viable, avoiding catastrophic forgetting by e.g. freezing parameters of some neural circuits, allocating more resources to brain areas selected depending on the context, which may allow for higher performance.

### parameters
The modification of real-valued parameters is ensured via a neuromodulated version of Hebb-like rules, taking account recent findings such as [heterosynaptic plasticity](https://en.wikipedia.org/wiki/Heterosynaptic_plasticity), [synaptic tagging and other mechanisms](https://en.wikipedia.org/wiki/Metaplasticity).

Besides these, we seek to implement a context-dependent parameter sharing mechanism, which would allow to reduce the total number of parameters.
Parameter sharing has proven efficient e.g. in convolutional neural networks, and we try here to generalize this idea so that which parameters to share is left to the brain's decision, depending on genetic factors and life-course evolution.

### topology
The guiding principle we lean on to propose an evolving topology is to avoid both over-and under-exploitation of neurons and synapses.
Thus, frequently used neurons should develop new connections to share computational load.
As introducing new neurons is costly, a neuron may first look around for an existing partner in under-exploited regions, in hope they become useful again.
One possiblity to enchance the search is to restrict among neural under-exploited neural hubs (a neuron connected to many others) and their neighbours.
If this search fails, new neurons can be added to highly activated regions, so that more resources are allocated to the regions that do most of the computations.

In order to identify neural hubs or under and over-exploitation, a data base about the brain components has to be updated.
Relevant measures include node centrality of neurons, degree, number of saturated synapses per neuron (meaning the synaptic weight has reached its maximal value), etc.
Note that knowledge of transport networks or YouTube recommondation algorithms may be helpful in designing an efficient topology plasticity, as they face similar challenges.

### resources
In the case the brain takes too many resources, it may become inefficient at processing information.
Then it is necessary to decrease the level of activity.
However, doing it at random is not a good idea, as it could shut down areas that are relevant to the on-going task.
Hence, we are trying to put in place a selective shut down process, where the choice of which neurons to shut down is either the result of modulator neurons or an heuristic implemented in imperative code.
In either way, knowledge of distributed computing systems, brain irrigation or public power network may be critical to achieve this goal.
