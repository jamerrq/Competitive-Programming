import sys


n = int(sys.stdin.readline())

m = {}
c = {}
ans = 0

for _ in range(n):

    name = sys.stdin.readline().strip()

    if not m.get(name[0]):
        m[name[0]] = {}

    m[name[0]][name] = m[name[0]].get(name, 0) + 1
    c[name[0]] = c.get(name[0], 0) + 1

for key in m.keys():
    for name in m[key].keys():
        ans += m[key][name] * (c[key] - m[key][name])


print(ans)
