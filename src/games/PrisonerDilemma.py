from environments.GridWorld34 import GridWorld
import random

class PrisonerDilemma:

    def __init__(self, agentA, agentB):
        self.agentA = agentA
        self.agentB = agentB
        self.env = GridWorld()
        self.num_steps_in_game = 72

    def reset(self):

        self.env.reset()

    def step(self):
        # Build state representation of the current environment
        state_A = PrisonerDilemma.state_representation(self.env, 0, self.num_steps_in_game)
        state_B = PrisonerDilemma.state_representation(self.env, 1, self.num_steps_in_game)

        # Retrieve agent's chosen action for state
        action_choices = ['0', '1']
        action_choice_A = self.agentA.action(state=state_A,
                                          action_choices=action_choices)
        action_choice_B = self.agentB.action(state=state_B,
                                          action_choices=action_choices)

        self.env.curr_step = self.env.curr_step + 1

        # Simulate effect of agent's chosen action
        if action_choice_A == '0':
            self.env.agent_A.append(0) 
        elif action_choice_A == '1':
            self.env.agent_A.append(1) 
        else:
            print("Agent A attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))
        
        if action_choice_B == '0':
            self.env.agent_B.append(0)
        elif action_choice_B == '1':
            self.env.agent_B.append(1)
        else:
            print("Agent B attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))

        # Compute reward
        (rewardA, rewardB) = PrisonerDilemma.reward(self.env)
        # Allow agent to learn
        new_state_A = PrisonerDilemma.state_representation(self.env, 0, self.num_steps_in_game)  ##??????
        new_state_B = PrisonerDilemma.state_representation(self.env, 1, self.num_steps_in_game)

        self.agentA.learn(state_A, action_choice_A, new_state_A, rewardA)
        self.agentB.learn(state_B, action_choice_B, new_state_B, rewardB)

    def state_representation(env, ID, total):
        curr = env.curr_step
        left = total - curr
        ''' 
        if curr <= 4:
            tmp = [0, 0, 0, 0 ,0]
            #tmp.append(left)
            return tuple(tmp)

        if ID == 0:
            tmp = (env.agent_A[curr-5:curr])
            #tmp.append(left)
            return tuple(tmp)
        elif ID == 1:
            tmp = (env.agent_B[curr-5:curr])
            #tmp.append(left)
            return tuple(tmp)
        '''
    
        if curr == -1:
            return 0
        if ID == 0:
            return env.agent_A[curr]
        elif ID == 1:
            return env.agent_B[curr]
        
    def reward(env):

        curr = env.curr_step

        reward = (-1, -1)
        
        if (env.agent_A[curr] == 0 and env.agent_B[curr] == 0):
            reward = (-0.2, -0.2)
        elif (env.agent_A[curr] == 1 and env.agent_B[curr] == 1):
            reward = (-0.1, -0.1)
        elif (env.agent_A[curr] == 1 and env.agent_B[curr] == 0):
            reward = (-0.3, 0)
        elif (env.agent_A[curr] == 0 and env.agent_B[curr] == 1):
            reward = (0, -0.3)
        
        return reward
