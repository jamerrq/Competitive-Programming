import sys


n = int(sys.stdin.readline())
R = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

RnB = sum([(R[i] and not B[i]) for i in range(n)])
BnR = sum([(B[i] and not R[i]) for i in range(n)])

if not RnB:
    print(-1)
else:
    print(BnR // RnB + 1)
