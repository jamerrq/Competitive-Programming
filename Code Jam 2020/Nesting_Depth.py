import sys

t = int(sys.stdin.readline())

for k in range(t):
    s = sys.stdin.readline().split()[0]
    n = ''
    i = 0
    while i < len(s):
        if s[i] == '1':
            n += '('
            while i < len(s):
                if s[i] == '0' or i == len(s) - 1:
                    if s[i] == '1':
                        n += '1)'
                    else:
                        n += ')0'
                        break
                else:
                    n += s[i]
                i += 1
        else:
            n += s[i]
        i += 1

    print('Case #{}: {}'.format(k + 1, n))
