import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


p = read(str)
s = []
index = 0
for char in p:
    if char == 'L':
        index -= 1
    elif char == 'R':
        index += 1
    elif char == 'B':
        s.pop(index - 1)
        index -= 1

    else:
        s.insert(index, char)
        index += 1

    #print(s, index)

print(''.join(s))
