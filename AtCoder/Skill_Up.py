import sys

n, m, x = map(int, sys.stdin.readline().split())

prices = []
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    prices.append(nums)


min_price = 0
skills = []
