import matplotlib.pyplot as plt
import numpy as np

class GridWorld:

    def __init__(self):
        self.width = 5
        self.height = 5

        self.agent_x = 0
        self.agent_y = 0

        self.goal_y = self.height - 1
        self.goal_x = self.width - 1

    def render(self, output_file):
        # Set up background tile checkerboard pattern
        img = np.empty(self.height*self.width)
        img[::2] = 1.0
        img[1::2] = 0.9
        img = img.reshape((self.height,self.width))

        # Mark goal and agent
        img[self.goal_y, self.goal_x] = 0.4
        img[self.agent_y, self.agent_x] = 0.2

        # Save to output file
        figure = plt.figure()
        plt.clf()
        plt.imshow(img, cmap='tab20c', vmin=0.0, vmax=1)
        figure.savefig(output_file)
        plt.close()
