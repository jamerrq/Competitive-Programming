import sys

n = int(sys.stdin.readline())

QALY = 0

for i in range(n):
    line = sys.stdin.readline().split()
    QALY += float(line[0]) * float(line[1])

print(QALY)
