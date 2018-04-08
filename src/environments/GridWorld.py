import matplotlib.pyplot as plt
import numpy as np

class GridWorld:

    def __init__(self):
        self.width = 5
        self.height = 5
        self.reset()
        self.obstacles = []

    def reset(self):
        self.agent_x = 0
        self.agent_y = 0

        self.goal_y = self.height - 1
        self.goal_x = self.width - 1

    def render(self, output_file, add_obstacle):
        # Set up background tile checkerboard pattern
        img = np.empty(self.height*self.width)
        img[::2] = 1.0
        img[1::2] = 0.9
        img = img.reshape((self.height,self.width))

        # Mark goal and agent
        img[self.goal_y, self.goal_x] = 0.4
        img[self.agent_y, self.agent_x] = 0.2

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