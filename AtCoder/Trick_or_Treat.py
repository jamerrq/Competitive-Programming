import sys
     
n, k = map(int, sys.stdin.readline().split())
     
snukes = [1] * n
     
for _ in range(k):
  n = int(sys.stdin.readline())
  nums = list(map(int, sys.stdin.readline().split()))
  for num in nums:
    snukes[num - 1] = 0

print(sum(snukes))
