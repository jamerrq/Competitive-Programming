n = 600851475143
l = int(n ** .5)

sieve = [True] * l
maxi = -1

for i in range(1, l):
    if sieve[i]:
        for j in range(2*i + 1, l, i + 1):
            sieve[j] = False
        if n % (i + 1) == 0:
            maxi = i + 1


print(maxi)
