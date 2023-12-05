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

## Neuron
A neuron is a causal process taking as input a multivariate temporal serie and outputting a univariate temporal serie.
Said otherwise, a neuron processes some temporal streams of information, while outputting another.
It can be represented as a one-node directed graph, with one out-edge and an arbitrary number of in-edges.
Generally, the information processing in a neuron is separated in three steps:
* aggregation or pre-processing step: usually it is the conversion of the multi-dimensional input into a scalar one, e.g.
* update, if any, the state variables
* deduce the output from the state variables: usually it is done through the use of an activation function

$(w_{i}x_{i})_{i}&rarr;b_{i}+\sum_{i}w_{i}x_{i}$ or $(w_{i}x_{i})_{i}&rarr;\max_{i}(x_{i})$

## Neural types
$w_{i}$
We distinguish between two types:
(1) functional types, which include input neurons, output neurons and interneurons, and (2) structural types, which describe how the neuron is processing its inputs.

A neuron can have multiple functional types but has only one structural type.
For example, a neuron can be both a sensory neuron and a motor neuron.

Sensory neural types separate into two families: internal and external.
External sensory types comprise neurons sensitive to light and neurons sensitive to sound.
Internal sensory types comprise neurons sensitive to life points, neurons sensitive to oxygen points, inventory, age and food level.
Motor types gather neurons involved in body displacement, item use, item drop, item craft, chatting, coopulating and acting on the world (mining, pushing a button, taking an object on the ground, etc).

For now, we have identified 6 structural neural types to implement in our networks.
We think neural diversity is crucial because it allows to save computational resources, as well as reducing the total number of neurons and connections used.
Indeed, distinct neural types perform distinct kinds of computation, as well as have distinct computational costs.
For example, a XOR operation requires three perceptron neurons (we exclude the two input neurons) to be implemented, while only one biological neuron is enough: [12:10](https://www.youtube.com/watch?v=hmtQPrH-gC4&t=1s&ab_channel=ArtemKirsanov).

Conversely, a convolutional neural network with 5 up to 8 layers of ReLu actived neurons is needed to simulate accurately a single biological neuron.
However, the neural network equivalent of the latter is 2000 faster at execution than the detailed system of differential equations used to modelize the biological neuron.
Thus, it would be of great use to build a map between structural types, defining $N(A&rarr;B)$ to be the minimal network made of neurons of type A that emulates a single neuron of type B.
Then both types A and B should be considered if $N(A&rarr;B)$ has a greater computational cost than B and $N(B&rarr;A)$ has a greater computational cost than A.

Here are the 6 structural types we have identified so far:
* perceptron: no internal state, deterministic activation function (sigmoid, ReLu, Heaviside, etc)
* temporal: the output is a function of the internal state, whose change is a function of the neuron inputs. An example of such neuron is the [integrate-and-fire model](https://neuronaldynamics.epfl.ch/online/Ch1.S3.html).
* boolean: the output is a [boolean function](https://en.wikipedia.org/wiki/Boolean_function) of the inputs
* stochastic: the output is a random variable. The simplest example of such neuron is obtained by considering the activation function as returning a probability to fire.
* ordered: usually, a neuron takes as input the biased aggregation of its inputs, i.e. the nunmber $b_{i}+\sum_{i}w_{i}x_{i}$. However, this aggregation is actually a pre-processing step that is part of the neuron's computation, and other pre-processing steps could be imagined. One of the simplest is to return the maximum value, i.e. the number $\max_{i}(w_{i}x_{i})$. Another possibility is to return a vector instead of a number. This allows the neuron to distinguish between its inputs, resulting in a distinct output when two inputs are swapped with another, even in the case of equal synaptic weights. One simple implementation of this is to return the vector $(w_{i}x_{i})_{i}$ after the pre-processing step.
* transitory: the neuron has a structural type other than transitory that can change according to specified rules

## Plasticity
Plasticity is needed for our purpose. It is the ability of the network to change its edges in a dependent way with the stream of inputs it receives.
Plasticity is needed because it allows the agent to adapt to diverse environments, even though
