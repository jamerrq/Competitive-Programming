import sys

n = int(sys.stdin.readline())

neg = 0
pos = 0
zer = 0

line = sys.stdin.readline().split()
nums = list(map(int, line))

coins = 0

for i in range(n):
    if nums[i] < 0:
        neg += 1
        coins += -(nums[i] + 1)
    elif nums[i] > 0:
        pos += 1
        coins += nums[i] - 1
    else:
        zer += 1
        coins += 1

if neg % 2 != 0 and zer == 0:
    coins += 2

print(coins)
