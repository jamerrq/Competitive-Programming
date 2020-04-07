import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()
b = list(map(int, line))

a = [0] * n

maximum = max(b[0], b[1])

for i in range(n):

    if i == 0:
        a[i] = b[i]
    
    elif i == 1:
        a[i] = b[i] + a[0]
        if a[i] > maximum:
            maximum = a[i]

    else:
        a[i] = b[i] + maximum
        if a[i] > maximum:
            maximum = a[i]

print(' '.join([str(x) for x in a]))
