"""
User wants to optimize a function for which they have prior knowledge
* Need to provide Configs tried, along with the result

Requires:
---------
* Knowing how to specify previous evaluations. Might be easier at this point
  for users to understand ConfigSpace

Notes:
------
* We would need to check the prior configurations are valid.
    * If specified in `__init__` we can not verify until `optimize` is called. To fix
    this, the configspace could be in `__init__`?
    * We could put `previous evaluations in `optimize` itself?
* Do Configurations behave nicely as dictionary keys?
"""

def func(x1, x2):
    return x1 + x2

# Manual
# ------
optimizer = SMAC(
    previous_evaluations=[
        ({"x1": 4.0, "x2": 5.0}, 3.4)
        ({"x1": 7.0, "x2": 8.0}, 5.4)
    ]
)
optimizer.optimize(
    func,
    configspace={"x1": (1.0, 10.0), "x2": (1.0, 10.0)}
)

for (name, value), _ in previous_evaluations:
    assert value in configspace[name]


# Using ConfigSpace
# -----------------
# Specfiying Configurations and there results
optimizer = SMAC(
    previous_evaluations=[
        (Configuration, 3.4),
        (Configuration2, 5.4)
    ]
)
optimizer.optimize(
    func,
    configspace=ConfigurationSpace(...)
)

# Assert configs are generated from `configspace` parameter
for config, result in previous_evaluations:
    assert config in configspace

