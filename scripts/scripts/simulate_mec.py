import numpy as np
import os
from cso import CelestialSwarmOptimizer
from pso import ParticleSwarmOptimizer
from gwo import GreyWolfOptimizer
from ga import GeneticAlgorithm
from sa import SimulatedAnnealing


TASK_DATA_PATH = "data/tasks.npy"
if not os.path.exists(TASK_DATA_PATH):
    raise FileNotFoundError(f"Task dataset {TASK_DATA_PATH} not found! Run generate_tasks.py first.")

tasks = np.load(TASK_DATA_PATH)


cso = CelestialSwarmOptimizer()
pso = ParticleSwarmOptimizer()
gwo = GreyWolfOptimizer()
ga = GeneticAlgorithm()
sa = SimulatedAnnealing()

methods = {"CSO": cso, "PSO": pso, "GWO": gwo, "GA": ga, "SA": sa}
results = {}

for name, optimizer in methods.items():
    best_solution, best_fitness, _ = optimizer.solve(tasks)
    results[name] = best_fitness
    print(f"✅ {name} completed with Best Fitness: {best_fitness}")


RESULTS_PATH = "data/simulation_results.npy"
np.save(RESULTS_PATH, results)
print(f"📊 Simulation results saved at {RESULTS_PATH}.")
