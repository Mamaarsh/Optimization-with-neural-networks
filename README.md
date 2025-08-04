# Optimization with Neural Networks: Scheduling Algorithm Predictor

A machine learning project to optimize CPU scheduling by predicting the best algorithm for a given scenario using neural networks.

## Project Objective

Design a neural network model that **predicts the most efficient scheduling algorithm** for a given set of process features. The aim is to **minimize total waiting time** for each instance using learned patterns in the data.

## 📄 Project Description

### Problem

Given the arrival and burst times of four processes, determine which of the following classical scheduling algorithms yields the **lowest total waiting time**:

- **FCFS** (First Come First Serve)
- **SJF** (Shortest Job First)
- **RR** (Round Robin) with a fixed quantum of 4

### 🧾 Dataset Structure

- **Samples:** 1200
- **Features per sample:** 8
  - **4 Arrival Times** → `P1ta`, `P2ta`, `P3ta`, `P4ta`
  - **4 Burst Times** → `P1bt`, `P2bt`, `P3bt`, `P4bt`
- **Additional columns per sample:**
  - `FCFS_WT` → Total waiting time for FCFS
  - `SJF_WT` → Total waiting time for SJF
  - `RR_WT` → Total waiting time for RR
  - `Label` → The name of the algorithm with the **minimum waiting time**

### 🏷️ Labeling Rule

To assign the final label (best algorithm):

1. If **SJF** and **FCFS** tie → choose `FCFS`
2. If **FCFS** and **RR** tie → choose `RR`
3. If **SJF** and **RR** tie → choose `SJF`
4. Otherwise → choose the one with the smallest waiting time

---

## 🛠️ Technologies Used

- Python 3.x
- NumPy, Pandas
- PyTorch (for MLP Neural Network)
- Scikit-learn (for preprocessing & metrics)
- Matplotlib / Seaborn (for visualization)

---

## 🔄 Workflow

1. **Dataset generation**:
   - Randomly generate 1200 rows of arrival and burst times
   - Simulate all 3 algorithms for each row
   - Calculate waiting times and assign the correct label

2. **Model design**:
   - A Multi-Layer Perceptron (MLP) classifier
   - Input: 8 normalized features
   - Output: 3-class prediction (`FCFS`, `SJF`, or `RR`)

3. **Training & Evaluation**:
   - Split data into training/validation/test sets
   - Evaluate accuracy, precision, recall
   - Visualize confusion matrix

---

# Dataset example:

![image](https://github.com/user-attachments/assets/94a959ae-84b9-4f20-a6b7-7523c1473a72)

# Output example:

![image](https://github.com/user-attachments/assets/65409c1e-089a-4483-bfca-1efa488c2c51)

---
Authors: Mohammad Javad Majlesi, Mohammad Arshia Jafari.
