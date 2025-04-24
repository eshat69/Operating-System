
print("Running FCFS Scheduling Algorithm...")
n = int(input("Enter the number of processes: "))
d = {}

# Input arrival and burst times for each process
for i in range(n):
    key = "P" + str(i + 1)
    arrival = int(input(f"Enter arrival time for {key}: "))
    burst = int(input(f"Enter burst time for {key}: "))
    d[key] = [arrival, burst]

# Sort processes by arrival time (in case they are not already sorted)
d = sorted(d.items(), key=lambda item: item[1][0])

# Calculate Completion Time (CT) for each process
CT = []
for i in range(len(d)):
    CT.append(d[i][1][1] if i == 0 else CT[i - 1] + d[i][1][1])

# Calculate Turnaround Time (TAT) and Waiting Time (WT) for each process
TAT = [CT[i] - d[i][1][0] for i in range(len(d))]
WT = [TAT[i] - d[i][1][1] for i in range(len(d))]

# Calculate average waiting time
avg_WT = sum(WT) / n

# Print results in a table format
print("Process | Arrival | Burst | Completion | Turnaround | Waiting |")
for i in range(n):
    print(f" {d[i][0]}     |  {d[i][1][0]}      |  {d[i][1][1]}    |     {CT[i]}     |    {TAT[i]}       |  {WT[i]}     ")

print(f"\nAverage Waiting Time: {avg_WT:.2f}")
