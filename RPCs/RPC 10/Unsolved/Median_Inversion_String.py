import sys

def get_sol(k):
    return (-1 + (1 + 4 * (2 * k) ** 0.5)) // 2


n, k = map(int, sys.stdin.readline().split())
cntr = int(get_sol(k)) // 2
left = (n - cntr * 2) // 2
if n % 2:
    print('A' * (left + 1) + 'BA' * cntr + 'B' * left)
    print('A' * left + 'BA' * cntr + 'B' * (left + 1))
else:
    print('A' * left + 'BA' * cntr + 'B' * left)
