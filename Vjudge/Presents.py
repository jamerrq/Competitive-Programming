import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()
nums = list(map(int, line))

news = [0] * n
for i in range(n):
    news[nums[i] - 1] = i + 1

print(' '.join([str(x) for x in news]))