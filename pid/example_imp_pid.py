from pid.abstract_pid import AbstractPID
from scipy import signal


class ExampleOnePID(AbstractPID):
    def __init__(self):
        super(ExampleOnePID, self).__init__(number_of_inputs=3, lim_min=0, lim_max=5)

    def get_plant_transfer_function(self) -> signal.lti:
        return signal.lti([4], [1, 0.5, 1])

    def get_fitness_pid(self, kp: float, ki: float, kd: float) -> float:
        indicators = self.get_performance_indicators_pid(kp=kp, ki=ki, kd=kd)
        fitness = indicators.overpoint*indicators.time_to_setpoint

        if (fitness == 0):
            fitness = 10

        print("####################################")
        print("Fitness = %s" % fitness)
        print("Overpoint = %s" % indicators.overpoint)
        print("TimeToSetpoint = %s" % indicators.time_to_setpoint)
        print("####################################")

        return fitness

    def get_function_fitness(self, input) -> float:
        # TODO: Verificar porque tem um erro aqui
        return self.get_fitness_pid(input[0], input[1], input[2])
