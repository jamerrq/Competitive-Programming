import sys

line = sys.stdin.readline().split()[0]

n = len(line)

minx = n

if line.count('X') == 0:
    print(0)
else:
    for i in range(n):
        line = line[i:] + line[:i]
        left = line.index('X')
        right = line.rindex('X')
        cout = 0
        for j in range(left, right):
            if line[j] == '.':
                cout += 1
        if cout < minx:
            minx = cout
    
    print(minx)
