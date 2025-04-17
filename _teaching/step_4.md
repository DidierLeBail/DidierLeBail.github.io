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

# goal: what we want our computing system to realize
We want out computing system to emulate general intelligence.
To do this, it must beforehand satisfy the following prerequisites:
- no characteristic scale in space, time or complexity (scale invariance)
- modularity
- generality
- care for laziness
- the more information it contains, the easier it absorbs new information

Said otherwise, as a computing system, our artificial brain should be able to implement any algorithm, save resources to run these algorithms more efficiently and memorize an arbitrary amount of information.
Ideally, a general intelligence will memorize everything, recognizing any pattern, able to exploit these patterns to perform any task with minimum use of resources, and able to display open-ended novelty in behavior or ideas.
Importantly, a general intelligence is able to step back (e.g. dramatically change its world model or way of thinking) and constantly improves on any of the aforementioned properties (novelty, sparing resources, memorizing, etc).
Lastly, a general intelligence is able to model its own behavior as well as modify selectively any specific aspect of it, which makes it able to learn how to improve itself faster.

These properties are not possible to implement with traditional current deep learning models, so we have to build our own: the artificial brain.



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

