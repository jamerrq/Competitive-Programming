import sys

t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    print('Case #{}:'.format(k + 1))
    if n < 10:
        for i in range(n):
            print(i + 1, 1)
    else:
        print('1 1')
        print('2 1')
        row = 3
        pos = 2
        n -= 2
        while n > 0:
            if n >= row - 1:
                print('{} 2'.format(row))
                n -= (row - 1)
                row += 1
            else:
                print('{} 1'.format(row - 1))
                n -= 1
                row += 1
