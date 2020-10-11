import sys

nmax = 10 ** 9

sieve = [False] * nmax
nums  = [i + 1 for i in range(nmax)]

sieve[1] = True

for i in range(1, nmax):
    for j in range(i, nmax, nums[i]):
        sieve[j] = True


print([i + 1 for i in range(20) if sieve[i]])
