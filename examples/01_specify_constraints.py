"""
User wants to now provide some constraints on their function
* Needs to understand the possible constraints

Requires:
---------
* Knowing the different constraints options

Notes:
------
* What constraints do we provide in `optimize` vs `__init__` vs any constraints?
* These should have a simple and correct default to provide fast feedback for users trying SMAC
"""

def func(x1, x2):
    return x1 + x2

optimizer = SMAC()
optimizer.optimize(
    func,
    configspace=configspace,
    runtime_limit=120,
    memory_limit=4,
    n_runs=10,
    deterministic=True,
)
