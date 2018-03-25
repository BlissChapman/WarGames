import random

class RandomAgent:

    def __init__(self):
        pass

    def action(self, state):
        # Choose a random direction
        action_choices = ['N', 'E', 'S', 'W']
        return random.choice(action_choices)

    def learn(self, state, action, chosen_next_state, reward_for_choice):
        # Do nothing - random agents don't learn
        pass
