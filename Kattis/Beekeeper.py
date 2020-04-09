import sys

n = -1
while n != 0:
    n = int(sys.stdin.readline())
    l = 0
    w = ''
    for i in range(n):
        wt = sys.stdin.readline().split()[0]
        lt = wt.count('aa') + wt.count('ee') + wt.count('ii') + wt.count('oo') + wt.count('uu') + wt.count('yy')
        if len(w) == 0:
            w = wt
            l = lt
        if lt > l:
            l = lt
            w = wt
    print(w)
