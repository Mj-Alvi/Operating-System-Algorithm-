# SRTF (Shortest Remaining Time First) - Preemptive SJF

n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    print("Process P" + str(i + 1))
    arrival = int(input("  Arrival time: "))
    burst = int(input("  Burst time: "))
    processes.append({"pid": "P" + str(i + 1), "arrival": arrival, "burst": burst})
    
# ---------- Algorithm ----------
processes.sort(key=lambda p: p["arrival"])

for p in processes:
    p["remaining"] = p["burst"]
    p["response"] = -1

timeline = []
current_time = 0
finished = 0

while finished < n:
    chosen = None

    for p in processes:
        if p["arrival"] <= current_time and p["remaining"] > 0:
            if chosen is None or p["remaining"] < chosen["remaining"]:
                chosen = p

    if chosen is None:
        timeline.append("IDLE")
        current_time += 1
        continue

    # First response time
    if chosen["response"] == -1:
        chosen["response"] = current_time - chosen["arrival"]

    timeline.append(chosen["pid"])
    chosen["remaining"] -= 1
    current_time += 1

    if chosen["remaining"] == 0:
        chosen["completion"] = current_time
        chosen["turnaround"] = chosen["completion"] - chosen["arrival"]
        chosen["waiting"] = chosen["turnaround"] - chosen["burst"]
        finished += 1

# ---------- Gantt Chart ----------
print("\nGantt Chart:")
chart = "|"
start = 0

for t in range(1, len(timeline) + 1):
    if t == len(timeline) or timeline[t] != timeline[start]:
        chart += f" {timeline[start]} ({start}-{t}) |"
        start = t

print(chart)

# ---------- Process Table ----------
print(f"\n{'PID':<6}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}{'RT':<6}")

for p in processes:
    print(f"{p['pid']:<6}{p['arrival']:<6}{p['burst']:<6}"
          f"{p['completion']:<6}{p['turnaround']:<6}"
          f"{p['waiting']:<6}{p['response']:<6}")

# ---------- Average Times ----------
avg_tat = sum(p["turnaround"] for p in processes) / n
avg_wt = sum(p["waiting"] for p in processes) / n
avg_rt = sum(p["response"] for p in processes) / n

cpu_utilization = (sum(p["burst"] for p in processes) / current_time) * 100

print("\nAverage Turnaround Time =", round(avg_tat, 2))
print("Average Waiting Time    =", round(avg_wt, 2))
print("Average Response Time   =", round(avg_rt, 2))
print("CPU Utilization         =", round(cpu_utilization, 2), "%")