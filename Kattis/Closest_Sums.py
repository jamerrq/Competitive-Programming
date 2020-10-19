import sys


case = 1
for line in sys.stdin:
    n = int(line)
    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline()))

    m = int(sys.stdin.readline())
    queries = []
    for _ in range(m):
        queries.append(int(sys.stdin.readline()))

    all = []
    for i in range(n):
        for j in range(i + 1, n):
            all.append(nums[i] + nums[j])

    print('Case {}:'.format(case))
    case += 1

    for num in queries:
        mini = float('inf')
        numq = -1
        for num2 in all:
            if abs(num2 - num) < mini:
                mini = abs(num2 - num)
                numq = num2

        print('Closest sum to {} is {}.'.format(num, numq))
