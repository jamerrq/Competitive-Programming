import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    nums = list(map(int, line))
    odd = 0
    eve = 0
    for i in range(n):
        if nums[i] % 2 == 0:
            eve += 1
        else:
            odd += 1
    if odd % 2 != 0:
        print('YES')
    else:
        if eve >= 1 and odd >= 1:
            print('YES')
        else:
            print('NO')
