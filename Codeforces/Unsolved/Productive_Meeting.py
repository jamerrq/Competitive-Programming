import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()

for _ in range(t):
    n = read()
    A = readList()

    B = [[i, A[i]] for i in range(n)]
    B.sort(key=lambda x:x[1], reverse=True)

    tps = []

    i = 0
    j = 1
    ans = 0
    while j < n:
        conv_i = B[i][1]
        conv_j = B[j][1]
        max_ps = min(conv_i, conv_j)
        ans += max_ps
        idx_i = B[i][0]
        idx_j = B[j][0]

        tps.append((idx_i + 1, idx_j + 1, max_ps))
        B[i][1] -= max_ps
        B[j][1] -= max_ps

        if B[i][1]:
            j += 1
        else:
            if B[j][1]:
                i = j
                j = i + 1
            else:
                break

    print(ans)

    for tp in tps:
        for _ in range(tp[2]):
            print(f'{tp[0]} {tp[1]}')
