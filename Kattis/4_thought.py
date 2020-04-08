import sys

n = int(sys.stdin.readline())

operations = []
results = []

def operation(n1,a,n2):
    if a == '+':
        return n1 + n2
    if a == '-':
        return n1 - n2
    if a == '*':
        return n1 * n2
    return int(n1 / n2)
    

def operation2(n1,a,n2,b,n3):
    if a == '*':
        return operation(n1 * n2, b, n3)
    if a == '/':
        return operation(int(n1 / n2), b, n3)
    if b == '*':
        return operation(n1, a, n2 * n3)
    if b == '/':
        return operation(n1, a, int(n2 / n3))
    if a == '+':
        return operation(n1 + n2, b, n3)
    if a == '-':
        return operation(n1 - n2, b, n3)

def operation3(n1,a,n2,b,n3,c,n4):
    if a == '*':
        return operation2(n1 * n2, b, n3, c, n4)
    if a == '/':
        return operation2(int(n1 / n2), b, n3, c, n4)
    if b == '*':
        return operation2(n1, a, n2 * n3, c, n4)
    if b == '/':
        return operation2(n1, a, int(n2 / n3), c, n4)
    if c == '*':
        return operation2(n1, a, n2, b, n3 * n4)
    if c == '/':
        return operation2(n1, a, n2, b, int(n3 / n4))
    if a == '+':
        return operation2(n1 + n2, b, n3, c, n4)
    if a == '-':
        return operation2(n1 - n2, b, n3, c, n4)

def generateOperations(ops):
        for a in ops:
            for b in ops:
                for c in ops:
                    operations.append('4 ' + a + ' 4 ' + b + ' 4 ' + c + ' 4')
                    results.append(operation3(4,a,4,b,4,c,4))

generateOperations(['+', '*', '-', '/'])

for i in range(n):
    u = int(sys.stdin.readline())
    if u < -60 or u > 256 or results.count(u) == 0:
        print('no solution')
    else:
        print(operations[results.index(u)] + ' = ' + str(results[results.index(u)]))

