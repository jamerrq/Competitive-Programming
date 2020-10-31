import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def primes(num):

    n = num
    sieve = [True] * n
    sieve[0] = False
    nums = [i + 1 for i in range(n)]

    for i in range(1, n):
        if sieve[i]:
            for j in range(i + nums[i], n, nums[i]):
                sieve[j] = False

    primes = [nums[i] for i in range(n) if sieve[i]]
    return primes


X = read()
primes = primes(X)

ans = 0
curr = 0

while X > 1:
    prime = primes[curr]
    if X % prime == 0:
        X //= prime
        ans += 1
    else:
        curr += 1

print(ans)
