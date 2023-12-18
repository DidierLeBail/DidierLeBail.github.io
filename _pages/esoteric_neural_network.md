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

Let us summarize in which context arise typical neural networks.
First, we face a problem for which we do not know any solution.
Instead of finding this solution, we design an algorithm that will find it.
Said otherwise, we seek an algorithm that, given an object, returns an algorithm that generates this object.
In a deep learning approach, the seeking algorithm is stochastic gradient descent and the solution is a trained neural network.
Here, the training consists in finding a good solution among a parametrized set of candidates.
Each of these candidates is a neural network with different weights on their edges.
Viewed as algorithms, each neural network always terminates, which is a desirable property for a possible solution.
The parametrization of this space of algorithms allows to reduce the search to the minimization of a real-valued differentiable function on an Euclidian space of finite dimension.

Said otherwise, the trick was to consider a sufficiently wide set of algorithms, so that at least one of them is a good solution to our problem.
Additionally, this set has a structure which makes possible to _find_ that good solution.
For example, the search would be hopeless if we had consider the set of all algorithms.

Then, the question is:
how large can we choose the search space, so that we are still able to find a good solution?

Let us denote by $E$ the set of algorithms, among which we seek a solution to our problem.
What is the most general structure that we need to put on $E$, so that learning is still possible?
By learning is possible, we mean there exists a computable algorithm that finds increasingly good solutions faster than Monte-Carlo search.

Actually, we would like this searching algorithm to itself improve with time.
Consider life for example.
Life exhibits hierarchical learning:
at the first level is running a genetic algorithm.
Individuals produced by this algorithm are themselves learning algorithms.
But these algorithms themselves can greatly improve their way of learning!

This is in sharp contrast with the neural networks and training methods used today.
Indeed, we are used to think inside a given well-defined framework.
However, in biological learning, this very framework is part of the learning process!

How to appraise learning at such an abstract level?

