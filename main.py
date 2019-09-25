from pso.run import PSO
from pid.example_imp_pid import ExampleOnePID

# Initialize PID
pid = ExampleOnePID()

# Initialize PSI
pso = PSO(
        W=0.5
        , c1=0.8
        , c2=0.9
        , n_iterations=100
        , n_particles=10
        , target=0.2
        , target_error=0.000001
    )

# Get tuning value
pid_tuning = pso.run(function_optimization=pid)
print("The best value for tuning PID is: %s" % pid_tuning)

