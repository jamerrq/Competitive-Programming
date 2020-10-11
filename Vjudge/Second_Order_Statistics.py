import sys

n = int(sys.stdin.readline())

nums = set(map(int, sys.stdin.readline().split()))

mini = min(nums)
nums.remove(mini)

if len(nums) > 0:
    print(min(nums))
else:
    print('NO')
