import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n < 4:
        print(-1)
    else:
        out = []
        if n == 4:
            print('3 1 4 2')
        elif n % 2 == 0:
            for i in range(2, n + 1, 2):
                out.append(i)
            out.append(n - 3)
            out.append(n - 1)
            out.append(n - 5)
            for i in range(n - 7, 0, -2):
                out.append(i)
            print(' '.join([str(x) for x in out]))
        elif n == 5:
            print('4 2 5 3 1')
        else:
            for i in range(2, n - 5, 2):
                out.append(i)
            out.append(n - 5)
            out.append(n - 1)
            out.append(n - 3)
            for i in range(n, 0, -2):
                out.append(i)
            print(' '.join([str(x) for x in out]))
