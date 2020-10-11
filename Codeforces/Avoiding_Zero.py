import sys

def read(func=int):
    return func(sys.stdin.readline())

def read_list(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
while t:
    n = read()
    A = read_list()
    neg = [x for x in A if x < 0]
    pos = [x for x in A if x > 0]
    if -sum(neg) > sum(pos):
        print('YES')
        B = neg + [0] * A.count(0) + pos
        print(' '.join([str(x) for x in B]))
    elif -sum(neg) == sum(pos):
        print('NO')
    else:
        print('YES')
        B = pos + [0] * A.count(0) + neg
        print(' '.join([str(x) for x in B]))
    t -= 1
