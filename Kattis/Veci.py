import sys

n = int(sys.stdin.readline())

def isMax(a):
  if len(a) < 2:
    return True
  if int(a[0]) < int(a[1]):
    return False
  return isMax(a[1:])

def sameDigits(a, b):
  if len(a) == 0 or len(b) == 0:
    return True
  if len(a) == 0:
    return False
  if len(b) == 0:
    return False
  if len(a) != len(b):
    return False
  if a.count(b[0]) == 0:
    return 0
  a.remove(b[0])
  b = b[1:]
  return sameDigits(a, b)

if isMax(list(str(n))):
  print(0)
else:
  m = n + 1
  while(not sameDigits(list(str(n)), list(str(m)))):
    m += 1
  print(m)