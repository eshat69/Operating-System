print("Running Priority Scheduling Algorithm...")
n = int(input("Enter the number of processes: "))
d = {}
# Input arrival time, burst time, and priority for each process
for i in range(n):
    key = "P" + str(i + 1)
    arrival = int(input(f"Enter arrival time for {key}: "))
    burst = int(input(f"Enter burst time for {key}: "))
    priority = int(input(f"Enter priority for {key} (lower number = higher priority): "))
    d[key] = [arrival, burst, priority]
# Sort based on arrival time and then priority
d = sorted(d.items(), key=lambda item: (item[1][0], item[1][2]))
# Calculate Completion Time (CT)
CT = []
current_time = 0
for i in range(len(d)):
    arrival, burst, _ = d[i][1]
    if current_time < arrival:
        current_time = arrival
    current_time += burst
    CT.append(current_time)
# Calculate Turnaround Time (TAT) and Waiting Time (WT)
TAT = [CT[i] - d[i][1][0] for i in range(len(d))]
WT = [TAT[i] - d[i][1][1] for i in range(len(d))]
# Average Waiting Time
avg_WT = sum(WT) / n
print("\nProcess | Arrival | Burst | Priority | Completion | Turnaround | Waiting |")
for i in range(n):
    print(f" {d[i][0]}     |   {d[i][1][0]}    |   {d[i][1][1]}   |    {d[i][1][2]}     |     {CT[i]}     |     {TAT[i]}      |   {WT[i]}")
print(f"\nAverage Waiting Time: {avg_WT:.2f}")
