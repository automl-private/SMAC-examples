import smac


def func(x1, x2):
    return x1 + x2

optimizer = SMAC()
optimizer.optimize(
    func,
    configspace={
        "x1": FloatHyperparameter(1, 10),
        "x2": FloatHyperparameter(1, 10)
    }
    runtime_limit=120,
    memory_limit=4,
    n_runs=10,
    deterministic=True,
)
