import sys


inf, sup, n = 1, int(1e6), 25

while n and inf <= sup:

    mid = (inf + sup) // 2
    print(mid)
    sys.stdout.flush()

    que = sys.stdin.readline().strip()
    if que == '<':
        sup = mid - 1
    else:
        inf = mid + 1

    n -= 1


print('!', sup)
sys.stdout.flush()
