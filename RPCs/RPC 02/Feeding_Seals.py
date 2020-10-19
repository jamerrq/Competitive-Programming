import sys

n, c = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

i = 0
j = n - 1

count = 0

while True:
    if i > j:
        break
    if i == j:
        count += 1
        break
    if nums[i] + nums[j] <= c:
        i += 1
    count += 1
    j -= 1


print(count)
