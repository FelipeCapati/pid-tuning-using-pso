import random
import numpy as np

class Particle():
    def __init__(self):
        lim_min = 0
        lim_max = 5
        self.position = np.array([random.uniform(lim_min, lim_max)
                                , random.uniform(lim_min, lim_max)
                                , random.uniform(lim_min, lim_max)])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0, 0])

    def __str__(self):
        print("Particle with position: %s and the pbest is: %s" %(self.position, self.pbest_position))

    def move(self):
        self.position = self.position + self.velocity