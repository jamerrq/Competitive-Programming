import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    s1 = list(read(str))
    s2 = list(read(str))
    ans = 0
    for i in range(n):
        if s2[i] == '1':
            if s1[i] == '0':
                ans += 1
                continue
            if i > 0 and s1[i - 1] == '1':
                ans += 1
                continue
            if i < n - 1 and s1[i + 1] == '1':
                s1[i + 1] == '2'
                ans += 1
                continue

    print(ans)
