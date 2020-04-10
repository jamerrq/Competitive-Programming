import sys

n = int(sys.stdin.readline())

bills = [100, 20, 10, 5, 1]
nbills = 0

for i in range(5):
    amount = n // bills[i]
    nbills += amount
    n -= amount * bills[i]
    if n == 0:
        break

print(nbills)
