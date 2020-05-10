import sys

for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    string = ''

    if a > 0:
        for _ in range(a + 1):
            string += '0'

    if b > 0 and a == 0:
        string += '0'
    
    
    for i in range(b):
        n = 1 - (i % 2)
        string += str(n)
    
    if c > 0:
        if b == 0:
            c += 1
        if b > 0 and b % 2 == 0:
            string = string[:-1]
            for _ in range(c):
                string += '1'
            string += '0'
        else:
            for _ in range(c):
                string += '1'

    print(string)