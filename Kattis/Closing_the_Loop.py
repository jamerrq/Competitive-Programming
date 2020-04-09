import sys

# Number of cases
n = int(sys.stdin.readline())


def max_sum(l1, l2):
    max_lg = min(len(l1), len(l2))
    l1, l2 = sorted(l1, reverse=True), sorted(l2, reverse=True)
    l1, l2 = l1[:max_lg], l2[:max_lg]
    return sum(l1) + sum(l2) - 2 * max_lg


for i in range(n):
    s = int(sys.stdin.readline())
    l = sys.stdin.readline().split()
    r = [int(t[:-1]) for t in l if t[-1] == 'R']
    b = [int(t[:-1]) for t in l if t[-1] == 'B']
    a = max(max_sum(r.copy(), b.copy()), max_sum(b, r))
    if a < 0:
        a = 0
    print('Case #{}: {}'.format(i + 1, a))
