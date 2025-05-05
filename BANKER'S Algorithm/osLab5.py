print("BANKER'S ALGORITHM")
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))
print("Enter Allocation Matrix:")
allocation = []
for i in range(n):
    allocation.append(list(map(int, input(f"Process {i} allocation: ").split())))
print("Enter Maximum Matrix:")
maximum = []
for i in range(n):
    maximum.append(list(map(int, input(f"Process {i} max: ").split())))
available = list(map(int, input("Enter Available Resources: ").split()))
need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)
finish = [False] * n
safe_sequence = []
while len(safe_sequence) < n:
    allocated_in_this_round = False
    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= available[j] for j in range(m)):
                for j in range(m):
                    available[j] += allocation[i][j]
                safe_sequence.append(f"P{i}")
                finish[i] = True
                allocated_in_this_round = True
                break
    if not allocated_in_this_round:
        break
if len(safe_sequence) == n:
    print("\nSystem is in a Safe State.")
    print("Safe Sequence:", ' -> '.join(safe_sequence))
else:
    print("\nSystem is NOT in a Safe State.")
