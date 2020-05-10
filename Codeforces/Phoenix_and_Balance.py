import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    current = 2
    p1 = 2 ** n
    p2 = 0
    for _ in range(n // 2 - 1):
        p1 += current
        current *= 2
    for _ in range(n // 2):
        p2 += current
        current *= 2
    
    print(abs(p1 - p2))
