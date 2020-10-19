import sys

h = int(sys.stdin.readline())

def cards(n):
    return (3 * h ** 2 + h) // 2

while cards(h) % 4 != 0:
    h += 1

print(h)
