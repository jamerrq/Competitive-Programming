import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    s = 1
    for i in range(2, n):
        if not n % i:
            s += i

    if n > s:
        print('deficient')
    elif n == s:
        print('perfect')
    else:
        print('abundant')
