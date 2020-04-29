import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    answ = nums[0]
    for i in range(1, n):
        if d == 0:
            break
        pile = min(d // i, nums[i])
        answ += pile
        d -= pile * i
    print(answ)
