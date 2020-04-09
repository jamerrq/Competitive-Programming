import sys

def check(n):
    if len(n) % 2 != 0:
        n = '0' + n
    c = 0
    for i in range(len(n)):
        p = int(n[i])
        if i % 2 == 0:
            p *= 2
            while p > 9:
                p = (p % 10) + (p // 10)
        c += p
    return c % 10 == 0

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().split()[0]
    if check(s):
        print('PASS')
    else:
        print('FAIL')
