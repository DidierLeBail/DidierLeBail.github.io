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
We want to build a general artificial intelligence, which would be able to collaborate with human researchers to help them solving or asking scientific questions.

## Basic requirements
To achieve this goal, this clever agent needs to be able to discuss with humans, as well as sharing some human emotions like empathy or the sake for cooperation.
Thus, the agent must be familiar with cooperative social interactions and natural language.
Also it must build intuitive core knowledge about physics of our world, as this intuition is crucial to researchers to tackle difficult problems.

## How we do it
We consider a population of 100 or less agents [immersed](/embodiement) in the [Minecraft](https://minecraft.wiki/) world.

Each agent has a physical body and a [neural network](/neural_network).
This network takes sensory information as input and returns motor commands as outputs.

There are two types of sensory information: internal and external.
External information we consider gather visual RGB images and 3D auditive signal.
Internal information gather life points, oxygen points, inventory, age and food level.
Motor commands gather body displacement, item use, item drop, item craft, acting on the world, chatting and coopulating.

The population of agents is evolved through a [genetic algorithm](/genetic_algo).
Indeed, a gradient-based approach is impossible for three reasons:
* no cost function is known, whose minimization would imply general intelligence
* the neural networks we consider contain loops
* we include non-differentiable neurons in our network (although it may be possible to get differentiability back by considering each neuron as a continuous mixture of available types: the cost function should be differentiable with respect to the mixture coefficients)
Moreover, a gradient-based approach demands more computational resources than a genetic algorithm (to check actually) as the dimension of the search space grows to infinity, which is clearly the case if we allow neural diversity, variable architecture and variable learning rules.

Agents are free to copulate (pairwise coopulation) whenever they want to, on condition that they are close enough from each other.
Copulating takes resources (food level) and if both agents do have the required resources, the copulation does not lead to any birth.
Two selection pressures are applied to the population in order to bias the genetic search towards general intelligence:
The first one is implicit and always active ; it is survival in the world of Minecraft.
The second one is explicit and most of the time inactive ; it is an exam similar to an intelligence test.
Making progress from one exam session to the other increases the agent's degree of fertility, whereas making worse decreases it.

