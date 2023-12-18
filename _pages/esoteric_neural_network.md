---
permalink: /esoteric_neural_network
title: "What is a neural network?"
author_profile: true
---

Informally, a neural network is any stochastic computable function mapping a stream of inputs to a stream of outputs.
In the framework of neuroscience, the inputs are called sensory information while the outputs are called motor commands.
The "network" vision comes from the fact that any computing process can decompose into elementary processes that takes some inputs from other processes and return some outputs to other processes.
In particular, any program turns out to be a network.
The "neural" vision implies that the elementary processes going on at each node of the computing netwok take a particular form that offers several advantages over generic programs.
Actually, the programs to which we refer to as "neural networks" are not programs but classes of programs, usually parametrized by floats (numeric approximation of real numbers).

Indeed, we are interested in _learning_ algorithms.
Typically, we face a problem for which we do not know any solution.
Instead of finding this solution, we design an algorithm that will find it.
Said otherwise, we seek an algorithm that, given an object, returns an algorithm that generates this object.
Also, we would like to return the most efficient algorithm as possible, using the least computational resources (time and memory) as possible.

Let us introduce a bit of notations to clarify.
Let us denote by $E$ the set of algorithms, among which we seek a solution to our problem.

Contrary to generic programs, neural networks (1) always terminate and (2) can be trained.
Let us introduce a bit of notations to clarify.
(1) means that
