import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
nums = [read() for _ in range(n)]
miss = [i for i in range(1, nums[-1]) if not i in nums]

if miss:
    print(*miss, sep='\n')
else:
    print('good job')
