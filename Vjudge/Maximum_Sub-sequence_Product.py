import sys


for line in sys.stdin:
    values = list(map(int, line.split()))[:-1]
    ans = 1
    for value in values:
        ans = max(ans * value, ans)
    print(ans)
