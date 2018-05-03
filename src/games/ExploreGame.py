from environments.GridWorld import GridWorld

class ExploreGame:

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

        self.env = GridWorld(2)

        self.num_steps_in_game = 25

    def reset(self):
        self.env.reset()

    def step(self, num):
        # Build state representation of the current environment
        state_tuple = ExploreGame.state_representation(self.env)


        # Retrieve agent's chosen action for state
        action_choices = ['N', 'E', 'S', 'W']
        if num == 0:
            action_choice = self.agent1.action(state=state_tuple,
                                          action_choices=action_choices)
            last_pos = self.agent1.last_pos = (self.env.agents_x[num], self.env.agents_y[num])
        else:
            action_choice = self.agent2.action(state=state_tuple,
                                          action_choices=action_choices)
            last_pos = self.agent2.last_pos = (self.env.agents_x[num], self.env.agents_y[num])

        # Simulate effect of agent's chosen action
        if action_choice == 'N':
            print("N")
            self.env.agents_y[num] = max(self.env.agents_y[num] - 1, 0)
        elif action_choice == 'E':
            print("E")
            self.env.agents_x[num] = min(self.env.agents_x[num] + 1, self.env.width - 1)
        elif action_choice == 'S':
            print("S")
            self.env.agents_y[num] = min(self.env.agents_y[num] + 1, self.env.height-1)
        elif action_choice == 'W':
            print("W")
            self.env.agents_x[num] = max(self.env.agents_x[num] - 1, 0)
        elif action_choice == '_':
            print("_")
            pass
        else:
            print("Agent attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))
        # Compute reward
        reward = ExploreGame.reward(self.env, num, last_pos)

        # Allow agent to learn
        new_state_tuple = ExploreGame.state_representation(self.env)
        if num == 0:
            self.agent1.learn(state_tuple, action_choice, new_state_tuple, reward)
        else:
            self.agent2.learn(state_tuple, action_choice, new_state_tuple, reward)

    def state_representation(env):
        return (env.agents_x[0], env.agents_y[0], env.agents_x[1], env.agents_y[1])

    def reward(env, num, last_pos):
        mirroring = ((env.agents_y[0] == env.agents_y[1]) and (env.agents_x[0] + env.agents_x[1] == 5) and (env.agents_x[0] != env.agents_x[1]))
        not_moving = last_pos == (env.agents_x[num], env.agents_y[num])
        if not_moving:
            return -0.1
        elif mirroring:
            return 2.0
        return -0.1
