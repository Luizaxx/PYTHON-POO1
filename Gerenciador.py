
from ponto import Ponto
from circulo import Circulo
from quadrado import Quadrado
from retangulo import Retangulo


class GerenciadorDeFormas:
    def __init__(self):
        self.formas = []
    
    def adicionar_forma(self, forma):
        self.formas.append(forma)
    
    def listar_formas(self):
        return [type(forma).__name__ for forma in self.formas]
    
    def verificar_ponto_nas_formas(self, ponto):
        resultados = {}
        for forma in self.formas:
            if hasattr(forma, 'contem_ponto'):
                resultados[type(forma).__name__] = forma.contem_ponto(ponto)
        return resultados


