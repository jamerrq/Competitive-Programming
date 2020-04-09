import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().split()
    if len(line) > 2 and line[0] == 'simon' and line[1] == 'says':
        print(' '.join(line[2:]))
    else:
        print()
