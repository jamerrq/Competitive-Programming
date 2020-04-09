import sys

n = int(sys.stdin.readline())

def ab(a,b,i):
    if i == 0:
        return str(a) + ' ' + str(b)
    return ab(b, a + b, i - 1)

print(ab(1,0,n))
