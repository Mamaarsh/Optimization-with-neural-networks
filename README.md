# Optimization-with-neural-networks.
Scheduling optimization algorithms for operational systems with neural networks and machines learning

# Project Objective: 
The goal of this project is to design a neural network that predicts the operating system using the features available in the data.

# Project Description:
In the first step, create a dataset containing 1200 samples (rows), each sample containing 8 input features. These features
are:

•4 arrival times for processes (P1taP4)

•4 burst times for the same processes

The goal of this data is to predict the best scheduling algorithm for each instance,
so that the total waiting time in that instance is minimized.
In this project, only 3 classical scheduling algorithms are considered:

•FCFS (First Served)

•SJF (Short Job First)

•RR (Round Robin) with equal quantum 4

------------------------------------------------------------------------------------------
After creating 9 columns for feature labels, add 3 more columns to show the Waiting Time of each algorithm for each instance. (The name of the algorithm with the lowest Waiting Time should be in the Label column).

If two algorithms SJF and FCFS are minimized simultaneously, FCFS is considered as the label.

If two algorithms FCFS and RR are minimized simultaneously, RR is considered as the label.

If two algorithms SJF and RR are minimized simultaneously, SJF is considered as the label.

-------------------------------------------------------------------------------------------
# output example:

![image](https://github.com/user-attachments/assets/b96d4781-fcfc-49a7-9225-4f46c763a291)

-------------------------------------------------------------------------------------------
Authors: Mohammad Javad Majlesi, Mohammad Arshia Jafari.
