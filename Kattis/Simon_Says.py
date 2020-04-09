import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'Simon' and line[1] == 'says':
        print(*line[2:])
