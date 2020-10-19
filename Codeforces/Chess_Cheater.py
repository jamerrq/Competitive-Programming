import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())
    pv = ''
    w = False
    aux = []
    curr = 0
    for i in range(n):
        if s[i] == 'L':
            if w:
                curr += 1
        else:
            w = True
            if curr > 0:
                aux.append((curr, i - 1))
                curr = 0

    aux.sort()
    #print(aux)
    for i in range(len(aux)):
        maxi = min(aux[i][0], k)
        k -= maxi
        for j in range(maxi):
            s[aux[i][1] - j] = 'W'

    for i in range(n):
        if s[i] == 'L' and k > 0:
            k -= 1
            s[i] = 'W'

    ans = 0
    for i in range(n):
        if s[i] == 'W':
            if i > 0 and s[i - 1] == 'W':
                ans += 2
            else:
                ans += 1

    #print(s)
    print(ans)
