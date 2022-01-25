import smac


def func(x1, x2):
    return x1 + x2

configspace = ConfigurationSpace()

optimizer = SMAC(
    previous_evaluations={}  # Union[Dict[Config, Union[float, list]], Dict[[Tuple, Union[float, list]]]
    initial_design=InitialDesign(configs=)
)

optimizer.optimize(
    func,
    configspace=configspace
    runtime_limit=120,
    memory_limit=4,
    n_runs=10,
    deterministic=True,
)
