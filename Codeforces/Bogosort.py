import sys
 
n = int(sys.stdin.readline())
 
for _ in range(n):
    m = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort(reverse=True)
    print(' '.join([str(x) for x in nums]))
