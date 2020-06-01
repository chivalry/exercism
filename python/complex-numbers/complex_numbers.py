from math import cos, sin, e


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        numer = self.real * other.real + self.imaginary * other.imaginary
        denom = other.sum_squares()
        real = numer / denom
        numer = self.imaginary * other.real - self.real * other.imaginary
        imaginary = numer / denom
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        return self.sum_squares() ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self):
        x = e ** self.real
        real = cos(self.imaginary)
        imaginary = sin(self.imaginary)
        return ComplexNumber(x, 0) * ComplexNumber(real, imaginary)

    def sum_squares(self):
        return self.real ** 2 + self.imaginary ** 2
