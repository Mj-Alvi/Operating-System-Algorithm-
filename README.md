# Operating System CPU Scheduling Algorithms

A collection of CPU scheduling algorithms implemented in **Python** and **C**. This project demonstrates how an operating system selects processes for CPU execution and compares scheduling performance using standard metrics.

## Algorithms Included

| No. | Algorithm | Scheduling Type |
|---:|---|---|
| 1 | First Come First Served (FCFS) | Non-preemptive |
| 2 | Shortest Job First (SJF) | Non-preemptive |
| 3 | Shortest Remaining Time First (SRTF) | Preemptive SJF |
| 4 | Round Robin (RR) | Preemptive |
| 5 | Priority Scheduling | Non-preemptive |
| 6 | Priority Scheduling | Preemptive |

## Features

- Accepts process details from the user.
- Takes Arrival Time and Burst Time as input.
- Takes Priority as input for priority scheduling.
- Takes Time Quantum as input for Round Robin scheduling.
- Displays a Gantt chart for process execution.
- Calculates Completion Time, Turnaround Time, Waiting Time, and Response Time.
- Calculates average Turnaround Time, Waiting Time, and Response Time.
- Calculates CPU Utilization.
