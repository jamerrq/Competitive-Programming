import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    l1, r1, l2, r2 = readList()
    ans = float('inf')
    if l1 >= l2 and l1 <= r2:
        ans = l1
    if l2 >= l1 and l2 <= r1:
        ans = min(ans, l2)
    
    ans = min(ans, l1 + l2)
    print(ans)
