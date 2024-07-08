from forma import Forma

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

    def circunferencia(self):
        return 2 * 3.14 * self.raio
