from math import sqrt, pi

class FormaGeometrica:
    def area(self):
        pass

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia_entre_pontos(self, ponto):
        return sqrt((self.x - ponto.x) ** 2 + (self.y - ponto.y) ** 2)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return pi * (self.raio ** 2)
    
    def circunferencia(self):
        return 2 * pi * self.raio
    
    def contem_ponto(self, ponto):
        return ponto.distancia_entre_pontos(Ponto(0, 0)) <= self.raio

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4
    
    def diagonal(self):
        return self.lado * sqrt(2)
    
    def contem_ponto(self, ponto):
        return 0 <= ponto.x <= self.lado and 0 <= ponto.y <= self.lado

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def diagonal(self):
        return sqrt(self.base ** 2 + self.altura ** 2)
    
    def contem_ponto(self, ponto):
        return 0 <= ponto.x <= self.base and 0 <= ponto.y <= self.altura
