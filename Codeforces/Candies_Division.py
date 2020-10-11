import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    divd = n // k
    n   -= divd * k
    answ = divd * k + min(n, k // 2)
    print(answ)
