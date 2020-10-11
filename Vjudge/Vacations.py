    import sys


    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    prev, ans = 0, 0

    for i in range(n):

        if A[i] == 0:
            ans += 1
            prev = 0

        elif A[i] == 1 or A[i] == 2:
            if prev == A[i]:
                ans += 1
                prev = 0
            else:
                prev = A[i]

        else:
            if prev == 0:
                if i < n - 1:
                    if A[i + 1] == 1 or A[i + 1] == 2:
                        prev = 3 - A[i + 1]
            else:
                prev = 3 - prev


    print(ans)
