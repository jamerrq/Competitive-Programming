import sys


T = int(sys.stdin.readline())

for k in range(T):
    N = int(sys.stdin.readline())
    f = sys.stdin.readline().strip()
    B = [False] * N
    i = 0
    while i < N:
        if f[i] == '.':
            b1 = i > 0 and B[i - 1]
            b2 = B[i]
            b3 = i < N - 1 and B[i + 1]
            if b1 + b2 + b3 < 1:
                if i < N - 1:
                    B[i + 1] = True
                    i += 1
                else:
                    B[i] = True
        i += 1
    
    print('Case {}: {}'.format(k + 1, sum(B)))
