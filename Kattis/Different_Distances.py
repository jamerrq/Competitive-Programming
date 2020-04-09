import sys

while True:
    line = sys.stdin.readline().split()
    if len(line) == 1:
       break
    x1 = float(line[0])
    y1 = float(line[1])
    x2 = float(line[2])
    y2 = float(line[3])
    p = float(line[4])
    distance = pow(pow(abs(x1 - x2), p) + pow(abs(y1 - y2), p), 1 / p)
    print(distance)