import sys
 
n = int(sys.stdin.readline())
 
def bad_ugly_number(t):
 
    if t == 1:
        return -1
 
    if (t - 1) % 3 != 0:
        return int('5' * (t - 1) + '3')
    else:
        return int('5' * (t - 1) + '4')
 
 
for _ in range(n):
    t = int(sys.stdin.readline())
    print(bad_ugly_number(t))
