import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    s = read(str)
    ans = 'NO'
    if s.endswith('2020'):
        ans = 'YES'
    elif s.endswith('020'):
        if s.startswith('2'):
            ans = 'YES'
    elif s.endswith('20'):
        if s.startswith('20'):
            ans = 'YES'
    elif s.endswith('0'):
        if s.startswith('202'):
            ans = 'YES'
    else:
        if s.startswith('2020'):
            ans = 'YES'
    print(ans)
