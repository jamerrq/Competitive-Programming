import sys

n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    b = int(k / 400)
    if b * 400 == k:
        print(str(b))
    else:
        print(str(b + 1))
    
