import random

class RandomAgent:

    def __init__(self):
        self.training = True

    def action(self, state, action_choices):
        # Choose a random direction
        return random.choice(action_choices)

    def learn(self, state, action, chosen_next_state, reward_for_choice):
        # Do nothing - random agents don't learn
        pass
