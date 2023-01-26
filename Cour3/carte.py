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
        self.x = x
        self.y = y
        self.orientation = orientation