import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()
nums = list(map(int, line))

maxi = max(nums)

freq = [0] * maxi

for i in range(n):
    freq[nums[i] - 1] += 1

added = [0] * maxi
added[0] = freq[0] * 1
added[1] = max(freq[1] * 2, added[0])

for i in range(2, maxi):
    added[i] = max(freq[i] * (i + 1) + added[i - 2], added[i - 1])

print(added[-1])
