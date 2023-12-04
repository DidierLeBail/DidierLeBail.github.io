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
We consider a population of 100 or less agents immersed in the Minecraft world  [Minecraft](https://minecraft.wiki/).
Embedded intelligence has a lot of advantages:

* more suited to develop intuitive knowledge about physics
* data have only a few types: sensory (auditive, visual, etc) or motor ; then the same agent can handle any problem immersed in the same world. This is in contrast with non-embedded algorithms, which are wired to receive only numbers or images as input: depending on the problem, their input and output layers need to be re-defined.
* active learning: agents are able to act on the world to design experiences in order to discriminate between models of their world, which was not possible in the non-embedded setting.

Each agent has a physical body and a neural network.
This network takes sensory information as input and returns motor commands as outputs.

There are two types of sensory information: internal and external.
External information we consider gather visual RGB images and 3D auditive signal.
Internal information gather life points, oxygen points, inventory, age and food level.
Motor commands gather body displacement, item use, item drop, item craft, acting on the world, chatting and coopulating.

The population of agents is evolved through a genetic algorithm.
Indeed, a gradient-based approach is impossible for three reasons:
* no cost function is known, whose minimization would imply general intelligence
* the neural networks we consider contain loops
* we include non-differentiable neurons in our network (although it may be possible to get differentiability back by considering each neuron as a continuous mixture of available types: the cost function should be differentiable with respect to the mixture coefficients)
Moreover, a gradient-based approach demands more computational resources than a genetic algorithm as the dimension of the search space grows to infinity, which is clearly the case if we allow neural diversity, variable architecture and variable learning rules.

Agents are free to coopulate (pairwise coopulation) whenever they want to, on condition that they are close enough from each other.
Copulating takes resources (food level) and if both agents do have the required resources, the copulation does not lead to any birth.
Two selection pressures are applied to the population in order to bias the genetic search towards general intelligence:
The first one is implicit and always active ; it is survival in the world of Minecraft.
The second one is explicit and most of the time inactive ; it is an exam alike to an intelligence test.
Making progress from one exam session to the other increases the agent's degree of fertility, whereas making worse decreases it.

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

## Markdown guide

### Header three

#### Header four

##### Header five

###### Header six

## Blockquotes

Single line blockquote:

> Quotes are cool.

## Tables

### Table 1

| Entry            | Item   |                                                              |
| --------         | ------ | ------------------------------------------------------------ |
| [John Doe](#)    | 2016   | Description of the item in the list                          |
| [Jane Doe](#)    | 2019   | Description of the item in the list                          |
| [Doe Doe](#)     | 2022   | Description of the item in the list                          |

### Table 2

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|-----------------------------|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=============================|
| Foot1   | Foot2   | Foot3   |

## Definition Lists

Definition List Title
:   Definition list division.

Startup
:   A startup company or startup is a company or temporary organization designed to search for a repeatable and scalable business model.

#dowork
:   Coined by Rob Dyrdek and his personal body guard Christopher "Big Black" Boykins, "Do Work" works as a self motivator, to motivating your friends.

Do It Live
:   I'll let Bill O'Reilly [explain](https://www.youtube.com/watch?v=O_HyZ5aW76c "We'll Do It Live") this one.

## Unordered Lists (Nested)

  * List item one 
      * List item one 
          * List item one
          * List item two
          * List item three
          * List item four
      * List item two
      * List item three
      * List item four
  * List item two
  * List item three
  * List item four

## Ordered List (Nested)

  1. List item one 
      1. List item one 
          1. List item one
          2. List item two
          3. List item three
          4. List item four
      2. List item two
      3. List item three
      4. List item four
  2. List item two
  3. List item three
  4. List item four
