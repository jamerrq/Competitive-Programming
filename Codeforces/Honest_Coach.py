import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    mini = abs(l[0] - l[1])
    for i in range(1, n):
        if abs(l[i] - l[i - 1]) < mini:
            mini = abs(l[i] - l[i - 1])
    print(mini)
