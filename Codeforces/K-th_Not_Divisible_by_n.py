import sys

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    avan = (k - 1) // (n - 1)
    cand = n * avan
    k -= avan * (n - 1)
    cand += k
    print(cand)
