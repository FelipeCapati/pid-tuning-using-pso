from pso.space import Space
from pso.particle import Particle
from pid.example_imp_pid import ExampleOnePID
from pso.abstract_function_optimization import AbstractFunctionOptimization


class PSO(object):
    def __init__(self, W: float, c1: float, c2: float, n_iterations: int, n_particles: int, target: float, target_error: float):
        self.W = W
        self.c1 = c1
        self.c2 = c2
        self.n_iterations = n_iterations
        self.n_particles = n_particles
        self.target = target
        self.target_error = target_error
        self.pid = ExampleOnePID()

    def run(self, function_optimization: AbstractFunctionOptimization) -> list:
        search_space = Space(target=self.target
                             , target_error=self.target_error
                             , n_particles=self.n_particles
                             , function_optimization=function_optimization)
        particles_vector = [Particle(lim_min=function_optimization.lim_min, lim_max=function_optimization.lim_max, length=function_optimization.number_of_inputs) for _ in range(search_space.n_particles)]
        search_space.particles = particles_vector
        search_space.print_particles()

        iteration = 0
        while iteration < self.n_iterations:
            print("Iteration = %s" % iteration)
            search_space.set_pbest()
            search_space.set_gbest()

            if abs(search_space.gbest_value - search_space.target) <= search_space.target_error:
                break

            search_space.move_particles(W=self.W, c1=self.c1, c2=self.c2)
            iteration += 1

        return search_space.gbest_position
