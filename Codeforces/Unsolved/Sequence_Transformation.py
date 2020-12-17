import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    B = []
    for i in range(n):
        if (B and B[-1] != A[i]) or not B:
            B.append(A[i])

    m = {}
    for num in B[1:]:
        m[num] = m.get(num, 0) + 1

    min, num = m.get(B[0], 0), B[0]
    for numi in B:
        if m.get(numi, 0) < min:
            min = m.get(numi, 0)
            num = numi

    spaces = 0
    B.insert(0, num)
    for i in range(1, len(B)):
        spaces += int(B[i] != num and B[i - 1] == num)

    print(spaces)
