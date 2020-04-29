import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()
nums = list(map(int, line))

m = len(nums)

freq = [0] * n

for i in range(m):
    freq[nums[i] - 1] += 1

print('\n'.join([str(x) for x in freq]))
