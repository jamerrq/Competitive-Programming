import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().split()
    a, b = int(line[0]), int(line[1])

    if a % b == 0:
        print(0)
    else:
        print(b - a % b)
