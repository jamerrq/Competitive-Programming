import sys

def is_harshad(n):
  s = sum([int(c) for c in str(n)])
  return n % s == 0

def smallest(n):
  while not is_harshad(n):
    n += 1
  return n

n = int(sys.stdin.readline())
print(smallest(n))