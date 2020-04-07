import sys
 
n = int(sys.stdin.readline())
 
possible = False
for i in range(1, n):
    j = n - i
    if i % 2 == 0 and j % 2 == 0:
        possible = True
        break
 
if possible:
    print('YES')
else:
    print('NO')