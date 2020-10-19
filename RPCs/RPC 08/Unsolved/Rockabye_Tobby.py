import sys


T = int(sys.stdin.readline())

for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    mini = float('inf')
    meds = []
    for _ in range(n):
        m, t = sys.stdin.readline().split()
        meds.append((int(t), m))
        mini = min(mini, int(t))
    
    maxi = mini * k
    sched = [None] * maxi
    for med in meds:
        t, m = med
        for i in range(t, maxi, t):
            if sched[i] is None:
                sched[i] = []
            sched[i].append(m)

    count = 0
    i = 0
    pills = []
    while count < k:
        if sched[i] is not None:
            for j in range(len(sched[i])):
                pills.append((i, sched[i][j]))
                count += 1
        i += 1
    
    for i in range(count):
        print(pills[i][0], pills[i][1])
