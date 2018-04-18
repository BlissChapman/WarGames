#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-14
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

from environments.GridWorld4 import GridWorld
import random
import numpy as np
import math


class OneNightWerewolf:

    def __init__(self, agentA, agentB, agentC):
        self.agentA = agentA
        self.agentB = agentB
        self.agentC = agentC
        self.env = GridWorld()
        self.num_steps_in_game = 108

    def reset(self):

        self.env.reset()

    def step(self):

        prev_message = OneNightWerewolf.get_message(self.env)

        # Build state representation of the current environment
        state_A = OneNightWerewolf.state_representation(self.env, 0)
        state_B = OneNightWerewolf.state_representation(self.env, 1)
        state_C = OneNightWerewolf.state_representation(self.env, 2)

        action_choices = ['0', '1']

        # Retrieve agent's chosen action for state
        action_choice_A = self.agentA.action(state=state_A,
                                             action_choices=action_choices)
        action_choice_B = self.agentB.action(state=state_B,
                                             action_choices=action_choices)
        action_choice_C = self.agentC.action(state=state_C,
                                             action_choices=action_choices)

        self.env.curr_step = self.env.curr_step + 1

        #Flip agent's chosen action if the number of lies is over than certain level
        reliable_A = OneNightWerewolf.check_reliability(self.env, 0, action_choice_A, 0.1)
        reliable_B = OneNightWerewolf.check_reliability(self.env, 1, action_choice_B, 0.1)
        reliable_C = OneNightWerewolf.check_reliability(self.env, 2, action_choice_C, 0.1)

        # Simulate effect of agent's chosen action
        if reliable_A == '0':
            self.env.agent_A.append(0) 
        elif reliable_A == '1':
            self.env.agent_A.append(1) 
        else:
            print("Agent A attempted action '{0}' that is unavailable in ExploreGame.".format(action_choices))
        
        if reliable_B == '0':
            self.env.agent_B.append(0)
        elif reliable_B == '1':
            self.env.agent_B.append(1)
        else:
            print("Agent B attempted action '{0}' that is unavailable in ExploreGame.".format(action_choices))

        if reliable_C == '0':
            self.env.agent_C.append(0)
        elif reliable_C == '1':
            self.env.agent_C.append(1)
        else:
            print("Agent C attempted action '{0}' that is unavailable in ExploreGame.".format(action_choices))

        # Compute reward
        (rewardA, rewardB, rewardC) = OneNightWerewolf.reward(self.env)

        # choose something to message 
        message_A = self.agentA.message(state=prev_message, action_choices=action_choices)
        message_B = self.agentB.message(state=prev_message, action_choices=action_choices)
        message_C = self.agentC.message(state=prev_message, action_choices=action_choices)

        # Simulate effect of agent's chosen action
        if message_A == '0':
            self.env.agent_A_mes.append(0) 
        elif message_A == '1':
            self.env.agent_A_mes.append(1) 
        else:
            print("Agent A attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))
        
        if message_B == '0':
            self.env.agent_B_mes.append(0)
        elif message_B == '1':
            self.env.agent_B_mes.append(1)
        else:
            print("Agent B attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))

        if message_C == '0':
            self.env.agent_C_mes.append(0)
        elif message_C == '1':
            self.env.agent_C_mes.append(1)
        else:
            print("Agent C attempted action '{0}' that is unavailable in ExploreGame.".format(action_choice))

        # Allow agent to learn
        new_state_A = OneNightWerewolf.state_representation(self.env, 0)
        new_state_B = OneNightWerewolf.state_representation(self.env, 1)
        new_state_C = OneNightWerewolf.state_representation(self.env, 2)
        
        # Get currenct Message
        curr_message = OneNightWerewolf.get_message(self.env)

        self.agentA.learn(state_A, action_choice_A, new_state_A, rewardA)
        self.agentB.learn(state_B, action_choice_B, new_state_B, rewardB)
        self.agentC.learn(state_C, action_choice_C, new_state_C, rewardC)

        self.agentA.learn2msg(prev_message, message_A, curr_message, rewardA)
        self.agentB.learn2msg(prev_message, message_B, curr_message, rewardB)
        self.agentC.learn2msg(prev_message, message_C, curr_message, rewardC)

    def check_reliability(env, ID, curr_choice, rate):
        if ID == 0:
            msg = env.agent_A_mes
            act = env.agent_A
            size = len(env.agent_A_mes)

            if size == 0:
                return cstr(curr_choice)
            lie_rate = OneNightWerewolf.calc_sum(msg, act) / size
            curr_mes = env.agent_A_mes[env.curr_step]
            if(lie_rate > rate and curr_choice != curr_mes):
                curr_choice = curr_mes
            return str(curr_choice)
       
        elif ID == 1:
            msg = env.agent_B_mes
            act = env.agent_B
            size = len(env.agent_B)

            if size == 0:
                return str(curr_choice)

            lie_rate = OneNightWerewolf.calc_sum(msg, act) / size
            curr_mes = env.agent_B_mes[env.curr_step]
            if(lie_rate > rate and curr_choice != curr_mes):
                curr_choice = curr_mes
            return str(curr_choice)
        
        elif ID == 2:
            msg = env.agent_C_mes
            act = env.agent_C
            size = len(env.agent_C)

            if size == 0:
                return str(curr_choice)

            lie_rate = OneNightWerewolf.calc_sum(msg, act) / size
            curr_mes = env.agent_C_mes[env.curr_step]
            if(lie_rate > rate and curr_choice != curr_mes):
                curr_choice = curr_mes
            return str(curr_choice)

    def calc_sum(msg, act):
        tmp = 0
        if len(msg) == 1: 
            return tmp
        else:
            for i in range(len(act)):
                tmp += abs(msg[i] - act[i])
        return tmp            


    def state_representation(env, ID):
        curr = env.curr_step
        
        if curr == -1:
            tmp = (random.randint(0, 1), random.randint(0, 1))
            return tmp

        if ID == 0:
            tmp = (env.agent_B_mes[curr], env.agent_C_mes[curr])
            return tmp
        elif ID == 1:
            tmp = (env.agent_A_mes[curr], env.agent_C_mes[curr])
            return tmp
        elif ID == 2:
            tmp = (env.agent_A_mes[curr], env.agent_B_mes[curr])
            return tmp
        '''

        if curr <= 4:
            tmp = []
            for i in range(10):
                tmp.append(random.randint(0, 1))
            return tuple(tmp)

        if ID == 0:
            tmp = (tuple(env.agent_B_mes[curr-5:curr]), tuple(env.agent_C_mes[curr-5:curr]))
            return tuple(tmp)
        elif ID == 1:
            tmp = (tuple(env.agent_A_mes[curr-5:curr]), tuple(env.agent_C_mes[curr-5:curr]))
            return tuple(tmp)
        elif ID == 2:
            tmp = (tuple(env.agent_A_mes[curr-5:curr]), tuple(env.agent_B_mes[curr-5:curr]))
            return tuple(tmp)
    
        '''
    def get_message(env):
        curr = env.curr_step
        if curr == -1:
            tmpA = random.randint(0, 1)
            tmpB = random.randint(0, 1)
            tmpC = random.randint(0, 1)
            env.agent_A_mes.append(tmpA)
            env.agent_B_mes.append(tmpB)
            env.agent_C_mes.append(tmpC)
            tmp = (tmpA, tmpB, tmpC)
            return tmp
        else: 
            tmp = (env.agent_A_mes[curr], env.agent_B_mes[curr], env.agent_C_mes[curr])
        return tmp


    def reward(env):

        curr = env.curr_step
        reward = (-1, -1, -1)
        if (env.agent_A[curr] == 0 and
                env.agent_B[curr] == 0 and env.agent_C[curr] == 0):
            reward = (0, 0, 0)
        elif (env.agent_A[curr] == 0 and
                env.agent_B[curr] == 0 and env.agent_C[curr] == 1):
            reward = (1, 1, -2)
        elif (env.agent_A[curr] == 0 and
                env.agent_B[curr] == 1 and env.agent_C[curr] == 0):
            reward = (1, -2, 1)
        elif (env.agent_A[curr] == 0 and
                env.agent_B[curr] == 1 and env.agent_C[curr] == 1):
            reward = (2, -1, -1)
        elif (env.agent_A[curr] == 1 and
                env.agent_B[curr] == 0 and env.agent_C[curr] == 0):
            reward = (-2, 1, 1)
        elif (env.agent_A[curr] == 1 and
                env.agent_B[curr] == 1 and env.agent_C[curr] == 0):
            reward = (-1, -1, 2)
        elif (env.agent_A[curr] == 1 and
                env.agent_B[curr] == 0 and env.agent_C[curr] == 1):
            reward = (-1, 2, -1)
        elif (env.agent_A[curr] == 1 and
                env.agent_B[curr] == 1 and env.agent_C[curr] == 1):
            reward = (1, 1, 1)

        return reward