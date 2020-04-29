import sys

n, m = map(int, sys.stdin.readline().split())

line = sys.stdin.readline().split()
nums = list(map(int, line))

maxi = n - sum(nums)
print(max(-1, maxi))
