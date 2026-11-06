# FCFS Scheduling (Non-preemptive)

n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    print("Process P" + str(i + 1))
    arrival = int(input("  Arrival time: "))
    burst = int(input("  Burst time: "))
    processes.append({"pid": "P" + str(i + 1), "arrival": arrival, "burst": burst})

# Sort by arrival time
processes.sort(key=lambda p: p["arrival"])

timeline = []
current_time = 0

for p in processes:

    while current_time < p["arrival"]:
        timeline.append("IDLE")
        current_time += 1

    start_time = current_time
    p["response"] = start_time - p["arrival"]

    for i in range(p["burst"]):
        timeline.append(p["pid"])

    current_time += p["burst"]

    p["completion"] = current_time
    p["turnaround"] = p["completion"] - p["arrival"]
    p["waiting"] = p["turnaround"] - p["burst"]

# Gantt Chart
print("\nGantt Chart:")
chart = "|"
start = 0

for t in range(1, len(timeline) + 1):
    if t == len(timeline) or timeline[t] != timeline[start]:
        chart += f" {timeline[start]} ({start}-{t}) |"
        start = t

print(chart)

# Process Table
print(f"\n{'PID':<6}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}{'RT':<6}")

for p in processes:
    print(f"{p['pid']:<6}{p['arrival']:<6}{p['burst']:<6}"
          f"{p['completion']:<6}{p['turnaround']:<6}"
          f"{p['waiting']:<6}{p['response']:<6}")

# Average Times
avg_tat = sum(p["turnaround"] for p in processes) / n
avg_wt = sum(p["waiting"] for p in processes) / n
avg_rt = sum(p["response"] for p in processes) / n

print("\nAverage Turnaround Time =", round(avg_tat, 2))
print("Average Waiting Time    =", round(avg_wt, 2))
print("Average Response Time   =", round(avg_rt, 2))