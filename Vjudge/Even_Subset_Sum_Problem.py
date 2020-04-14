import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    nums = list(map(int, line))

    left = -1
    right = -1

    pair = -1

    for j in range(n):
        if nums[j] % 2 == 0:
            pair = j
            break
        else:
            if left == -1:
                left = j
            right = j
            if left != right:
                break

    if left == right and pair == -1:
        print(-1)
    else:
        if pair != -1:
            print(1)
            print(pair + 1)
        else:
            print(right - left + 1)
            print(left + 1, right + 1)
