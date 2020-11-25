import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    nums = [n - i for i in range(n)]
    if n % 2:
        m = n // 2
        nums[m], nums[m - 1] = nums[m - 1], nums[m]
    print(*nums)
