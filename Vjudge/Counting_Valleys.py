import sys


n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

valley = False
level = 0
ans = 0

for i in range(n):

    if s[i] == 'D':
        level -= 1
    else:
        level += 1

    if level < 0:
        valley = True
    
    if level == 0 and valley:
        ans += 1
        valley = False


print(ans)
