import sys

line = sys.stdin.readline().split()
r, c = int(line[0]), int(line[1])

cells = []

for _ in range(r):
    line = sys.stdin.readline().split()[0]
    cells.append(line)

spaces = [0] * 5

for i in range(r - 1):
    for j in range(c - 1):
        s = cells[i][j] + cells[i][j + 1] +\
            cells[i + 1][j] + cells[i + 1][j + 1]
        if s.count('#') == 0:
            spaces[s.count('X')] += 1

print('\n'.join([str(x) for x in spaces]))
