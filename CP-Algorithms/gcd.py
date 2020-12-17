import random


def gcd(a, b):
    if b:
        return gcd(b, a % b)

    return a


for _ in range(10):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    print(a, b, gcd(a, b))
