from ponto import Ponto
from circulo import Circulo
from quadrado import Quadrado
from retangulo import Retangulo
from triangulo import TrianguloEquilatero
from trapezio import Trapezio
from gerenciador import Gerenciador

def main():
    gerenciador = Gerenciador()
    gerenciador.inicializar()

    # Criar formas geométricas
    circulo = Circulo(5)
    quadrado = Quadrado(4)
    retangulo = Retangulo(3, 6)
    triangulo = TrianguloEquilatero(4)
    trapezio = Trapezio(6, 4, 5, 3, 3)

    gerenciador.criar_forma(circulo)
    gerenciador.criar_forma(quadrado)
    gerenciador.criar_forma(retangulo)
    gerenciador.criar_forma(triangulo)
    gerenciador.criar_forma(trapezio)

    # Listar formas
    formas = gerenciador.listar_formas()
    for forma in formas:
        print(f"Forma: {type(forma).__name__}, Área: {forma.area()}")

    # Definir pontos
    ponto1 = Ponto(1, 2)
    ponto2 = Ponto(3, 4)
    ponto3 = Ponto(5, 5)

    gerenciador.definir_ponto(ponto1)
    gerenciador.definir_ponto(ponto2)
    gerenciador.definir_ponto(ponto3)

    # Calcular distância
    distancia = gerenciador.calcular_dist(ponto1, ponto2)
    print(f"Distância entre ponto1 e ponto2: {distancia}")

    # Verificar relações ponto-forma
    print(f"Ponto1 está dentro do círculo? {gerenciador.verificar_relacao_ponto_forma(ponto1, circulo)}")
    print(f"Ponto2 está dentro do quadrado? {gerenciador.verificar_relacao_ponto_forma(ponto2, quadrado)}")
    print(f"Ponto3 está dentro do retângulo? {gerenciador.verificar_relacao_ponto_forma(ponto3, retangulo)}")
    print(f"Ponto3 está dentro do triângulo? {gerenciador.verificar_relacao_ponto_forma(ponto3, triangulo)}")
    print(f"Ponto1 está dentro do trapézio? {gerenciador.verificar_relacao_ponto_forma(ponto1, trapezio)}")

    gerenciador.encerrar()

if __name__ == "__main__":
    main()
