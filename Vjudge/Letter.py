import sys

s = sys.stdin.readline().split()[0]
n = len(s)

low = [0] * (n + 1)
upp = [0] * (n + 1)

minc = n - 1

for i in range(n):
    if i == 0:
        if s[i].lower() == s[i]:
            low[i + 1] = 1

        if s[-i-1].upper() == s[-i-1]:
            upp[-i-2] = 1
    else:
        low[i + 1] = low[i]
        upp[-i-2] = upp[-i-1]
        if s[i].lower() == s[i]:
            low[i + 1] += 1
        if s[-i-1].upper() == s[-i-1]:
            upp[-i - 2] += 1
    
for i in range(n + 1):
    if low[i] + upp[i] < minc:
        minc = low[i] + upp[i]

print(minc)
