from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


class GridWorld:

    def __init__(self):
        self.width = 12
        self.height = 12
        self.curr_step = -1
        self.reset()

    def reset(self):
        self.agent_A = []
        self.agent_B = []
        self.curr_step = -1

    def render(self, output_file):
        # Set up background tile checkerboard pattern
        img = np.empty(self.height*self.width)
        img[::2] = 1.0
        img[1::2] = 0.9

        curr = self.curr_step
        if self.agent_A[curr] == 0:
            img[curr*2] = 0.2
        elif self.agent_A[curr] == 1:
            img[curr*2] = 0.4

        if self.agent_B[curr] == 0:
            img[curr*2 + 1] = 0.2
        elif self.agent_B[curr] == 1:
            img[curr*2 + 1] = 0.4

        img = img.reshape((self.height,self.width))

        # Save to output file
        figure = plt.figure()
        plt.clf()
        plt.imshow(img, cmap='tab20c', vmin=0.0, vmax=1)
        figure.savefig(output_file)
        plt.close()
