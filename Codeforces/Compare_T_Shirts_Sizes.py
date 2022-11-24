import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    a, b = readList(str)

    if 'S' in a:
        if 'S' in b:
            xa = a.count('X')
            xb = b.count('X')
            if xa > xb:
                print('<')
            elif xa < xb:
                print('>')
            else:
                # print(xa, xb)
                print('=')

        elif 'M' in b:
            print('<')

        elif 'L' in b:
            print('<')

    elif 'M' in a:
        if 'S' in b:
            print('>')

        elif 'M' in b:
            print('=')

        elif 'L' in b:
            print('<')

    elif 'L' in a:
        if 'S' in b:
            print('>')

        elif 'M' in b:
            print('>')

        elif 'L' in b:
            xa = a.count('X')
            xb = b.count('X')
            if xa > xb:
                print('>')
            elif xa < xb:
                print('<')
            else:
                print('=')
