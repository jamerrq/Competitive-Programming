import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    w = [0] * 100
    m = {}
    W = list(map(int, sys.stdin.readline().split()))
    for num in W:
        m[num] = m.get(num, 0) + 1
    for num in set(num):