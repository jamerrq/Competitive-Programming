import sys

t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    stringM = sys.stdin.readline().split()[0]
    idx, rdx = stringM.index('*'), stringM.rindex('*')
    pre, pos = stringM[:idx], stringM[rdx + 1:]
    midM = ''.join([x for x in stringM[idx:rdx + 1] if x != '*'])
    pos = pos[::-1]
    possible = True
    for _ in range(n - 1):
        string = sys.stdin.readline().split()[0]
        idx, rdx = string.index('*'), string.rindex('*')
        prt, pot = string[:idx], string[rdx + 1:]
        mid = ''.join([x for x in string[idx:rdx + 1] if x != '*'])
        pot = pot[::-1]
        for i in range(min(len(pre), len(prt))):
            if pre[i] != prt[i]:
                possible = False
                break
        if len(prt) > len(pre):
            pre = prt
        for i in range(min(len(pos), len(pot))):
            if pos[i] != pot[i]:
                possible = False
                break
        if len(pot) > len(pos):
            pos = pot
        midM += mid
    stringM = pre + midM + pos[::-1]
    if possible:
        print('Case #{}: {}'.format(k + 1, stringM))
    else:
        print('Case #{}: *'.format(k + 1))
