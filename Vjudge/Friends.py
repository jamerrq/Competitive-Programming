import sys

m = int(sys.stdin.readline())

matrix = []
rows = [0] * 5

for _ in range(5):
    matrix.append([0] * 5)

for _ in range(m):
    line = sys.stdin.readline().split()
    a, b = int(line[0]), int(line[1])
    matrix[a - 1][b - 1] = 1
    rows[a - 1] += 1
    rows[b - 1] += 1

yes = False

for i in range(5):
    if rows[i] != 2:
        yes = True

if yes:
    print('WIN')
else:
    print('FAIL')
