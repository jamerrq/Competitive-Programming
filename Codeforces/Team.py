import sys
 
n = int(sys.stdin.readline())
m = 0
 
for _ in range(n):
    line = sys.stdin.readline().split()
    a, b, c = int(line[0]), int(line[1]), int(line[2])
    if a + b + c < 2:
        m += 1
 
print(n - m)