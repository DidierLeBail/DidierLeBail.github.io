---
title: "step 4: the artificial brain"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/step_4
venue: "University 1, Department"
date: 2025-04-16
location: "Gottingen, Germany"
---

We describe here what are the steps to follow in order to build an artificial brain.
Note that we do not seek to build a brain-like computing system, which would directly emulate general intelligence.
Instead, we seek to define a class of computing systems, such that many instances of it realize general intelligence.
In parallel of that, in the previous and later phases (3- and 5+) we define a process that allows us to find such an instance.

# goal: what we want our computing system to realize
We want out computing system to have the potential to emulate general intelligence.
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
Also, there is no black box within an artificial brain: any intermediate computation within a neuron leaves a trace on the neighbouring neurons.
This choice is inspired from biological brains, where subthreshold fluctuations of the membrane potential are detected by neighbouring neurons and participate to important neural functions (see [this paper](https://www.mdpi.com/2076-3425/13/1/74) and [this paper](https://www.pnas.org/doi/pdf/10.1073/pnas.1716933115)).
Aside from the relevance of this mechanism in biological brains, this choice allows our artificial brain to access the detailed steps of each neuron, making it possible to share variables between neurons, reuse some intermediate computations and adjust the behavior of a neuron depending on the context, including e.g. the correction of some errors.

For a comparison between brains and in silico computing systems, see [this paper](https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2023.1220030/full).

Note that we do not aim at reproducing a biologically plausible brain ; this would be completely out of the scope of modern computers.
Indeed, the human brain possesses 86 billion neurons, each of these neurons having in average 10 000 synapses.
Moreover, each neuron is at least as complex as a [deep artificial convolutional neural network, being e.g. to perform XOR computation within its dendritic tree alone](https://www.cell.com/neuron/pdfExtended/S0896-6273(21)00501-8).
Besides neurons, the brain contains [as many glial cells](https://pmc.ncbi.nlm.nih.gov/articles/PMC5063692/pdf/nihms799882.pdf), which play [a direct and critical role in the brain computations](https://pmc.ncbi.nlm.nih.gov/articles/PMC2894949/pdf/rstb20090313.pdf) and are yet not understood.
Said otherwise, it is simply impossible to simulate a biological brain, even on modern supercomputers.

That is why we include as many symbolic components and imperative programming instructions as possible (e.g. the node-to-node communication protocol), which we will describe in the following.

To recap, an artificial brain is a computing system satisfying the following properties:
- a temporal directed weighted network, called the synaptic network
- elementary computing units called neurons. Neurons of various types coexist, including symbolic processing units. The precise definition of a neuron will be given in the following.
- another temporal network called the parasynaptic network (inspired from the hormons released in the brain)
- every parameter is subject to context-dependent plasticity
- no black box: computations within each neuron are available to other neurons
- a long-range communication protocol allowing neurons from distant areas to communicate via the synaptic network
- a module called an observer, that computes various statistics about the dynamics of the whole brain and makes these statistics available to the brain itself
- components or modules explicitly designed for long-term storage (building upon the ideas of [neural Turing machines](https://www.researchgate.net/profile/Faramarz-Safi/publication/344617740_A_Review_on_Neural_Turing_Machine_NTM/links/602fe79da6fdcc37a83954d2/A-Review-on-Neural-Turing-Machine-NTM.pdf), [engrams](https://pmc.ncbi.nlm.nih.gov/articles/PMC9065729/) and [epigenetic storage of information](https://www.nature.com/articles/s41539-019-0048-y.pdf)).




# still in progress


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
implement neurons with long-term memory (inspire from the paper about )
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

