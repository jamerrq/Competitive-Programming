import sys
 
n = int(sys.stdin.readline())
 
for _ in range(n):
    line = sys.stdin.readline().split()
    a, b = int(line[0]), int(line[1])
    if a % b == 0:
        print('YES')
    else:
        print('NO')
