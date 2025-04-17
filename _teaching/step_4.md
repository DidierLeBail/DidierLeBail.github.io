---
title: "step 4: the artificial brain"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/step_4
venue: "University 1, Department"
date: 2025-04-16
location: "Gottingen, Germany"
---

We describe here what steps to follow in order to build an artificial brain.

# brain
What functional types of neurons should be implemented?

## neural functional types (semantics of flowing information)
To implement a complex algorithm, a computing system should be able to do the following:
- stop a computation given some signal (in a neural network, it could mean shut down a group of neurons or shut down neurons along a path of activation): it is useful e.g. implement an if else statement or an assert statement
- pause and resume a computation (given some signal)
- add context to adapt a computation
- keep history to eventually revert back to a previous step of the computation or recycle the results of a previous computation

## use of neural circuits
- combining already existing algorithms to produce new ones should be possible. In a neural context, this may mean that a neural circuit should be reused by others (algorithm modularity)
- algorithms should be general, meaning that the same algorithm covers many use cases (for example an implementation of addition works for any pair of integers). In a neural context, this may mean that a neural circuit should be used in as many sensory contexts as possible
- algorithms should be possible to modify given context. In a neural context, this may mean that plasticity should be modulated


Heading 1

Heading 2
======

Heading 3
======
