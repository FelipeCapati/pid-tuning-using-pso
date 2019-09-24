import random
import numpy as np
from pid.abstract_pid import AbstractPID


class Space():
    def __init__(self, target: float, target_error: float, n_particles: float, pid:AbstractPID):
        self.pid = pid
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')

        lim_min = 0
        lim_max = 5
        self.gbest_position = np.array([random.uniform(lim_min, lim_max)
                                , random.uniform(lim_min, lim_max)
                                , random.uniform(lim_min, lim_max)])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()

    def fitness(self, particle) -> float:
        return self.pid.get_fitness_pid(particle.position[0], particle.position[1], particle.position[2])

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if (particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if (self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self, W: float, c1: float, c2: float):
        for particle in self.particles:
            new_velocity = (W * particle.velocity) + \
                           (c1 * random.random()) * \
                           (particle.pbest_position - particle.position) + \
                           (random.random() * c2) * \
                           (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()