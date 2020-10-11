import sys


t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))

    c = l[-1]
    index = n - 1
    u = True

    while True:
        # Por si llego al final
        if index < 0:
            break
        # Si voy subiendo
        if u:
            if l[index] >= c:
                c = l[index]
                index -= 1
            else:
                u = False
        # Si empecé a bajar
        else:
            if l[index] <= c:
                c = l[index]
                index -= 1
            else:
                break

    print(index + 1)
