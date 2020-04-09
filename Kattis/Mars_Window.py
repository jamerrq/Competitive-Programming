import sys

sys.setrecursionlimit(10000)

def isOptimal(y, start = 2018, month = 4):
  if y == start:
    return True
  elif start > y:
    return False
  elif month + 2 > 12:
    return isOptimal(y, start + 3, month - 10)
  else:
    return isOptimal(y, start + 2, month + 2)

y = int(sys.stdin.readline())
b = isOptimal(y)
if b:
  print('yes')
else:
  print('no')