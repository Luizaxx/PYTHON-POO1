from math import sqrt
from forma import Forma

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def diagonal(self):
        return sqrt(self.base ** 2 + self.altura ** 2)
