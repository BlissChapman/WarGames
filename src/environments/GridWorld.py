import matplotlib.pyplot as plt
import numpy as np

class GridWorld:

    def __init__(self, num_agents):
        self.width = 5
        self.height = 5
        self.agents_x = [0]*num_agents
        self.agents_y  = [0]*num_agents
        self.obstacles = []

        self.reset()

    def reset(self):
        for i in range(len(self.agents_x)):
            self.agents_x[i] = 0
            self.agents_y[i] = 0

        self.goal_y = self.height - 1
        self.goal_x = self.width - 1

    def render(self, output_file, add_obstacle):
        # Set up background tile checkerboard pattern
        img = np.empty(self.height*self.width)
        img[::2] = 1.0
        img[1::2] = 0.9
        img = img.reshape((self.height,self.width))

        colors = [0.2, 0.5, 0.6]

        # Mark goal and agent
        img[self.goal_y, self.goal_x] = 0.4

        for i in range(len(self.agents_x)):
            img[self.agents_y[i], self.agents_x[i]] = colors[i]

        if add_obstacle:
            for i in range(self.height-2):
                img[i, 1] = 0.7
                obstacles.append(tuple(i, 1))
            for i in range(1, self.width):
                img[self.height-3, i] = 0.7
                obstacles.append(tuple(self.height-3, i))

        # Save to output file
        figure = plt.figure()
        plt.clf()
        plt.imshow(img, cmap='tab20c', vmin=0.0, vmax=1)
        figure.savefig(output_file)
        plt.close()