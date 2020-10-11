import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    p = []
    u = []
    mapi = {}
    for num in l:

        if mapi.get(num):
            mapi[num] += 1
        else:
            mapi[num] = 1

        if num % 2 == 0:
            p.append(num)
        else:
            u.append(num)

    if len(p) % 2 == 0 and len(u) % 2 == 0:
        print('YES')
    else:
        founded = False
        for num in l:
            if mapi.get(num + 1) or mapi.get(num - 1):
                founded = True
                break
        if founded:
            print('YES')
        else:
            print('NO')
