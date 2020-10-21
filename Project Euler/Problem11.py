matrix = []
file = open('in')
for line in file:
    matrix.append(list(map(int, file.readline().split())))
    print(matrix[-1])
