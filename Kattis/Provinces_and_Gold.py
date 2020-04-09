import sys

l = sys.stdin.readline().split()
G = int(l[0])
S = int(l[1])
C = int(l[2])
T = 3 * G + 2 * S + C

if T >= 8:
  print('Province or Gold')
elif T >= 6:
  print('Duchy or Gold')
elif T >= 5:
  print('Duchy or Silver')
elif T >= 3:
  print('Estate or Silver')
elif T >= 2:
  print('Estate or Copper')
else:
  print('Copper')