print("ROUND ROBIN SCHEDULING")
n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    pid = "P" + str(i + 1)
    arrival = int(input(f"Enter arrival time of process {i+1}: "))
    burst = int(input(f"Enter burst time of process {i+1}: "))
    processes.append([pid, arrival, burst])
time_quantum = int(input("Enter Time Quantum: "))
current_time = 0
queue = []
completed = []
remaining_burst = {}
arrival_map = {}
for p in processes:
    pid, arrival, burst = p
    remaining_burst[pid] = burst
    arrival_map[pid] = arrival
processes.sort(key=lambda x: x[1])
ready = processes.copy()
visited = set()
while True:
    for p in ready:
        if p[1] <= current_time and p[0] not in visited:
            queue.append(p[0])
            visited.add(p[0])
    if queue:
        pid = queue.pop(0)
        arrival = arrival_map[pid]
        burst = remaining_burst[pid]
        exec_time = min(time_quantum, burst)
        current_time += exec_time
        remaining_burst[pid] -= exec_time
        for p in ready:
            if p[1] <= current_time and p[0] not in visited:
                queue.append(p[0])
                visited.add(p[0])
        if remaining_burst[pid] > 0:
            queue.append(pid)
        else:
            for p in processes:
                if p[0] == pid:
                    finish = current_time
                    tat = finish - p[1]
                    wt = tat - p[2]
                    completed.append([pid, p[1], p[2], finish, tat, wt])
    else:
        if len(completed) == n:
            break
        current_time += 1
avg_wt = sum(p[5] for p in completed) / n
print("\nProcess | Arrival | Burst | Exit | Turn Around | Wait |")
for p in completed:
    print(f" {p[0]}     |   {p[1]}     |  {p[2]}   |  {p[3]}  |     {p[4]}      |  {p[5]}  ")
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
