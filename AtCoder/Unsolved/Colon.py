import sys
import math

a, b, h, m  = map(int, sys.stdin.readline().split())

a1 = abs(h * 5 - m) * 6
angle = min(a1, 360 - a1)
#print(angle)

c2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle))
print(c2 ** 0.5)
