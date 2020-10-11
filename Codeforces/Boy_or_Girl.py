import sys

s = sys.stdin.readline().split()[0]

m = {}
count = 0
for char in s:
    if m.get(char):
        pass
    else:
        m[char] = True
        count += 1


if count % 2 != 0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
