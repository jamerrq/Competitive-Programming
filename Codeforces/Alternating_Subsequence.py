import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    tot = 0
    neg = nums[0] < 0
    maxn = nums[0]
    nums += [-nums[-1]]

    for num in nums:
        if num < 0:
            if neg:
                if maxn < num:
                    maxn = num
            else:
                neg = True
                tot += maxn
                maxn = num
        else:
            if not neg:
                if maxn < num:
                    maxn = num
            else:
                neg = False
                tot += maxn
                maxn = num
    
    print(tot)
