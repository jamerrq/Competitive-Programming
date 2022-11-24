import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
M = [read(str) for i in range(n)]
answer = 'YES'

for i in range(n):

    for j in range(n):
        count = 0

        if i > 0:
            count += 1 if M[i - 1][j] == 'o' else 0

        if i < n - 1:
            count += 1 if M[i + 1][j] == 'o' else 0

        if j > 0:
            count += 1 if M[i][j - 1] == 'o' else 0

        if j < n - 1:
            count += 1 if M[i][j + 1] == 'o' else 0

        if count % 2 != 0:
            answer = 'NO'
            break


print(answer)
