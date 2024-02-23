---
permalink: /
title: "project overview"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## Final goal
We want to build an Artificial General Intelligence (AGI), which would be able to collaborate with human researchers to help them solving or asking scientific questions.

## Basic requirements
To achieve this goal, this clever [agent](/agents) needs to be able to discuss with humans, as well as sharing some human emotions like empathy for the sake of cooperation.
Thus, the agent must be familiar with cooperative social interactions and natural language.
Also it must build intuitive core knowledge about numbers and physics of our world.

## How we do it
We consider a population of 100 or less agents immersed in the [Minecraft](https://minecraft.wiki/) world.\
In addition to their body, each agent is characterized by an artificial DNA.
Agents can copulate, giving rise to new agents by mixing their DNA.
This DNA initializes a [neural network](/neural_network) at the agent's birth, and also stipulates how this network will evolve through the agent's life.
The neural network of one agent takes sensory information as input and returns motor commands as outputs.

As generations follow each other, a selection pressure is applied to the population so that biological intelligence becomes a likely trait.

## Why we do not believe in current mainstream attempts
Currently, the methodology to progress towards AGI is to build huge (1) statistical models with (2) ever-increasing number of parameters and (3) trained on an insanely huge pile of data.
Then the basic procedure is to define a cost function and optimize the model parameters by gradient descent so that to minimize this function averaged on the training data.
After training, the model is frozen: it cannot learn anymore.
The hope is generally that some kind of emergence takes place, which allows the model to generalize efficiently to unseen data without having to be retrained constantly.

What could possibly be wrong with this?

First, statistical correlations cannot be a stand-in for a cognitive model of the world.
It is very easy to prove this.
Consider for example the problem of minimizing the following cost function $L((n,m),y)=(y-n*m)^{2}$
Said otherwise, you want to build a statistical model that performs the multiplication of integers.
Even the largest LLM in the world cannot perform the multiplication of two integers.
Indeed, this task requires learning a deterministic rewriting rule, i.e. an _algorithm_ and not interpolating the _map_, which to two integers associates their product.
There is a theorem, which is probably at least in part responsible for the interpolation hype.
This theorem is called the universal approximation theorem, and states that for most continuous maps between Euclidean spaces, and for any given bounded region of the input space, we can find an arbitrarily good approximation of those maps with neural networks such as those massively used nowadays.
However, one thing that maybe is forgotten is you have no information on how good your neural network approximates a given map outside the training region.
Said otherwise, no result does exist yet on generalization error.
Another point, that may or not be of interest, is that biological brains are far from implementing a continuous map between Euclidean spaces.
Most of interesting features of biological neural networks (object recognition, decision making, mathematical reasoning) are not at all continuous as maps!
This is why I prefer to view a biological neural network as implementing an _algorithm_ rather than a map.

Another example I like to demonstrate how we are overconfident in the dominant approach to AI is to train a neural network to interpolate the cosine function.
It is a one-dimensional and differentiable function, which in principle makes it easy for a neural model to learn.
Hell no, the neural network will _always_ be wrong with an arbitrarily large error outside its training set.
In contrast, a human can draw the same function with less precision than the model on its training set, but with a bounded error anywhere on the real axis.

The number of parameters have nothing to do with the gap of performance between artificial and biological neural networks.
C. Elegans has 302 neurons and does better than Chat GPT.
A fruit fly has 150 000 neurons and shows signs of self-awareness.
With less neurons that the giant current models, insects can learn, understand abstract concepts, navigate and display what it seems like a wide range of emotions, like fear, curiosity, desire or pain.
These emotions allow them to behave in a context-sensitive way, this context including their current inner state.

Said otherwise, it seems that complex cognition does not require giant models.

The way models are trained differ completely from the way biological brains learn.
The latter learn by building some model of the world.
This model is algorithmically simple, which allows it to be built from a few examples.
More importantly, biological brains perform experiments, motivated by curiosity, to confront their models to reality and enrich them iteratively.
When something is not explained by their model, they are able to adapt it rapidly because this model is modular.
Often it is enough to change one module to correct their model.
Moreover, the module to change is identified because biological brains have a high-level understanding of their own models, of how they process information and take decisions or make conclusions.

A neural network has no inner understanding on how it works and their developpers do not have it either.
This makes very difficult the task of improving the performance of a network.
If the neural network had this understanding, training data should not be fed to it in a passive way, but the network would be able to identify the difficult examples and train harder on them.
To develop an autonomous agent, this agent should autonomously learn.
The last problem I will mention is that the performance of a network is measured as an average over a list of examples.
Biological brains are not evaluated that way.
Most of their decisions have irreversible consequences, and above all a biological brain is constantly subject to imminent death.
Hence, doing well in average is of no use for a biological agent.
What counts is to _always_ remaining above a certain threshold (the death threshold for example).
Then a very unlikely situation, which is of no significance for a network, may be of high significance for a biological agent.
Unlikely situations have revealed particularly useful in improving our scientific world models.
If we paid attention only to average performance, science would probably not have made it so far.

My last remark will be about how many neuroscientists think that information is processed in the brain.
A widespread opinion is that _in vivo_ neurons behave stochastically and this randomness is needed.
Without any arguments, I will simply give my own point of view.
Organisms with larger brains contain almost only spiking neurons, whereas smaller organisms can possess continously varying neurons.
So there seems to be an advantage to spiking versus continuous neurons.
For me it is digital vs analog encoding. The former is more prone to errors, while the latter is reliable in a deterministic setting, besides allowing for symbolic computation.
Well, in large brains, small errors become rapidly large so you should use digital encoding.
In small devices or organisms, a small error remains small because it does not propagate much, so analog encoding is possible (and in principle more energy efficient).

So to summarize my point of view on information encoding in the brain, (1) spiking neurons may be more relevant than continuous neurons to implement complex algorithms and (2) the brain is a perfectly deterministic processing machine.

## What reasons do we have to believe that our approach will lead to AGI (and more details on this approach)


We think embodiement offers important advantages:
* more suited to develop intuitive knowledge about physics
* data have only a few types: sensory (auditive, visual, etc) or motor ; then the same agent can handle any problem immersed in the same world. This is in contrast with non-embodied algorithms, which are wired to receive only numbers or images as input: depending on the problem, their input and output layers need to be re-defined.
* active learning: agents are able to act on the world to design experiences in order to discriminate between models of their world


Agents can discuss by posting strings of characters on the chat.
There is no restriction on these characters or the length of the strings.

Inputs to the neural network include visual RGB images and 3D auditive signal, as well as life points, oxygen points, inventory, age and food level.
Motor commands include body displacement, item use, drop and craft, acting on the world, chatting and coopulating.

The population of agents is evolved through a [genetic algorithm](/genetic_algo).
Indeed, a gradient-based approach is impossible for three reasons:
* no cost function is known, whose minimization would imply general intelligence
* the neural networks we consider contain loops
* we include non-differentiable neurons in our network (although it may be possible to get differentiability back by considering each neuron as a continuous mixture of available types: the cost function should be differentiable with respect to the mixture coefficients)
Moreover, a gradient-based approach demands more computational resources than a genetic algorithm (claim to check actually) as the dimension of the search space grows to infinity, which is clearly the case if we allow neural diversity, variable architecture and variable learning rules.

Agents are free to copulate (pairwise copulation) whenever they want to, on condition that they are close enough from each other.
Copulating takes resources (food level) and if both agents do not have the required resources, the copulation does not lead to any birth.
Two selection pressures are applied to the population in order to bias the genetic search towards general intelligence:
The first one is implicit and always active ; it is survival in the world of Minecraft.
The second one is explicit and most of the time inactive ; it is an [exam](/exams) similar to an intelligence test.
This test evaluates core knowledge like intuitive Physics, basic arithmetic, spatial reasoning and the ability to draw basic analogies.
Making progress from one exam session to the other increases the agent's degree of fertility, whereas making worse decreases it.

Between two exam sessions, agents are free to explore their world and/or discuss with each other so that they perform better at the next session.

## Philosophy
Although no formal theory can help us significantly so far to reach user-friendly AGI, important principles have guided us and keep doing so on the long path we have taken.
We believe these principles to be essential for an evolutionary-driven computing system to reach AGI:
* redundancy
* feedback loops: each process should report its outcome
* maximal flexibility: any parameter or rule introduced should be a degree of freedom
* maximal liability: any process should be either adaptive or checked and corrected adaptively
* maximal diversity of computational processes
* hierarchy, modularity: any complex process should be decomposed as a DAG of simpler intermediate processes

