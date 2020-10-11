import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    w = []
    m = {}
    for num in l:
        if m.get(num, 1):
            w.append(num)
            m[num] = 0
    
    print(' '.join([str(x) for x in w]))
