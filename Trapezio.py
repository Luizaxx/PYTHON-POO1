from math import sqrt
from forma import Forma

class Trapezio(Forma):
    def __init__(self, base_maior, base_menor, altura, l1, l2):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = l1
        self.lado2 = l2
    
    def area(self):
        return ((self.base_maior + self.base_menor) * self.altura) / 2
    
    def perimetro(self):
        return self.base_maior + self.base_menor + self.lado1 + self.lado2
    
    def base_media(self):
        return (self.base_maior + self.base_menor) / 2
    
    def mediana(self):
        return (self.base_maior - self.base_menor) / 2
