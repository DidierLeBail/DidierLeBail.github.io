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
To achieve this goal, this clever [agent](/agents) needs to be able to discuss with humans, as well as sharing some human emotions like empathy or the sake for cooperation.
Thus, the agent must be familiar with cooperative social interactions and natural language.
Also it must build intuitive core knowledge about physics of our world, as this intuition is crucial to researchers to tackle difficult problems.

## How we do it
We consider a population of 100 or less agents immersed in the [Minecraft](https://minecraft.wiki/) world.\
We think embodiement offers important advantages:
* more suited to develop intuitive knowledge about physics
* data have only a few types: sensory (auditive, visual, etc) or motor ; then the same agent can handle any problem immersed in the same world. This is in contrast with non-embodied algorithms, which are wired to receive only numbers or images as input: depending on the problem, their input and output layers need to be re-defined.
* active learning: agents are able to act on the world to design experiences in order to discriminate between models of their world

In addition to their body, each agent has a [neural network](/neural_network).
This network takes sensory information as input and returns motor commands as outputs.
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

Agents are free to copulate (pairwise coopulation) whenever they want to, on condition that they are close enough from each other.
Copulating takes resources (food level) and if both agents do have the required resources, the copulation does not lead to any birth.
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
* hierarchy, multi-stage: any complex process should be decomposed as a DAG of simpler intermediate processes

