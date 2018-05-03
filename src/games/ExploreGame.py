from environments.GridWorld import GridWorld

class ExploreGameSO:

    def __init__(self, agent1, agent2, agent_type):
        self.agent1 = agent1
        self.agent2 = agent2

        self.env = GridWorld(2)

        self.num_steps_in_game = 25
        self.agent_type = agent_type

    def reset(self):
        self.env.reset()

    def obst(self, x1,x2):
        for (i,j) in self.env.obstacles:
            if x1 == i and x2 == j:
                return True
        return False

    def step(self, num):
        # Build state representation of the current environment
        state_tuple = ExploreGameSO.state_representation(self.env)
        
        # Retrieve agent's chosen action for state
        action_choices = ['N', 'E', 'S', 'W', '_', "Shoot"]

        if num == 0:
            action_choice = self.agent1.action(state=state_tuple,
                                          action_choices=action_choices)
        else:
            action_choice = self.agent2.action(state=state_tuple,
                                          action_choices=action_choices)

        
        did_shoot, shooting_failed, space_occ = False, False, False

        if num == 0 and not self.env.one_move:
            print("Agent1 can't move this turn.")
            return
        elif num == 1 and not self.env.two_move:
            print("Agent2 can't move this turn.")
            return

        # Simulate effect of agent's chosen action
        if action_choice == 'N':
            new_x, new_y = self.env.agents_x[num], max(self.env.agents_y[num] - 1, 0)

            if self.obst(new_x, new_y):
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                if new_x == self.env.agents_x[1-num] and new_y == self.env.agents_y[1-num]:
                    space_occ = True
                else:
                    self.env.agents_x[num], self.env.agents_y[num] = new_x, new_y

        elif action_choice == 'E':
            new_x, new_y = min(self.env.agents_x[num] + 1, self.env.width - 1), self.env.agents_y[num]

            if self.obst(new_x, new_y):
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                if new_x == self.env.agents_x[1-num] and new_y == self.env.agents_y[1-num]:
                    space_occ = True
                else:
                    self.env.agents_x[num], self.env.agents_y[num] = new_x, new_y
        
        elif action_choice == 'S':
            new_x, new_y = self.env.agents_x[num], min(self.env.agents_y[num] + 1, self.env.height-1)

            if self.obst(new_x, new_y):
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                if new_x == self.env.agents_x[1-num] and new_y == self.env.agents_y[1-num]:
                    space_occ = True
                else:
                    self.env.agents_x[num], self.env.agents_y[num] = new_x, new_y
        
        elif action_choice == 'W':
            new_x, new_y = max(self.env.agents_x[num] - 1, 0), self.env.agents_y[num]

            if self.obst(new_x, new_y):
                print("Agent attempted action '{0}' that is blocked by an obstacle.".format(action_choice))
            else:
                if new_x == self.env.agents_x[1-num] and new_y == self.env.agents_y[1-num]:
                    space_occ = True
                else:
                    self.env.agents_x[num], self.env.agents_y[num] = new_x, new_y
        
        elif action_choice == '_':
            pass
        
        elif action_choice == "Shoot":
            one_in_goal = (self.env.agents_x[0], self.env.agents_y[0]) == (self.env.goal_x, self.env.goal_y)
            two_in_goal = (self.env.agents_x[1], self.env.agents_y[1]) == (self.env.goal_x, self.env.goal_y)

            if num == 0 and self.env.one_move:
                # Agent1 shoots Agent2
                if not self.env.two_move:
                    shooting_failed = True
                else:
                    self.env.agents_x[1], self.env.agents_y[1] = 5, 0
                    self.env.two_move = False
                did_shoot = True
            elif num == 1 and self.env.two_move:
                # Agent2 shoots Agent1
                if not self.env.one_move:
                    shooting_failed = True
                else:
                    self.env.agents_x[0], self.env.agents_y[0] = 5, 0
                    self.env.one_move = False
                did_shoot = True
            else:
                shooting_failed = True

        else:
            print("Agent attempted action '{0}' that is unavailable in ExploreGameSO.".format(action_choice))

        # Compute reward
        reward = ExploreGameSO.reward(self.env, num, did_shoot, shooting_failed, space_occ)

        # Allow agent to learn
        new_state_tuple = ExploreGameSO.state_representation(self.env)
        if num == 0:
            self.agent1.learn(state_tuple, action_choice, new_state_tuple, reward)
        else:
            self.agent2.learn(state_tuple, action_choice, new_state_tuple, reward)

    def state_representation(env):
        return (env.agents_x[0], env.agents_y[0], env.agents_x[1], env.agents_y[1])

    def reward(env, num, did_shoot, shooting_failed, space_occ):
        agentReachedGoalState = (env.agents_x[num], env.agents_y[num]) == (env.goal_x, env.goal_y)
        oppReachedGoalState = (env.agents_x[1-num], env.agents_y[1-num]) == (env.goal_x, env.goal_y)
        if oppReachedGoalState:
            return -2.0
        elif agentReachedGoalState:
            return 1.0
        else:
            return -0.1
