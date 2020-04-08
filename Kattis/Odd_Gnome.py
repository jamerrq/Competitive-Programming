import sys

n = int(sys.stdin.readline())

for i in range(n):
    gs = sys.stdin.readline().split()
    for j in range(2, len(gs) - 1):
        if int(gs[j]) != int(gs[j - 1]) + 1:
            print(j)
            break
