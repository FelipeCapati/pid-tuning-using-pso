import random
import numpy as np


class Particle(object):
    def __init__(self, lim_min: int, lim_max: int, length: int):
        #TODO: Implement for more lengths
        self.position = np.array([random.uniform(lim_min, lim_max)
                                , random.uniform(lim_min, lim_max)
                                , random.uniform(lim_min, lim_max)])
        self.velocity = np.array([0, 0, 0])
        self.pbest_position = self.position
        self.pbest_value = float('inf')

    def __str__(self):
        print("Particle with position: %s and the pbest is: %s" % (self.position, self.pbest_position))

    def move(self):
        self.position = self.position + self.velocity
