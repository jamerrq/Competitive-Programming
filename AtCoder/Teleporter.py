import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

path = []
i = nums[0] - 1
mapi = {}
while True:
    if mapi.get(i):
        break
    else:
        path.append(i)
        mapi[i] = True
    i = nums[i] - 1

print(path)
