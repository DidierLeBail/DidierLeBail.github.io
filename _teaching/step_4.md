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

An artificial brain consists in a weighted directed temporal network (with higher-order effects) of elementary computing units called neurons, rules to evolve both the network topology and the parameters of the neurons, a protocol for parasynaptic communication (i.e. communication between neurons that bypass the synaptic network) and a protocol for long-range node-to-node communication in the synaptic network (inspired from the Internet routing protocol and the blockchain algorithm).
Note that parasynaptic communication is equivalent to assume the existence of a second parallel temporal network between neurons.
Importantly, any parameter of an artificial brain is subject to plasticity in a context-dependent way.
Also, there is absolutely no black box within an artificial brain: any intermediate computation within a neuron leaves an impact on the neighbouring neurons.
This choice is inspired from biological brains, where subthreshold fluctuations of the membrane potential are detected by neighbouring neurons and participate to important neural functions (see [this paper](https://www.mdpi.com/2076-3425/13/1/74) and [this paper](https://www.pnas.org/doi/pdf/10.1073/pnas.1716933115)).
Aside from the relevance of this mechanism in biological brains, this choice allows the brain to access the detailed steps of each neuron, allowing it to share variables between different neurons, reuse some intermediate computations and adjust the behavior of a neuron depending on the context, including e.g. the correction of some errors.

For a comparison between brains and in silico computing systems, see [this paper](https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2023.1220030/full).






Note: we do not seek to build a brain-like computing system, but to create a process able to generate such a computing system

Implementing different types of neurons
brain = sensory area + deep brain + motor area
Implement the machine learning vision module (inspire from the DeepMind paper about reinforcement learning and world model, because they know how to handle small images, taking into account every pixel)
Implement the symbolic vision module
implement the retroaction loop btw the sensory modules and the deep brain
Design the motor area
Design the text processing modules
The deep brain:
implement synaptic propagation (neural functional roles, aggregation operators, etc)
Note that synapses can be both directional (chemical) or bidirectional (electrical), also think about higher-order synapses and think about subthreshold communication between neurons
Implement the parasynaptic propagation
design the long-range communication between neurons (inspire from Internet node-to-node communication protocol, also inspire from blockchain)
implement neurons with long-term memory (inspire from the paper about voltage dependent DNA fragmenting)
Implement the symbolic components of the deep brain (see notion + github: calculator, Turing tape, recorder, etc)
Implement the observer module of the deep brain (collect info about the brain dynamics)
implement the different forms of plasticity
design the parameter sharing mechanisms
see the .md files: implement the possibility for the brain to:
stop a computation
resume a computation
etc




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

