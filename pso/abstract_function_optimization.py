import abc


class AbstractFunctionOptimization(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, number_of_inputs: int, lim_min: int, lim_max: int):
        self.number_of_inputs = number_of_inputs
        self.lim_min = lim_min
        self.lim_max = lim_max

    @abc.abstractmethod
    def get_function_fitness(self, input: list) -> float:
        pass