from smac import SMAC


def func(x1, x2):
    return x1 + x2

# Easiest
# -------
optimizer = SMAC(settings={
    "intensification": {
        "name": "Hyperband",
        "min_budget": 15,
    }
})

exit()
optimizer.optimize(
    func,
    configspace={
        "x1": (1.0, 10.0),  # Can translate easily to ConfigSpace
        "x2": (1.0, 10.0)
    }
)