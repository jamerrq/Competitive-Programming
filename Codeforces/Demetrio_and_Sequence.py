import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
A = readList()
B = [0] * n
C = [0] * n

ans = 'YES'

for i in range(n // 2):
    if abs(A[i] - A[-i - 1]) % 2:
        ans = 'NO'
        break
    else:
        mid = (A[i] + A[-i - 1]) // 2
        C[i] = C[-i - 1] = mid
        B[i] = A[i] - C[i]
        B[-i - 1] = A[-i - 1] - C[-i - 1]


print(ans)
if ans == 'YES':
    C[n // 2] = A[n // 2]
    print(*B)
    print(*C)
