import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


P, D = readList()
dist = [None] * D
for _ in range(P):
    di, ai, bi = readList()
    if not dist[di - 1]:
        dist[di - 1] = [0, 0]

    dist[di - 1][0] += ai
    dist[di - 1][1] += bi

wa, wb, tot = 0, 0, 0
for i in range(D):
    A, B = dist[i]
    if A > B:
        WA = A - (A + B) // 2 - 1
        WB = B
        print('A', WA, WB)
    else:
        WA = A
        WB = B - (A + B) // 2 - 1
        print('B', WA, WB)

    wa += WA
    wb += WB
    tot += A + B

print(abs(wa - wb) / tot)
