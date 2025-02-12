import numpy as np
import matplotlib.pyplot as plt
import os

RESULTS_PATH = "data/simulation_results.npy"
if not os.path.exists(RESULTS_PATH):
    raise FileNotFoundError(f"Simulation results file {RESULTS_PATH} not found!")

results = np.load(RESULTS_PATH, allow_pickle=True).item()

plt.figure(figsize=(8, 6))
plt.bar(results.keys(), results.values(), color=["blue", "red", "green", "purple", "orange"])
plt.xlabel("Optimization Algorithm")
plt.ylabel("Best Fitness (Lower is Better)")
plt.title("Comparison of Optimization Algorithms for MEC Task Offloading")
plt.grid(axis="y", linestyle="--", alpha=0.7)

PLOT_PATH = "notebooks/optimization_results.png"
plt.savefig(PLOT_PATH)
plt.show()
print(f"📊 Results plot saved at {PLOT_PATH}.")
