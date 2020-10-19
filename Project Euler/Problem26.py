def longest(n, d, acc=set(), div=''):
    if n in acc or n == 0:
        return div
    m = (n * 10) // d
    acc.add(n)
    return longest(n * 10 - d * m, d, acc, div + str(m))


maxs = ''
k = 0

for i in range(1, 1000):
    li = longest(1, i, set())
    if len(li) > len(maxs):
        maxs = li
        k = i

print(k)
