from math import sqrt

class Ponto:
    def __init__(self, x, y):
        self.coordenada_x = x
        self.coordenada_y = y
    
    def distancia_entre_pontos(self, ponto):
        return sqrt((self.coordenada_x - ponto.coordenada_x) ** 2 + (self.coordenada_y - ponto.coordenada_y) ** 2)
