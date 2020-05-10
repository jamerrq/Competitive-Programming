import sys

s = sys.stdin.readline().split()[0]
t = sys.stdin.readline().split()[0]

if s == t[:-1]:
  print('Yes')
else:
  print('No')
