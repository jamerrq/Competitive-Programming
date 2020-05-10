import sys

a, b, c, k = map(int, sys.stdin.readline().split())

sumi = 0


sumi += min(a, k)
k -= min(a, k)
if k > 0:
  k -= min(b, k)
if k > 0:
  sumi -= min(c, k)
  k -= min(c, k)

print(sumi)
