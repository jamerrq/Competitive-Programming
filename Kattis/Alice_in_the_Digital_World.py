import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
while t:
    n, m = readList()
    answ = m
    nums = readList()
    for i in range(n):
        if nums[i] == m:
            temp  = m
            left  = i - 1
            right = i + 1
            while left >= 0:
                if nums[left] > m:
                    temp += nums[left]
                else:
                    break

                left -= 1

            while right < n:
                if nums[right] > m:
                    temp += nums[right]
                else:
                    break

                right += 1

            answ = max(temp, answ)

    print(answ)
    t -= 1
