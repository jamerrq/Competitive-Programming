import sys


n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(n):
    if a[i] > 0 and a[i] >= a[k - 1]:
        count += 1


print(count)
