import matplotlib.pyplot as plt
import numpy as np

class GridWorld:

    def __init__(self, num_agents, agent_type):
        self.width = 6
        self.height = 6

        self.agents_x = [0, 1]
        self.agents_y = [0, 0]
        
        self.obstacles = []

        self.one_move = True
        self.two_move = True

        self.reset()

    def reset(self):
        self.agents_x = [0, 1]
        self.agents_y = [0, 0]

        self.goal_y = self.height - 1
        self.goal_x = self.width - 1

        self.one_move = True
        self.two_move = True

    def render(self, output_file):
        # Set up background tile checkerboard pattern
        self.img = np.zeros((self.height, self.width))
        self.img[::, ::] = 1.0
        self.img[1::2, ::2] = 0.9
        self.img[::2, 1::2] = 0.9
        self.img = self.img.reshape((self.height,self.width))

        colors = [0.2, 0.05, 0.6]

        # Mark goal and agent
        self.img[self.goal_y, self.goal_x] = 0.4

        for i in range(len(self.agents_x)):
            self.img[self.agents_y[i], self.agents_x[i]] = colors[i]
        if not self.one_move:
            self.img[self.agents_y[0], self.agents_x[0]] = 0.8
        if not self.two_move:
            self.img[self.agents_y[1], self.agents_x[1]] = 0.8

        for i in range(self.height-2):
            self.img[i, 2] = 0.7
            self.obstacles.append((2, i))
        for i in range(2, self.width):
            self.img[self.height-2, i] = 0.7
            self.obstacles.append((i, self.height-2))

        # Save to output file
        figure = plt.figure()
        plt.clf()
        plt.imshow(self.img, cmap='tab20c', vmin=0.0, vmax=1)
        figure.savefig(output_file)
        plt.close()
