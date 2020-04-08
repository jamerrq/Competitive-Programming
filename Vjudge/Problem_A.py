import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().split()
    a, b = int(line[0]), int(line[1])
    x, y = int(line[2]), int(line[3])
    opt1 = max(x, a - x - 1) * b
    opt2 = a * max(y, b - y - 1)
    print(max(opt1, opt2))
