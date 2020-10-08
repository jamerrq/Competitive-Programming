f1 = 1
f2 = 2

fs = 2

while f2 < 4e6:
    ft = f2
    f2 += f1
    f1 = ft
    if f2 % 2 == 0:
        fs += f2

print(fs)

