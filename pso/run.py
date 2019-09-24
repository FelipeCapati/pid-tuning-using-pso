from pso.space import Space
from pso.particle import Particle
from pid.example_imp_pid import ExampleOnePID

class PSO(object):
    def __init__(self,W:float, c1:float, c2:float, n_iterations:int, n_particles:int, target:float, target_error:float):
        # PSO Config
        self.W = W
        self.c1 = c1
        self.c2 = c2
        self.n_iterations = n_iterations
        self.n_particles = n_particles
        self.target = target
        self.target_error = target_error
        self.pid = ExampleOnePID()

    def run(self) -> list:
        search_space = Space(target=self.target
                             , target_error=self.target_error
                             , n_particles=self.n_particles
                             , pid= self.pid)
        particles_vector = [Particle() for _ in range(search_space.n_particles)]
        search_space.particles = particles_vector
        search_space.print_particles()


        iteration = 0
        while (iteration < self.n_iterations):
            print("Iteration = %s" % iteration)
            search_space.set_pbest()
            search_space.set_gbest()

            if (abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
                break

            search_space.move_particles(W=self.W, c1=self.c1, c2=self.c2)
            iteration += 1

        return search_space.gbest_position