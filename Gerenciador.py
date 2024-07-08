from ponto import Ponto
from circulo import Circulo
from quadrado import Quadrado
from retangulo import Retangulo
from triangulo import TrianguloEquilatero
from trapezio import Trapezio

class Gerenciador:
    def __init__(self):
        self.formas = []
        self.pontos = []

    def criar_forma(self, forma):
        self.formas.append(forma)
    
    def listar_formas(self):
        return self.formas
    
    def definir_ponto(self, ponto):
        self.pontos.append(ponto)
    
    def calcular_dist(self, ponto1, ponto2):
        return ponto1.distancia_entre_pontos(ponto2)
    
    def verificar_relacao_ponto_forma(self, ponto, forma):
        if isinstance(forma, Circulo):
            return ponto.distancia_entre_pontos(Ponto(0, 0)) <= forma.raio
        elif isinstance(forma, Quadrado):
            lado = forma.lado / 2
            return abs(ponto.coordenada_x) <= lado and abs(ponto.coordenada_y) <= lado
        elif isinstance(forma, Retangulo):
            largura = forma.base / 2
            altura = forma.altura / 2
            return abs(ponto.coordenada_x) <= largura and abs(ponto.coordenada_y) <= altura
        elif isinstance(forma, TrianguloEquilatero):
            altura = forma.altura()
            return ponto.coordenada_y <= altura
        elif isinstance(forma, Trapezio):
            return abs(ponto.coordenada_x) <= forma.base_maior and ponto.coordenada_y <= forma.altura
        return False

    def inicializar(self):
        print("Programa inicializado")
    
    def encerrar(self):
        print("Programa encerrado")
