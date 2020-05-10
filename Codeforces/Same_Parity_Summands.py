import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    
    yes = False
    
    if (n - (k - 1) * 2) % 2 == 0 and k * 2 <= n:
        yes = True
        out = [2] * (k - 1)
        out.append(n - (k - 1) * 2)
    
    elif (n - (k - 1)) % 2 != 0 and k <= n:
        yes = True
        out = [1] * (k - 1)
        out.append(n - k + 1)
    
    if yes:
        print('YES')
        print(' '.join([str(x) for x in out]))
    
    else:
        print('NO')
