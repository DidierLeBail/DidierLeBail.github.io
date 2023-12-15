---
permalink: /exams
title: "exams"
author_profile: true
---

The evaluation of the degree of cleverness of our agents consists in a sequence of individual tasks of the same form as a quizz:
each task comes along with a description and one or two examples.
Then four answers are presented to the agent.
Only one is the correct answer.
It is also shown that each answer can be selected by pushing a button.
The agent should give his guess for the correct answer by pushing the button corresponding to his guess.

During the exam session, the agent stands in a room.
On one wall of the room are projected images or videos.
Sound can also be broadcast.
Four buttons are placed at the center of the room, each button corresponding to a different answer.

# tasks
Tasks range from the simplest to the hardest, where the degree of difficulty corresponds to the degree of abstraction required to successfully complete the task.

## perceptual completion
The simplest tasks involve completion of sensory information.
However, this is also the case for the hardest tasks, since the only data the agents have access to are sensory data.
For completing a piece of data, you need a model of these data, that tells you how they are structured as a whole.
The easiest data to model would be the data the agents are the most accustomed to, i.e. sensory information they receive from their natural surroundings, their natural habitat.
Since our agents are endowed with the senses of hearing and vision only, then the two basic completion tasks are completion of natural images and natural sounds.

### completion of natural images
A photo of the Minecraft world is randomly taken and projected onto a screen, but a small part of it is removed and let black.
Each of the four possible answers is a different proposal for the missing part of the image.
The goal is to identify the correct gluing.

### completion of natural sounds
Some seconds of ambient sounds in a Minecraft environment are recored and broadcast into the exam room.
However, three out of the four answers have been modified by superimposing a weird intruder sound.
The goal is to identify the natural soundtrack.

### completion of daily scenes
Some scenes of a typical day in the Minecraft world are recorded together with the ambient sounds, then broadcast into the room.
Some parts of the video are removed : e.g. if the video is 1 min long, the frames from 20 to 40 seconds are left blank.
Each answer is a proposal for the intermediate frames and soundtrack that have been removed.
Note that some proposals can have the correct frames but not the correct soundtrack, etc.
The correct answer has both the original frames and soundtrack.

## abstract classification
An aspect of intelligence other than data completion is to distinguish between things that are alike and things that are different.
One of the most famous example of such a task are the so-called [Bongard problems](https://www.foundalis.com/res/bps/bpidx.htm).
However, these problems must be adapted to our quizz setting.
Originally, consider a background made up of two blank pages.
Six boxes are drawn on each page, and each box is filled up with a black and white drawing.
All six boxes on the left page share a common feature, which also is absent from every box on the right page.
The goal is to formulate this feature in natural language.

In our setting, natural language cannot be used so instead, we propose a new drawing, and the agent should choose which on side it shall go.
This shrinks down the number of answers from four in the other tasks, to two in this task.
Another possibility is to propose the twelve boxes all mixed together.
Then the agent should partition them in the two groups of six boxes we expect.

génération et mémorisation de chaînes aléatoires,
Ravens progressive matrices, letter-string analogy problems created by Hofstadter,
 (Harry Foundalis' website) (note these problems need to be turned into a quizz, e.g. by proposing new
candidates and the lapinou has to place these propositions in the correct box or in no box if appopriate (so there may be
a third box, containing objects that cannot be classified)), Abstraction and Reasoning Corpus (ARC), Impartial-RAVEN corpus,
extend image completion to handwritten letters and digits (recall lapinous can write in the chat so they know about letters and
digits), fulfill a task like write a character or a figure by following ad-hoc rules (e.g. lapinou moves or gestures are
translated into drawings on a screen so the lapinou has to learn on-the-fly how to produce the requested figure),
Bongard-LOGO (see "A new benchmark for human-level concept learning and reasoning"), overall focus on core knowledge:
 - basic arithmetic
 - intuitive physics and objects
 - spatial geometry (includes relations like "in front of", "between", "next to", "far from", etc)
 - agents and goal-directedness (basic theory of mind),
include generative tasks,
