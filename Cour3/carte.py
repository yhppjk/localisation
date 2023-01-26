import numpy as np
import random
import matplotlib as plt

world_size = 100.
landmarks = np.array([[20,20],[20.,80],[80,20],[80,80]],float)

class robot:
    def __int__(self):
        self.x = random.random()*world_size
        self.y = random.random()*world_size
        self.orientation = random.random() * 2 * np.pi

    def set(self, x, y, orientation):
        self.x = float(x)
        self.y = float(y)
        self.orientation = float(orientation)
        return self.x, self.y, self.orientation

    def move(self, heading, distance):

        self.orientation = (self.orientation + heading) % (2*np.pi)

        x = self.x + (np.cos(self.orientation) * distance)
        y = self.y + (np.sin(self.orientation) * distance)










