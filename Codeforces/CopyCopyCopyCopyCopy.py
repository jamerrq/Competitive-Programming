import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    print(len(set(line)))
