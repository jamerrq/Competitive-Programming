import sys

s, w = map(int, sys.stdin.readline().split())

if w < s:
  print('safe')
else:
  print('unsafe')
