# SJF (Shortest Job First) - Non-preemptive

n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    print("Process P" + str(i + 1))
    arrival = int(input("  Arrival time: "))
    burst = int(input("  Burst time: "))
    processes.append({"pid": "P" + str(i + 1), "arrival": arrival, "burst": burst})

processes.sort(key=lambda p: p["arrival"])

for p in processes:
    p["done"] = False

timeline = []
current_time = 0
finished = 0

while finished < n:
    shortest = None

    for p in processes:
        if p["arrival"] <= current_time and not p["done"]:
            if shortest is None or p["burst"] < shortest["burst"]:
                shortest = p

    if shortest is None:
        timeline.append("IDLE")
        current_time += 1
        continue

    start_time = current_time
    shortest["response"] = start_time - shortest["arrival"]

    for i in range(shortest["burst"]):
        timeline.append(shortest["pid"])

    current_time += shortest["burst"]

    shortest["completion"] = current_time
    shortest["turnaround"] = current_time - shortest["arrival"]
    shortest["waiting"] = shortest["turnaround"] - shortest["burst"]
    shortest["done"] = True

    finished += 1

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
