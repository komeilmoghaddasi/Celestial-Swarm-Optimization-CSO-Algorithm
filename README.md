# 🌌 Celestial Swarm Optimization (CSO) for Task Offloading in MEC-IoT

## 📌 Overview
This repository provides an implementation of **Celestial Swarm Optimization (CSO)**, a novel swarm-based metaheuristic algorithm for **energy-efficient task offloading** in **Mobile Edge Computing (MEC)** environments. CSO optimizes the offloading decisions of IoT tasks by balancing exploration and exploitation through gravitational influences, reducing **energy consumption, latency, and computational overhead**.

📌 **Key Features:**
- Efficient task offloading strategy for MEC-enabled IoT networks.
- Novel **CSO algorithm** inspired by celestial mechanics.
- Performance comparison with **PSO, GWO, GA, SA, and Random Offloading**.
- Reproducible results with **Python-based simulations**.

---

## 👤 Developed By
**Komeil Moghaddasi**  
📧 [k.moghaddasi@ieee.org](mailto:k.moghaddasi@ieee.org)  

---

## 🚀 Quick Start

### 🔹 1️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed. Then, install required packages:

```bash
pip install -r requirements.txt
```

### 🔹 2️⃣ Generate MEC Task Data
Simulate IoT tasks for offloading:

```bash
python scripts/generate_tasks.py
```

### 🔹 3️⃣ Train CSO for Task Offloading
Run:

```bash
python scripts/train_cso.py
```

### 🔹 4️⃣ Evaluate CSO Performance
Compare CSO with baseline methods:

```bash
python scripts/evaluate_cso.py
```

### 🔹 5️⃣ Run Full Simulation
Execute the full simulation to analyze different optimization strategies:

```bash
python scripts/simulate_mec.py
```

### 🔹 6️⃣ Visualize Results
Generate comparative performance plots:

```bash
python scripts/plot_results.py
```

---

## 📂 Repository Structure

```plaintext
📦 Celestial-Swarm-Optimization-CSO
├── 📂 configs           # Configuration files (YAML)
├── 📂 data              # Input datasets for simulation
├── 📂 results           # Stored results and logs
├── 📂 scripts           # Python scripts for training, evaluation, and visualization
│   ├── generate_tasks.py  # Simulates IoT task data
│   ├── train_cso.py      # Trains CSO for task offloading
│   ├── evaluate_cso.py   # Evaluates CSO against baselines
│   ├── simulate_mec.py   # Runs MEC simulations
│   ├── plot_results.py   # Generates performance plots
├── 📜 requirements.txt  # Required dependencies
├── 📜 README.md         # Project documentation
```

---

## 📊 Performance Evaluation
CSO is compared against **PSO, GWO, GA, SA, and Random Offloading** in terms of:
- **Energy Consumption** ⚡
- **Task Completion Time** ⏳
- **CPU & Memory Utilization** 💾

📌 **Highlights:**
✅ **21.1% lower energy consumption** than baseline methods.  
✅ **16.9% lower task completion time** than standard swarm algorithms.  
✅ **Improved resource utilization** for large-scale MEC networks.

---


🔗 **Cite this repository if used in research.**  
📧 For any inquiries, contact **[k.moghaddasi@ieee.org](mailto:k.moghaddasi@ieee.org)**.

