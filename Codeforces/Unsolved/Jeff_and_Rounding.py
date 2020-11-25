import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def decimal(num):
    return num - int(num)


n = read()
nums = readList(float)
zeros = [x for x in nums if x == x + decimal(x)]
othrs = [x for x in nums if x != x + decimal(x)]

if len(zeros) % 2:
    othrs.append(zeros.pop())

othrs.sort(key=lambda x:decimal(x))

new_nums = othrs[:len(othrs) // 2] + zeros + othrs[len(othrs) // 2:]

for i in range(n):
    new_nums[i] = int(new_nums[i])
    new_nums[- i - 1] = int(new_nums[- i - 1] + 0.999)


diff = abs(sum(nums) - sum(new_nums))
print('{:.3f}'.format(diff))
