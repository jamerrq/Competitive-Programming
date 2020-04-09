import sys

n = int(sys.stdin.readline())

j = sys.stdin.readline().split()

min = float('Inf')
ind = -1

for i in range(n):
  k = int(j[i])
  if k < min:
    min = k
    ind = i
    if k == 1:
      print(ind)
      ind = -1
      break

if ind != -1:
  print(ind)