"""
User simply wants to optimize a function
* Need to provide names of parameters
* Need to provide ranges of parameters

Requires:
---------
* Understanding how to specify a ConfigSpace, manual is most intuitive without experience with
  ConfigSpace.

Notes:
------
* ConfigSpace doesn't support unnamed hyperparameters?
    * Makes sense a Hyperparameter should only be given a name once in the ConfigSpace?
    * This would require a major refactor of ConfigSpace
* Seems we would want directly translate everything to a ConfigurationSpace and Configurations
  before doing anything
"""
def func(x1, x2):
    return x1 + x2

# Easiest
# -------
optimizer = SMAC()
optimizer.optimize(
    func,
    configspace={
        "x1": (1.0, 10.0),  # Can translate easily to ConfigSpace
        "x2": (1.0, 10.0)
    }
)

# With ConfigSpace Hyperparameters
# ---------------------------------------
optimizer = SMAC()
optimizer.optimize(
    func,
    configspace=[
        FloatHyperparameter("x1", 1, 10),  # Just add them all to a ConfigSpace
        FloatHyperparameter("x2", 1, 10)
    ]
)


# Using ConfigSpace
# -----------------
configspace = ConfigurationSpace()
configspace.add_hyperparameters([
    FloatHyperparameter("x1", 1, 10),
    FloatHyperparameter("x2", 1, 10)
])

optimizer = SMAC()
optimizer.optimize(
    func,
    configspace=configspace  # They've done the work for us
)


