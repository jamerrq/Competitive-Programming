import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

count = 0
for num in nums:
    if freq.get(num + k, 0) > 0:
        count += 1

print(count)
