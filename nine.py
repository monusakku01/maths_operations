import math
from math import sqrt


class Complex(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        # Formats our results
        print(self.real + self.imag)

    def __add__(self, other):
        print('\nSum:')
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        print('\nDifference:')
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        print('\nProduct:')
        return Complex((self.real * other.real) - (self.imag * other.imag),
                       (self.imag * other.real) + (self.real * other.imag))

i = Complex(2, 10j)
k = Complex(3, 5j)
i + k
i - k
i * k
