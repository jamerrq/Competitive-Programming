import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    possible = True
    bina = '{0:b}'.format(a)
    binb = '{0:b}'.format(b)
    #
    j = 0
    for i in range(min(len(bina), len(binb))):
        if bina[i] != binb[i]:
            possible = False
            break
        j += 1

    zeros = 0
    if a > b:
        while j < len(bina):
            if bina[j] != '0':
                possible = False
                break
            j += 1
            zeros += 1

    else:
        while j < len(binb):
            if binb[j] != '0':
                possible = False
                break
            j += 1
            zeros += 1
    
    if possible:
        ops = 0
        while zeros > 0:
            if zeros > 3:
                ops += zeros // 3
                zeros %= 3
            else:
                zeros = 0
                ops += 1
        print(ops)
    else:
        print(-1)
