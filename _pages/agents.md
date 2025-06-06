---
permalink: /agents
title: "Description of the agents"
author_profile: true
---

What we call an agent is the data of a body and a neural network controlling that body.
In addition to that, an agent encounters three stages of development:
(1) prenatal, (2) child and (3) adult.

The benefit of having three stages is to allow the agent's brain to develop for longer.

## prenatal
In the prenatal stage, external sensory inputs (vision and hearing) are disabled, but interal inputs are activated.
This encompasses food level, oxygen level, life points and inventory content.
The agent is not allowed to move by itself, meaning that the state of the motoneurons is not converted into motor commands acting upon the agent's body.
However, those motoneurons are not frozen:
their state evolves because of their connexion with the remainder of the network.

The agent is physically tied to one of its parents chosen at random.
The parent that is bearing the newborn agent is called the "mother".
However, there is no sexual differentiation between agents:
any agent can successfully copulate with any other one.

In the prenatal stage, the agent does not cost any energy to the mother:
its food level is automatically replenished when it drops too low.
The very existence of the prenatal agent is hidden to every other agent, except to the mother:
The brain of her is interfaced with the neural network of the prenatal agent via specialized neurons called the ferry neurons.

## child
In the child stage, the agent does not benefit from automatic food replenishment anymore.
However, it cannot forage food by itself, because it is still physically tied to its mother.
It can only be fed by the adult agents, who now can see and hear him.
The child can communicate with them through the chat and receives light and sounds.

## adult
In the adult stage, every input and output entry is activated:
the agent now can wander freely through the world of Minecraft, endowed with all the gameplay possibilities of human players other than modding or cheating:
mining, crafting, navigating, using items, etc.

In addition to that, the adult agent can copulate with other adults:
for this to be possible, the two agents need both to consent to the copulation and be physically close enough to each other.
Also, they need both to have enough life points.
The consent is based on the activation of a specialized output neuron:
when it activates, it allows copulation and prevents it when it is inactive.
For a copulation to be successful, all the mentioned requirements (physical proximity, neural activationn and enough life points) need to be sustained during a short period of time.
More precisely, a variable is introduced with value 0 when the requirements are met simultaneously for the first time.
When the variable reaches the value 1, the copulation is considered as done.
This variable decreases spontaneously in the absence of the requirements, but increases when they are all met simultaneously.
The variable is removed when it reaches the value 0 or 1.

When completed, a copulation takes food and oxygen from the two agents, and leads to a birth with a probability depending of the level of fertility of the parents.
This level is updated after each [exam](/exams) session:
an improvement in an agent's answers increases its level of fertility, while a decrease in performance leads to a decrease in fertility.
A successful copulation leads to the creation of two agents in prenatal stage, each one hosted by a different parent.
