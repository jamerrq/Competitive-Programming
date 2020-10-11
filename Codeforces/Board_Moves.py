import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    m = [0]
    for i in range(n // 2):
        m.append(8 * (i + 1))
    #print(m)
    s = 0
    for i in range(n // 2 + 1):
        #print(m[i], i)
        s += m[i] * i
    print(s)
