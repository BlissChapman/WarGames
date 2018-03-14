# Analysis of Emergent Properties of Information Processing Systems Operating in Complex Environments.
by Bliss Chapman (nbchapm2@illinois.edu) and Varsha Subrahmanyam (varsha2@illinois.edu)

## Problem Motivation
We would like to understand how the economics of an environment influence the emergence of cooperation and conflict in multi-agent multi-goal interaction.  What conditions cause such a system to degenerate (i.e. make it impossible for agents to achieve their goals)?

## Problem Formulation
We propose the use of state of the art reinforcement learning techniques as a model of behavior for a rational agent acting with limited information about the environment (including the other agents).  We then design environments and models of agents with various properties and apply classical statistical simulation techniques to study the resulting interaction.

## Experiments
1) Agent A and Agent B live in a nxn grid world with a single overlapping path to a goal state.  Agent A and Agent B can either 1) stay still 2) move in any of the 4 cardinal directions or 3)'attack' in any of the 4 cardinal directions.  There is only room for one agent in the goal square.  Will Agent A and Agent B learn to attack one another to maximize their own reward?
2) Agent A and Agent B again live in a nxn grid world.  This time the goal state is only achieved if both agents occupy squares that are mirror images of each other.  Over time, the reward derived from staying in a goal state decreases and a rational agent would move to another square.  Will Agent A and Agent B learn to mirror each other's actions to achieve maximal reward?
3) Agent A and Agent B again live in a nxn grid world that simulates the conditions of [Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma).  Will Agent A and Agent B learn to cooperate in a single iteration of Prisoner's Dilemma?  What about in many iterations of Prisoner's Dilemma?  What about if the number of total iterations of Prisoner's Dilemma is known by the agents?
4) Repeat experiment 3 but allowing each agent to signal an intent to the other agents.  Each agent can choose to either lie or not to lie.  How does this change the outcome of iterated Prisoner's Dilemma?  What if we add a third Agent C?  What if each agent has a predefined level of trustworthiness that is known by them alone and allows them to lie about their intent only a certain fraction of the time?

## Thought Experiments
1) Simulate an artificial neuron with a very simple actuator.  What properties emerge when entire populations of neurons are exposed to simple inputs?  What if the inputs are randomized?  What if the inputs represent an encoding of simple patterns of beeps?  What if the inputs represent an encoding of Beethoven's 5th Symphony?
2) Finally, here's an example of a simulation way beyond the scope of anything we can simulate directly today: Are religious belief systems an emergent property of information processing systems evolving in an environment like Earth?

## Resources
[Understanding Agent Cooperation](https://deepmind.com/blog/understanding-agent-cooperation/)

[Homo Economicus](https://en.wikipedia.org/wiki/Homo_economicus)

[Multi-agent Reinforcement Learning in Sequential Social Dilemmas](https://storage.googleapis.com/deepmind-media/papers/multi-agent-rl-in-ssd.pdf)

[Multiagent Cooperation and Competition with Deep Reinforcement Learning](https://arxiv.org/pdf/1511.08779.pdf)

[When Machine Learning Meets AI and Game Theory](http://cs229.stanford.edu/proj2012/AgrawalJaiswal-WhenMachineLearningMeetsAIandGameTheory.pdf)

[Deep Learning for Predicting Human Strategic Behavior](http://www.cs.ubc.ca/~jasonhar/GameNet-NIPS-2016.pdf)

[A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning](https://arxiv.org/pdf/1711.00832.pdf)

[Multi-Agent Cooperation and the Emergence of Natural Language](https://openreview.net/pdf?id=Hk8N3Sclg)

[Multi-Agent Reinforcement Learning Paper Collection](https://github.com/LantaoYu/MARL-Papers#learning-to-communicate)

[Flow: Architecture and Benchmarking for Reinforcement Learning in Traffic Control](https://arxiv.org/abs/1710.05465)

[Complex dynamics of elementary cellular automata emerging from chaotic rules](https://arxiv.org/abs/1203.6074)

[Modeling the Formation of Social Conventions in Multi-Agent Populations](https://arxiv.org/abs/1802.06108)

[Valuing knowledge, information and agency in Multi-agent Reinforcement Learning: a case study in smart buildings](https://arxiv.org/abs/1803.03491)

[Ingredients for Robotic Research](https://blog.openai.com/ingredients-for-robotics-research/)

[Social norm complexity and past reputations in the evolution of cooperation](https://www.nature.com/articles/nature25763)
 
