import sys

def check(s, t):
    ds = {}
    dt = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        ds[char] = None
        dt[char] = None
    ls = len(s)
    for i in range(ls):
        s_char = s[i]
        t_char = t[i]
        if ds[s_char] is None:
            ds[s_char] = t_char
        else:
            if ds[s_char] != t_char:
                #print(1, i, ds)
                return False
        if dt[t_char] is None:
            dt[t_char] = s_char
        else:
            if dt[t_char] != s_char:
                #print(2, i, ds)
                return False

    return True

n, m = map(int, sys.stdin.readline().split())
stri = sys.stdin.readline().split()[0]

for _ in range(m):
    x, y, l = map(int, sys.stdin.readline().split())
    sx = ''
    sy = ''
    for i in range(l):
        sx += stri[x + i - 1]
        sy += stri[y + i - 1]
    
    if check(sx, sy):
        print('YES')
    else:
        print('NO')
