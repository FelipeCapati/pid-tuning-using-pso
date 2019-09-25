import abc
from scipy import signal
import sympy as sy
import utility.lti as lti
from pso.abstract_function_optimization import AbstractFunctionOptimization


class IndicatorPID(object):
    def __init__(self, overpoint:float, time_to_setpoint:float):
        self.overpoint = overpoint
        self.time_to_setpoint = time_to_setpoint


class AbstractPID(AbstractFunctionOptimization):
    __metaclass__ = abc.ABCMeta

    def __init__(self, number_of_inputs: int, lim_min: int, lim_max: int):
        super(AbstractPID, self).__init__(number_of_inputs=number_of_inputs, lim_min=lim_min, lim_max=lim_max)

    @abc.abstractmethod
    def get_plant_transfer_function(self) -> signal.lti:
        pass

    @abc.abstractmethod
    def get_fitness_pid(self, kp: float, ki: float, kd: float) -> float:
        pass

    def get_lti_by_pid(self, kp:float, ki:float, kd:float) -> signal.lti:
        # System equation
        lti_CT = signal.lti([kd, kp, ki], [0, 1, 0])
        lti_SY = self.get_plant_transfer_function()

        # Convert to sympy:
        Gs, Hs = lti.lti_to_sympy(lti_CT), lti.lti_to_sympy(lti_SY)

        # Multiply Gs and Hs
        GHs = sy.simplify(Gs * Hs).expand()  # make sure polynomials are canceled and expanded

        # Calculus of closing the loop without sensor gain
        IGHs = sy.simplify(GHs / (1 + GHs)).expand()

        return lti.sympy_to_lti(IGHs)

    def get_performance_indicators_pid(self, kp:float, ki:float, kd:float) -> IndicatorPID:
        # Get lti function about pid
        tf = self.get_lti_by_pid(kp=kp, ki=ki, kd=kd)

        # Analisy signal response a step signal
        t, y = signal.step(tf)

        # Get a time to setpoint
        time_to_setpoint = 0
        for i in range(0, len(y)):
            if y[i] >= 1.0 and y[i-1] < 1.0:
                time_to_setpoint = t[i]
                break

        return IndicatorPID(overpoint=y.max(), time_to_setpoint=time_to_setpoint)