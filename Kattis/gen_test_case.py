import random

file = open('in', 'w')

n = 100
file.write(str(n) + '\n')

for i in range(n):
    name = f'player{i + 1}'
    s1 = random.randint(0, 2000000000)
    s2 = random.randint(0, 2000000000)
    s3 = random.randint(0, 2000000000)
    line = ' '.join([str(x) for x in [name, s1, s2, s3]]) + '\n'
    file.write(line)


file.close()
