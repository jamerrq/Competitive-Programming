import sys

n, k = map(int, sys.stdin.readline().split())

mod = n % k

print(min(mod, abs(mod - k)))
