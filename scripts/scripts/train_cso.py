import yaml
import numpy as np
import os
from cso import CelestialSwarmOptimizer  # Assuming CSO implementation is in `cso.py`

CONFIG_PATH = "configs/cso_config.yaml"
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"Configuration file {CONFIG_PATH} not found!")

with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)

cso = CelestialSwarmOptimizer(
    population_size=config["CSO"]["population_size"],
    max_iterations=config["CSO"]["max_iterations"],
    stagnation_thresh=config["CSO"]["stagnation_threshold"]
)

TASK_DATA_PATH = "data/tasks.npy"
if not os.path.exists(TASK_DATA_PATH):
    raise FileNotFoundError(f"Task dataset {TASK_DATA_PATH} not found! Run generate_tasks.py first.")

tasks = np.load(TASK_DATA_PATH)

best_solution, best_fitness, history = cso.solve(tasks)

RESULTS_PATH = "data/cso_results.npy"
np.save(RESULTS_PATH, best_solution)
print(f"✅ Training completed. Best Fitness: {best_fitness}")

HISTORY_PATH = "data/cso_history.npy"
np.save(HISTORY_PATH, history)
print(f"📊 Training history saved at {HISTORY_PATH}.")
