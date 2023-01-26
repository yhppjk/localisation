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

        self.forward_noise = 0.
        self.turn_noise = 0.

    def set(self, x, y, orientation):
        self.x = float(x)
        self.y = float(y)
        self.orientation = float(orientation)
        return self.x, self.y, self.orientation

    def set_noise(self, forward_noise, turn_noise):
        self.forward_noise = forward_noise
        self.turn_noise = turn_noise

    def move(self, heading, distance):

        distance += np.random.normal(0, self.forward_noise)
        orientation = (self.orientation + heading + np.random.normal(0, self.turn_noise)) % (2*np.pi)

        x = self.x + (np.cos(self.orientation) * distance)
        y = self.y + (np.sin(self.orientation) * distance)

        if x > world_size or x < 0:
            x = x%world_size
        if y > world_size or y < 0:
            y = y%world_size

        res = robot()
        res.set(x, y, orientation)
        res.set_noise(self.forward_noise, self.turn_noise)
        return res
    def show(self):
        print("x= "+str(self.x) + "  y = "+str(self.y)+"; heading = "+ str(self.orientation) )


    def length(self):
        d1 = np.sqrt((self.x-20)**2+(self.y-20)**2)
        d2 = np.sqrt((self.x-20)**2+(self.y-80)**2)
        d3 = np.sqrt((self.x-80)**2+(self.y-20)**2)
        d4 = np.sqrt((self.x-80)**2+(self.y-80)**2)
        print("distance 1 = "+str(d1)+" distance 2 = "+str(d2)+" distance 3 = "+str(d3)+" distance 4 = "+str(d4))

    def measurement_probabilite(self):

        pass

myrobot = robot()
myrobot.set(10,10,0)
myrobot.set_noise(0,0)
myrobot.show()
myrobot.length()

myrobot = myrobot.move(np.pi/2, 10)
myrobot.show()
myrobot.length()
N = 1000
particule_set = []
for i in range(1000):
    particule_set.append(robot())
    particule_set[-1].set_noise(0,0)












