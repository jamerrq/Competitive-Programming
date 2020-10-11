import sys

n, r = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

count = 0

prevs = [0] * n
freqs = {}

for i in range(n):
    num = nums[i]
    freqs[num] = freqs.get(num, 0) + 1

print(count)
