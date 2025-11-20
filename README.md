NNA-Sim: Neural Network Accelerator Simulator

A Hardware-Software Co-Design Framework for Systolic Array Architectural Exploration.

📌 Overview

NNA-Sim is a Python-based simulation framework designed to analyze the performance and energy trade-offs of systolic array architectures. It serves as a cost-model simulator that allows computer architects to explore how hardware parameters (like array size) impact system efficiency for deep learning workloads.

This project was developed as a foundational tool for M.Tech research in Embedded System Design.

🚀 Features

Custom Compiler Backend: Implements a tiling engine to map large matrix multiplication tasks onto smaller physical arrays.

Cycle-Accurate Cost Model: Simulates execution cycles and estimates energy consumption based on architectural parameters.

Architectural Sweep: Automatically tests multiple hardware configurations (4x4, 8x8, 16x16) against a fixed workload.

Visualization: Auto-generates performance and energy trade-off graphs.

## 📂 Project Structure
```text
NNA_Project/
├── compiler/           # Software Backend
│   ├── compiler.py     # Tiling and instruction generation logic
│   └── __init__.py
├── sim/                # Hardware Model
│   ├── simulator.py    # Cycle-accurate simulator logic
│   └── __init__.py
├── main_experiment.py  # Experiment orchestration script
├── core_operation.py   # Functional baseline (NumPy)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```


🛠️ Installation & Usage

Clone the repository

git clone [https://github.com/Neelkachhia/NNA-Sim.git](https://github.com/Neelkachhia/NNA-Sim.git)

cd NNA-Sim


Create and activate a virtual environment

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate




Install dependencies

pip install -r requirements.txt


Run the experiment

python main_experiment.py


📊 Results

The simulation demonstrates the non-linear relationship between hardware area and system performance.

Performance Analysis

![Performance Plot](performance_results.png)

Energy Efficiency

![Energy Plot](energy_results.png)

🔮 Future Work

Implementation of Double Buffering scheduling to hide memory latency.

Support for Conv2D layers.

Integration with Apache TVM for advanced compiler optimizations.