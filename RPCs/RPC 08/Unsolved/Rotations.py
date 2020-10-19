import sys


def to_binary(num):
    s = ''
    while num > 0:
        s += str(num % 2)
        num //= 10
    return s[::-1]


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    b = bin(n)[2:]
    #print(b)
    #print(to_binary(n))
    ans = 'yes'
    lb = len(b)
    mp = {}
    if lb < 5:
        ans = 'no'
    else:
        for i in range(lb):
            s = b[i]
            for j in range(i + 1, i + 5):
                s += b[j % lb]
            mp[s] = True
    
    #print(mp)
    for num in range(16, 32):
        bn = bin(num)[2:]
        if not mp.get(bn, False):
            #print(bn)
            ans = 'no'
            break
    print(ans)
