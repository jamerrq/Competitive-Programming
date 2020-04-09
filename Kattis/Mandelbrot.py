import sys

sys.setrecursionlimit(100000)


class Complex(object):

    def __init__(self, real=.0, imaginary=.0):
        self.real = real
        self.imaginary = imaginary

    def square(self):
        return Complex(self.real ** 2 - self.imaginary ** 2, 2 * self.real * self.imaginary)

    def module(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def complex_sum(self, complex_number):
        return Complex(self.real + complex_number.real, self.imaginary + complex_number.imaginary)


def is_in_set(complex_number, c, rt):
    if complex_number.module() > 2:
        return False
    if rt == 0:
        return True
    return is_in_set(complex_number.square().complex_sum(c), c, rt - 1)


count = 1

for line in sys.stdin:
    data = line.split()
    x, y, r = float(data[0]), float(data[1]), int(data[2])
    ci = Complex(x, y)
    if is_in_set(Complex(), ci, r):
        print('Case {}: IN'.format(count))
    else:
        print('Case {}: OUT'.format(count))
    count += 1
