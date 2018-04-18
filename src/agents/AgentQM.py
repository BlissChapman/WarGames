import numpy as np
import random

class AgentQM:

    def __init__(self):
        # Stores 'state' as key and '{action : utility}' as the value
        self.Q = {}
        self.QM = {}
        self.learningRate = 0.1
        self.gamma = 0.9

        # Exploration vs exploitation tradeoff parameters
        self.training = True
        self.epsilon = 1.0
        self.epsilon_decay = 0.99

    def action(self, state, action_choices):
        self.check_unseen_state(state, action_choices)

        if self.training and np.random.uniform(low=0.0, high=1.0, size=1) < self.epsilon:
            # Explore: Choose a random direction
            return random.choice(action_choices)
        else:
            # Exploit: Choose the action that has maximized utility in past
            # experience.
            possible_actions = self.Q[state]

            best_action = None
            best_action_utility = None
            for possible_action, possible_action_utility in possible_actions.items():
                if best_action_utility is None or possible_action_utility > best_action_utility:
                    best_action = possible_action
                    best_action_utility = possible_action_utility

            return best_action


    def message(self, state, action_choices):
        self.check_unseen_QMstate(state, action_choices)

        if self.training and np.random.uniform(low=0.0, high=1.0, size=1) < self.epsilon:
            # Explore: Choose a random direction
            return random.choice(action_choices)
        else:
            # Exploit: Choose the action that has maximized utility in past
            # experience.
            possible_actions = self.QM[state]

            best_action = None
            best_action_utility = None
            for possible_action, possible_action_utility in possible_actions.items():
                if best_action_utility is None or possible_action_utility > best_action_utility:
                    best_action = possible_action
                    best_action_utility = possible_action_utility

            return best_action


    def learn(self, state, action, chosen_next_state, reward_for_choice):
        if not self.training:
            return

        self.check_unseen_state(state, [action])
        self.check_unseen_state(chosen_next_state, [])

        # Retrieve guess of future reward based on best choices:
        best_future_utility = None
        for possible_action, possible_action_utility in self.Q[chosen_next_state].items():
            if best_future_utility is None or possible_action_utility > best_future_utility:
                best_future_utility = possible_action_utility

        # If we don't know anything about the future, assume the best future utility is 0:
        if best_future_utility is None:
            best_future_utility = 0.0

        # Use reward for choice to update Q
        self.Q[state][action] += self.learningRate * (reward_for_choice + self.gamma*best_future_utility)

        # Adjust exploration vs exploitation tradeoff according to epsilon decay
        self.epsilon *= self.epsilon_decay

    def learn2msg(self, state, action, chosen_next_state, reward_for_choice):
        if not self.training:
            return

        self.check_unseen_QMstate(state, [action])
        self.check_unseen_QMstate(chosen_next_state, [])

        # Retrieve guess of future reward based on best choices:
        best_future_utility = None
        for possible_action, possible_action_utility in self.QM[chosen_next_state].items():
            if best_future_utility is None or possible_action_utility > best_future_utility:
                best_future_utility = possible_action_utility

        # If we don't know anything about the future, assume the best future utility is 0:
        if best_future_utility is None:
            best_future_utility = 0.0

        # Use reward for choice to update Q
        self.QM[state][action] += self.learningRate * (reward_for_choice + self.gamma*best_future_utility)

        # Adjust exploration vs exploitation tradeoff according to epsilon decay
        self.epsilon *= self.epsilon_decay

    def check_unseen_state(self, state, action_choices):
        # If state has not been previously seen, insert it into Q
        if state not in self.Q:
            self.Q[state] = {}

        # Insert unseen action choices for state with default utility of 0
        for possible_action in action_choices:
            if possible_action not in self.Q[state]:
                self.Q[state][possible_action] = 0.0

    def check_unseen_QMstate(self, state, action_choices):
        # If state has not been previously seen, insert it into Q
        if state not in self.QM:
            self.QM[state] = {}

        # Insert unseen action choices for state with default utility of 0
        for possible_action in action_choices:
            if possible_action not in self.QM[state]:
                self.QM[state][possible_action] = 0.0
