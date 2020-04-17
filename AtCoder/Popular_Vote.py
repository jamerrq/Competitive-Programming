import sys

n, m = map(int, sys.stdin.readline().split())
line = sys.stdin.readline().split()
nums = list(map(int, line))

sumi = sum(nums)
barr = (sumi / (4 * m))

if sum([1 for x in nums if x >= barr]) >= m:
    print('Yes')
else:
    print('No')
