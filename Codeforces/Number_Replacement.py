import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    s = read(str)
    #
    m = {}
    ans = 'YES'
    for i in range(n):
        ai = A[i]
        if m.get(ai):
            if m[ai] != s[i]:
                ans = 'NO'
                break
        else:
            m[ai] = s[i]

    print(ans)
