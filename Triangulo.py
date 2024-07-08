from math import sqrt
from forma import Forma

class TrianguloEquilatero(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return ((self.lado ** 2) * sqrt(3)) / 4
    
    def altura(self):
        return (self.lado * sqrt(3)) / 2
    
    def perimetro(self):
        return self.lado * 3
