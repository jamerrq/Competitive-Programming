import sys

def write(a,b,c):
    if a + b == c:
        return str(a) + "+" + str(b) + "=" + str(c)
    if a == b + c:
        return str(a) + "=" + str(b) + "+" + str(c)
    if a * b == c:
        return str(a) + "*" + str(b) + "=" + str(c)
    if a == b * c:
        return str(a) + "=" + str(b) + "*" + str(c)
    if a - b == c:
        return str(a) + "-" + str(b) + "=" + str(c)
    if a == b - c:
        return str(a) + "=" + str(b) + "-" + str(c)
    if a / b == c:
        return str(a) + "/" + str(b) + "=" + str(c)
    if a == b / c:
        return str(a) + "=" + str(b) + "/" + str(c)

for i in sys.stdin:
    n = i.split()
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    print(write(a,b,c))
