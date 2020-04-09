import sys


def ssd(b, n):
    sum_ssd = 0
    while n > 0:
        a = n % b
        sum_ssd += a**2
        n //= b
    return sum_ssd


p = int(sys.stdin.readline())

for i in range(p):
    line = sys.stdin.readline().split()
    k, b, n = int(line[0]), int(line[1]), int(line[2])
    print(i + 1, ssd(b, n))
