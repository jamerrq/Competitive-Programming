import random


# 1st implementation (recursive)
def binpower(a, b):
    if b == 0:
        return 1

    res = binpower(a, b // 2)
    if b % 2:
        return res * res * a
    else:
        return res * res


# 2nd implementation (loop)
def binpower2(a, b):

    res = 1
    while b > 0:
        if b & 1:
            res *= a
        a *= a
        b >>= 1

    return res


# 3rd implementation (mod)
def binpowermod(a, b, m):
    a %= m

    res = 1
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1

    return res


# Let's check
for _ in range(10):
    a = random.randint(1, 100)
    b = random.randint(1, 10)
    m = random.randint(2, 10)
    c = binpowermod(a, b, m)
    d = a ** b % m
    print(c, d)
