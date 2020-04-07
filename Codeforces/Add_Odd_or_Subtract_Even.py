import sys
 
t = int(sys.stdin.readline())
 
for i in range(t):
    line = sys.stdin.readline().split()
    a, b = int(line[0]), int(line[1])
    if a == b:
        print(0)
    else:
        if a < b:
            if (b - a) % 2 == 0:
                print(2)
            else:
                print(1)
        else:
            if (a - b) % 2 == 0:
                print(1)
            else:
                print(2)