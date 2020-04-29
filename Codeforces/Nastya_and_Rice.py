import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n, a, b, c, d = map(int, sys.stdin.readline().split())
    mini = n * (a - b)
    maxi = n * (a + b)

    if mini < c - d:
        if maxi >= c - d:
            print('Yes')
        else:
            print('No')
    elif mini >= c - d and mini <= c + d:
        print('Yes')
    else:
        print('No')
