import sys


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = [0] * n

for i in range(n):
    arr[i] = int(sys.stdin.readline())


arr.sort()


ans = max(arr) - min(arr)
for i in range(n - k + 1):
    ans = min(ans, arr[i + k - 1] - arr[i])

print(ans)
