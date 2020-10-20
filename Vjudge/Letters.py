import sys

line = sys.stdin.readline().split()

n, m = int(line[0]), int(line[1])

line = sys.stdin.readline().split()

rooms = list(map(int, line))

line = sys.stdin.readline().split()

letts = list(map(int, line))

acc = [0] * n

acc[0] = rooms[0]

for i in range(n):
    acc[i] = rooms[i] + acc[i - 1]

prev = 0
for j in range(m):
    lett = letts[j]
    for k in range(prev, n):
        if acc[k] >= lett:
            prev = k
            quita = 0
            if k > 0:
                quita = acc[k - 1]
            print(k + 1, lett - quita)
            break
