import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    m = {}
    for num in A:
        m[num] = m.get(num, 0) + 1

    l = [(key, value) for key, value in m.items()]
    l.sort(key=lambda x : x[1])
    f = l.pop(0)[0]

    intvs = []
    for i in range(n):
        if i == 0 or (not f - A[i]) or i == n - 1:
            intvs.append(i)

    print(f, intvs)
    count = sum([1 for i in range(1, len(intvs)) if intvs[i] > intvs[i - 1] + 1])
    print(count)
