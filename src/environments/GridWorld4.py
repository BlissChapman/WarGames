from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


class GridWorld:

    def __init__(self):
        self.width = 18
        self.height = 18
        self.curr_step = -1
        self.reset()

    def reset(self):
        self.agent_A = []
        self.agent_B = []
        self.agent_A_mes = []
        self.agent_B_mes = []
        self.curr_step = -1
        self.agent_C = []
        self.agent_C_mes = []



    def render(self, output_file):
        # Set up background tile checkerboard pattern
        img = np.empty(self.height * self.width)
        img[::3] = 1.0
        img[1::3] = 0.9
        img[2::3] = 0.8

        curr = self.curr_step
        if self.agent_A[curr] == 0:
            img[curr * 3] = 0.2
        elif self.agent_A[curr] == 1:
            img[curr * 3] = 0.4
        if self.agent_B[curr] == 0:
            img[curr * 3 + 1] = 0.2
        elif self.agent_B[curr] == 1:
            img[curr * 3 + 1] = 0.4

        
        if self.agent_C[curr] == 0:
            img[curr * 3 + 2] = 0.2
        elif self.agent_C[curr] == 1:
            img[curr * 3 + 2] = 0.4
        
        img = img.reshape((self.height, self.width))

        # Save to output file
        figure = plt.figure()
        plt.clf()
        plt.imshow(img, cmap='tab20c', vmin=0.0, vmax=1)
        figure.savefig(output_file)
        plt.close()

    def render_mes(self, output_file):
        # Set up background tile checkerboard pattern
        img = np.empty(self.height * self.width)
        img[::3] = 1.0
        img[1::3] = 0.9
        img[2::3] = 0.95
        
        curr = self.curr_step

        if curr<108:
            if abs(self.agent_A_mes[curr]- self.agent_A[curr]) == 0:
                img[curr * 3] = 0.6
            elif abs(self.agent_A_mes[curr]- self.agent_A[curr])== 1:
                img[curr * 3] = 0.8
            if abs(self.agent_B_mes[curr]- self.agent_B[curr]) == 0:
                img[curr * 3 + 1] = 0.6
            elif abs(self.agent_B_mes[curr]- self.agent_B[curr]) == 1:
                img[curr * 3 + 1] = 0.8
            if abs(self.agent_C_mes[curr]- self.agent_C[curr]) == 0:
                img[curr * 3 + 2] = 0.6
            elif abs(self.agent_C_mes[curr]- self.agent_C[curr]) == 1:
                img[curr * 3 + 2] = 0.8
            
            img = img.reshape((self.height, self.width))
            figure = plt.figure()
            plt.clf()
            plt.imshow(img, cmap='tab20c', vmin=0.0, vmax=1)
            figure.savefig(output_file)
            plt.close()