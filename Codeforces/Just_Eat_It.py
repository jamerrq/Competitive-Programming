import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    nums = list(map(int, line))

    acc = [0] * n
    maxc = nums[0]
    minc = nums[0]
    acc[0] = nums[0]
    yasser = nums[0]
    adel = nums[0]

    for i in range(1, n):
        acc[i] = acc[i - 1] + nums[i]
        if acc[i] < minc:
            minc = acc[i]
        else:
            maxc = acc[i]
        
        if i < n - 1:
            if max(maxc, maxc - minc) > adel:
                adel = max(maxc, maxc - minc)
        else:
            if maxc - minc > adel:
                adel = maxc - minc
        
        yasser += nums[i]
    
    if yasser > adel:
        print('YES')
    else:
        print('NO')
