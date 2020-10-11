import sys


T = int(sys.stdin.readline())

for _ in range(T):
    s = sys.stdin.readline().strip()
    n = len(s)
    v = []
    curr = 0
    for i in range(n):
        if s[i] == '1':
            curr += 1
        else:
            if curr != 0:
                v.append(curr)
            curr = 0
    if curr != 0:
        v.append(curr)
    
    ans = 0
    v.sort(reverse=True)
    for i in range(0, len(v), 2):
        ans += v[i]
    print(ans)
