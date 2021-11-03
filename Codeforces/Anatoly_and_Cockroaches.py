import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
s = read(str)


def cost_rb(s, reverse=False):
    r = not reverse
    l = len(s)
    wr = 0
    wb = 0
    for i in range(l):
        if r:
            if s[i] != 'r':
                wr += 1
        else:
            if s[i] != 'b':
                wb += 1

        r = not r

    return max(wr, wb)


print(min(cost_rb(s), cost_rb(s, True)))
