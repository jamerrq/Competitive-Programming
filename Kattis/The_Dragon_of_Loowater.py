import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


while True:
    n, m = readList()
    if n + m:
        heads = []
        knights = []
        for _ in range(n):
            heads.append(read())
        for _ in range(m):
            knights.append(read())

        heads.sort()
        knights.sort()
        ans = 0
        i = 0
        while heads and i < m:
            head = heads.pop(0)
            while i < m:
                knight = knights[i]
                if knight >= head:
                    ans += knight
                    break
                i += 1

            i += 1

        if heads:
            print('Loowater is doomed!')
        else:
            print(ans)

    else:
        break
