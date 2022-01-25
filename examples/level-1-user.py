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
)
