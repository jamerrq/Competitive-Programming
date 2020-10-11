import random

n = 100
print(n)
seq = []
for _ in range(n):
    seq.append(random.randint(0, 3))

print(' '.join([str(x) for x in seq]))
