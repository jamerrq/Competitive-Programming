import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    mapi = {}
    yes = False

    for i in range(n):
        #print(mapi)
        num = l[i]
        if mapi.get(num):
            if abs(i + 1 - mapi[num]) > 1:
                yes = True
                break
        else:
            mapi[num] = i + 1

    #print(mapi)
    if yes:
        print('YES')
    else:
        print('NO')
