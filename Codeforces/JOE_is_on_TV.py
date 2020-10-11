import sys


n = int(sys.stdin.readline())

t = 0
for i in range(n):
    t += 1 / (i + 1)


print(t)