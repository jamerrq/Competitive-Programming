import sys

line = sys.stdin.readline().split()
a, b = int(line[0]), int(line[1])
line = sys.stdin.readline().split()
m, s = int(line[0]), int(line[1])


def point_value(x_t, y_t):
    return a * x_t + b * y_t


bestR = 0

if s > m:

    if a*(s - m) + b*(2*m - s) > bestR:
        bestR = a*(s - m) + b*(2*m - s)

    if a*(m - 1) + b > bestR:
        bestR = a*(m - 1) + b

    if a * ((s - 1) // 2) + b > bestR:
        bestR = a * ((s - 1) // 2) + b

else:

    p1 = point_value(1, s - 2)
    if p1 > bestR:
        bestR = p1

    p2 = point_value(1, m - 1)
    if p2 > bestR:
        bestR = p2

    p3 = point_value((s - 1) // 2, 1)
    if p3 > bestR:
        bestR = p3

    p4 = point_value(m - 1, 1)
    if p4 > bestR:
        bestR = p4

print(int(bestR))
