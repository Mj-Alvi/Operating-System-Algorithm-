# Round Robin Scheduling

quantum = int(input("Enter time quantum: "))
n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    print("Process P" + str(i + 1))
    arrival = int(input("  Arrival time: "))
    burst = int(input("  Burst time: "))
    processes.append({"pid": "P" + str(i + 1), "arrival": arrival,
                      "burst": burst, "remaining": burst, "response": -1})

processes.sort(key=lambda p: p["arrival"])

queue = []
next_process = 0
gantt = []
current_time = 0
finished = 0

while finished < n:

    while next_process < n and processes[next_process]["arrival"] <= current_time:
        queue.append(processes[next_process])
        next_process += 1

    if not queue:
        next_time = processes[next_process]["arrival"]
        gantt.append(("IDLE", current_time, next_time))
        current_time = next_time
        continue

    p = queue.pop(0)

    if p["response"] == -1:
        p["response"] = current_time - p["arrival"]

    run_time = min(quantum, p["remaining"])

    start_time = current_time
    current_time += run_time
    p["remaining"] -= run_time

    # Store each execution separately
    gantt.append((p["pid"], start_time, current_time))

    while next_process < n and processes[next_process]["arrival"] <= current_time:
        queue.append(processes[next_process])
        next_process += 1

    if p["remaining"] > 0:
        queue.append(p)
    else:
        p["completion"] = current_time
        p["turnaround"] = p["completion"] - p["arrival"]
        p["waiting"] = p["turnaround"] - p["burst"]
        finished += 1

# Gantt Chart
print("\nGantt Chart:")
for pid, start, end in gantt:
    print(f"| {pid} ({start}-{end}) ", end="")
print("|")

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
