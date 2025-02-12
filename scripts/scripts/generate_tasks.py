import numpy as np
import os

NUM_TASKS = 100  
TASK_MIN_SIZE = 500
TASK_MAX_SIZE = 5000

tasks = np.random.randint(TASK_MIN_SIZE, TASK_MAX_SIZE, size=(NUM_TASKS,))
TASK_DATA_PATH = "data/tasks.npy"

# Save tasks to file
os.makedirs("data", exist_ok=True)
np.save(TASK_DATA_PATH, tasks)
print(f"✅ Task dataset generated and saved at {TASK_DATA_PATH}.")
