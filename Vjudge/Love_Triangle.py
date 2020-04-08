import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()
nums = list(map(int, line))

yes = False

for i in range(n):
    if nums[nums[nums[i] - 1] - 1] == i + 1:
        yes = True

if yes:
    print('YES')
else:
    print('NO')
