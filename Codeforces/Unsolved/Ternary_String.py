import sys

t = int(sys.stdin.readline())

for _ in range(t):

    s = sys.stdin.readline().split()[0]
    n = len(s)

    ones = [0] * (n + 1)
    twos = [0] * (n + 1)
    thrs = [0] * (n + 1)

    for i in range(n):
        one = int(s[i] == '1')
        two = int(s[i] == '2')
        thr = int(s[i] == '3')
        ones[i + 1] = ones[i] + one
        twos[i + 1] = twos[i] + two
        thrs[i + 1] = thrs[i] + thr
    
    ones = ones[1:]
    twos = twos[1:]
    thrs = thrs[1:]

    i = 0
    j = n - 1

    while True:

        a = b = False

        n1 = ones[j] - ones[i + 1]
        n2 = twos[j] - twos[i + 1]
        n3 = thrs[j] - thrs[i + 1]

        if n1 > 0 and n2 > 0 and n3 > 0:
            a = True
            i += 1
        
        n1 = ones[j - 1] - ones[i]
        n2 = twos[j - 1] - twos[i]
        n3 = thrs[j - 1] - thrs[i]

        if n1 > 0 and n2 > 0 and n3 > 0:
            b = True
            j -= 1
        
        if not a and not b:
            break
    
    print(i, j, j - i + 1)
