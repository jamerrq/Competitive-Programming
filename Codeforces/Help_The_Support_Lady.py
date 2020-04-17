import sys

t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    nums = list(map(int, line))
    nums.sort()
    timing = 0
    clients = 0

    for num in nums:
        if timing <= num * 2:
            clients += 1
            timing += 2 * num

    print('Case #{}: {}'.format(k + 1, clients))
