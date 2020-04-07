import sys

t = int(sys.stdin.readline())

def search(x, n):

    a = '1'
    b = '1'
    g = 0

    for i in range(1, n):
        v = x[i]
        if g == 0:
            if v == '2':
                a += '1'
                b += '1'
            elif v == '1':
                a += '1'
                b += '0'
                g = 1
            else:
                a += '0'
                b += '0'

        elif g == 1:
            if v == '2':
                a += '0'
                b += '2'
            elif v == '1':
                a += '0'
                b += '1'
            else:
                a += '0'
                b += '0'

    return a, b


for _ in range(t):
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().split()[0]
    a, b = search(x, n)
    print(a)
    print(b)
