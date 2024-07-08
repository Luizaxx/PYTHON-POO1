from math import sqrt
from forma import Forma

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4
    
    def diagonal(self):
        return self.lado * sqrt(2)
