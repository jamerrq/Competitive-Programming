import sys


n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort(reverse=True)
sol = [n]

for i in range(k):
    while not (n % nums[i]):
        n //= nums[i]
        sol.append(n)


if n != 1:
    print(-1)
else:
    print(' '.join([str(x) for x in sol[::-1]]))
