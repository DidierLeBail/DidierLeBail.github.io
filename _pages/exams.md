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
An aspect of intelligence other than data completion is to group together things that are alike and distinguish between things that are different.

### Bongard problems
One of the most famous examples of such a task are the so-called [Bongard problems](https://www.foundalis.com/res/bps/bpidx.htm).
However, these problems must be adapted to our quizz setting.
Originally, consider a background made up of two blank pages.
Six boxes are drawn on each page, and each box is filled up with a black and white drawing.
All six boxes on the left page share a common feature, which also is absent from every box on the right page.
The goal is to formulate this feature in natural language.
Although only 100 problems were originally designed, then joined by 300 more designed by hand, now new problems can be generated [automatically](https://arxiv.org/abs/2010.00763), ensuring enough diversity over generations of agents.

Note however, that in our setting natural language cannot be used, so instead, we propose a new drawing, and the agent should choose on which side it should go.
This shrinks down the number of possible answers from four in the other tasks, to two in this task.
Another possibility is to propose the twelve boxes all mixed together.
Then the agent should partition them in the two groups of six boxes that are expected from the secret feature.

### pairing
Some objects are presented to the agent and the goal is to match pairs of identical objects.
For example the [concentration game](https://en.wikipedia.org/wiki/Concentration_(card_game)) falls in this category.
We can also imagine that objects are presented one at a time, and the goal is to indicate whether the presented object has already been encountered.
We can also imagine a search game, where an object is given and the agent has to retrieve it in a bunch of data (for example an object placed somewhere in an image, or a word placed in a dictionary, or a sound placed at some time of a soundtrack, etc).

## abstract completion
In those tasks, the agent should infer rules that do not necessarily apply to sensory data most encountered in his environment.

### Raven progressive matrices
The [goal](https://en.wikipedia.org/wiki/Raven%27s_Progressive_Matrices) is to guess the content of the last entry of a matrix, typically 2x2, 4x4 or 6x6.
Every entry other than the last one has already been filled according to a rule, that the agent might need to infer in order to identify the correct completion.
Ever since the design of the original set, a larger set has been released, called the [Impartial-RAVEN corpus](https://arxiv.org/abs/2002.06838).

### the abstract and reasoning corpus (ARC)
Pairs of images with colored pixels are shown as examples of associations.
The second member of the pair is generated by applying a transformation rule to the first member of the pair.
The rule is the same for every pair.
The goal of the agent is to identify the pairs of images that satisfy the same relation as the examples.
An extended set and its description is available [here](https://lab42.global/arc/).

## other tasks
It would be possible to extend beyond the quizz setting so that the agent would be able to play generic games.
In particular, this would allow the agent to generate the correct answer rather than selecting it.

Here is an example of such a game:
a simple geometric figure made of a few black or white pixels is shown for a short time, then disappears.
The agent is supposed to re-draw this figure on a black screen pixel after pixel.
Assuming a square background and periodic boundary conditions, only three buttons are needed:
* one button moving the selected pixel to the right
* one button moving to the top
* one button changing the value of the selected pixel

Other interesting tasks would involve both sound and images.
These tasks would comprise extensions of Bongard problems, Raven matrices or the ARC corpus to both sounds and images.
An example of such task would be the completion of a succession of sounds.
Another example of task would test for associative memory:
Some images are shown simultaneously with a different sound, then if a sound is played, the agent must identify which image it had been paired with.

Other interesting tasks would be ethic problems:
a social context is given, typically a video of an agent in need of help.
The correct answer to this test is the action leading to the greatest common good.

The last type of task would test the understanding of the peers:
a video of an agent is projected and the tested agent should be able, among different possibilities, to select the correct outcome.
It is a completion task, but to complete it, the agent should have developed a model of the other agents.
