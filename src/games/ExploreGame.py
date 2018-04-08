from environments.GridWorld import GridWorld

class ExploreGame:

    def __init__(self, agent1, agent2=None):
        self.agent1 = agent1
        self.agent2 = agent2
        self.env = GridWorld()
        self.num_steps_in_game = 25

    def reset(self):
        self.env.reset()

    def step(self, agent_num):
        # Build state representation of the current environment
        state_tuple = ExploreGame.state_representation(self.env)

        # Retrieve agent's chosen action for state
        action_choices = ['N', 'E', 'S', 'W', '_']
        if agent_num == 1:
            action_choice = self.agent1.action(state=state_tuple,
                                          action_choices=action_choices)
        else:
            action_choice = self.agent2.action(state=state_tuple,
                                          action_choices=action_choices)
        # Simulate effect of agent's chosen action
        if action_choice == 'N':
            if tuple((self.env.agent_x, self.env.agent_y - 1)) in self.env.obstacles:
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                self.env.agent_y = max(self.env.agent_y - 1, 0)
        elif action_choice == 'E':
            if tuple((self.env.agent_x + 1, self.env.agent_y)) in self.env.obstacles:
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                self.env.agent_x = min(self.env.agent_x + 1, self.env.width - 1)
            
        elif action_choice == 'S':
            if tuple((self.env.agent_x, self.env.agent_y + 1)) in self.env.obstacles:
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                self.env.agent_y = min(self.env.agent_y + 1, self.env.height-1)
            
        elif action_choice == 'W':
            if tuple((self.env.agent_x - 1, self.env.agent_y)) in self.env.obstacles:
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                self.env.agent_x = max(self.env.agent_x - 1, 0)
            
        elif action_choice == '_':
            pass
        else:
            print("Agent attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))

        # Compute reward
        reward = ExploreGame.reward(self.env)

        # Allow agent to learn
        new_state_tuple = ExploreGame.state_representation(self.env)
        if agent_num == 1:
            self.agent1.learn(state_tuple, action_choice, new_state_tuple, reward)
        else:
            self.agent2.learn(state_tuple, action_choice, new_state_tuple, reward)

    def state_representation(env):
        return (env.agent_x, env.agent_y)

    def reward(env):
        agentReachedGoalState = (env.agent_x, env.agent_y) == (env.goal_x, env.goal_y)
        return 1.0 if agentReachedGoalState else -0.1
