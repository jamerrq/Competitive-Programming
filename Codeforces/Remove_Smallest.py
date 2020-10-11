import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    count = 0
    for i in range(n - 1):
        if abs(- l[i] + l[i + 1]) > 1:
            count += 1
    
    if count < 1:
        print('YES')
    else:
        print('NO')
