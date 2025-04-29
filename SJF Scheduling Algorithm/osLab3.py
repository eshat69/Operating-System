print("Running Shortest Job First Scheduling Algorithm")
n = int(input("Enter the number of processes: "))
d = {}
# Input arrival and burst times for each process
for i in range(n):
    key = "P" + str(i + 1)
    arrival = int(input(f"Enter arrival time for {key}: "))
    burst = int(input(f"Enter burst time for {key}: "))
    d[key] = [arrival, burst]
d = sorted(d.items(), key=lambda item: item[1][0])
# Create a ready queue to schedule by shortest job
time = 0
completed = []
remaining = d.copy()
while remaining:
    # Get processes that have arrived till current time
    available = [proc for proc in remaining if proc[1][0] <= time]
    if available:
        # Select process with shortest burst time
        available.sort(key=lambda x: x[1][1])
        current = available[0]
    else:
        # If no process has arrived yet, jump to the next arrival time
        current = min(remaining, key=lambda x: x[1][0])
        time = current[1][0]
    time += current[1][1]
    completed.append((current[0], current[1][0], current[1][1], time))
    remaining.remove(current)
# Calculate Turnaround Time (TAT) and Waiting Time (WT)
TAT = [comp[3] - comp[1] for comp in completed]
WT = [tat - comp[2] for tat, comp in zip(TAT, completed)]
avg_WT = sum(WT) / n
print("\nProcess | Arrival | Burst | Completion | Turnaround | Waiting |")
for i in range(n):
    p, a, b, c = completed[i]
    print(f" {p}     |   {a}     |   {b}   |     {c}     |     {TAT[i]}      |   {WT[i]}")
print(f"\nAverage Waiting Time: {avg_WT:.2f}")
