import sys

line = sys.stdin.readline().split()
n, s = int(line[0]), int(line[1])

line = sys.stdin.readline().split()
ascd = list(map(int, line))
line = sys.stdin.readline().split()
desc = list(map(int, line))

possible = False

if ascd[0] == 1:
    if ascd[s - 1] == 1:
        possible = True
    else:
        if sum([1 for i in range(s, n) if ascd[i] + desc[i] > 1]) > 0\
            and desc[s - 1]:
            possible = True

if possible:
    print('YES')
else:
    print('NO')
