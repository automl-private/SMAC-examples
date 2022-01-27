from smac.initial_design.random import RandomInitialDesign
from smac.initial_design.sobol import SobolInitialDesign
from smac.intensification.hyperband import Hyperband
from smac.intensification.successive_halving import SuccessiveHalving


SETTINGS = {
    
    "seed": 0,
    "multi_processing": True,
    "abort_on_first_run_crash": True,
    "cost_for_crash": 1e6,
    
    "func": {
        "detertministic": True,
    },
    
    
    "limitations": {
        "memory_limit": None,
        "walltime_limit": None,
        "func_limit": None,
    },

    "initial_design": {
        "name": [
            {
                "name": "random",
                "_default": True,
                "_class": RandomInitialDesign
            },
            {
                "name": "sobol",
                "n_configs": 16,
                "_class": SobolInitialDesign
            },
        ],
        "n_configs": 10,
    },
    
    "intensification": {
        "name": [
            {
                "name": "Hyperband",
                "min_budget": 10,
                "max_budget": 100,
                "eta": 3,
                "_class": Hyperband
            },
            {
                "name": "SuccessiveHalving",
                "_class": SuccessiveHalving
            },
        ],
    },
    
    "optimizer": {
        "name": [
            {
                "name": "RandomForest",
                "n_estimators": 100,
            },
            {
                "name": "GaussianProcess"
            },
            {
                "name": "Random",
            }
        ],
    },
        
    "acquisition_function": {
        "name": [
            {
                "name": "EI",
            }
        ]
    },
    
    "multi_objective": {
        "objectives": None,
    },
}