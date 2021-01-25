import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


line = read(str).split(';')
answ = 0
for prob in line:
    nums = prob.split('-')
    if len(nums) > 1:
        answ += int(nums[1]) - int(nums[0]) + 1
    else:
        answ += 1


print(answ)
