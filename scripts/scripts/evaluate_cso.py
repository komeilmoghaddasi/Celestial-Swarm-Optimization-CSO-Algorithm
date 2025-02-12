import numpy as np
import os

RESULTS_PATH = "data/cso_results.npy"
if not os.path.exists(RESULTS_PATH):
    raise FileNotFoundError(f"Results file {RESULTS_PATH} not found! Run train_cso.py first.")

best_solution = np.load(RESULTS_PATH)

TASK_DATA_PATH = "data/tasks.npy"
if not os.path.exists(TASK_DATA_PATH):
    raise FileNotFoundError(f"Task dataset {TASK_DATA_PATH} not found!")

tasks = np.load(TASK_DATA_PATH)

energy_consumption = np.sum(best_solution * tasks) 
latency = np.mean(tasks / best_solution)  

# Print Results
print("🔍 CSO Evaluation Results:")
print(f"⚡ Total Energy Consumption: {energy_consumption:.2f} J")
print(f"⏳ Average Task Completion Time: {latency:.2f} sec")

EVAL_REPORT = "data/cso_evaluation.txt"
with open(EVAL_REPORT, "w") as f:
    f.write(f"Energy Consumption: {energy_consumption:.2f} J\n")
    f.write(f"Task Completion Time: {latency:.2f} sec\n")

print(f"📄 Evaluation results saved at {EVAL_REPORT}.")
