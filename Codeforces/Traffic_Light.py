import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n, c = readList(str)
    n = int(n)
    s = read(str)

    if c == 'g':
        print(0)
        continue

    searching = False
    index_last_c = -1
    ans = -1
    index_first_g = -1
    first_g_founded = False

    for i in range(n):
        char_i = s[i]
        if char_i == c:
            if not searching:
                searching = True
                index_last_c = i
                continue
            continue
        if char_i == 'g':
            if not first_g_founded:
                first_g_founded = True
                index_first_g = i
            if searching:
                ans = max(i - index_last_c, ans)
                searching = False

    if searching:
        ans = max(ans, n - index_last_c + index_first_g)

    print(ans)
