suma1 = sum([(i + 1) ** 2 for i in range(100)])
suma2 = sum([i + 1 for i in range(100)]) ** 2
print(suma2 - suma1)
