import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().split()
    a, b, p = int(line[0]), int(line[1]), int(line[2])
    stations = sys.stdin.readline().split()[0]
    n = len(stations)
    costs = [0] * n
    if stations[0] == 'A':
        costs[0] = b
    else:
        costs[0] = a
    curr_cost = costs[0]
    for i in range(1, n):
        if stations[i] == stations[i - 1]:
            costs[i] = curr_cost
        else:
            costs[i] = curr_cost
            if stations[i] == 'A':
                curr_cost += b
            else:
                curr_cost += a
    
    costs = [0] + costs
    j = n
    maxi = costs[-1]
    for i in range(n):
        if costs[i + 1] != costs[i] and maxi - costs[i] <= p:
            j = i + 1
            break
    print(j)
