from ponto import Ponto
from circulo import Circulo
from quadrado import Quadrado
from retangulo import Retangulo
from gerenciador import Gerenciador

def main():
    gerenciador = Gerenciador()
    
    # Criando formas geométricas
    circulo = Circulo(raio=5)
    quadrado = Quadrado(lado=4)
    retangulo = Retangulo(base=3, altura=6)
    
    # Adicionando formas ao gerenciador
    gerenciador.adicionar_forma(circulo)
    gerenciador.adicionar_forma(quadrado)
    gerenciador.adicionar_forma(retangulo)
    
    # Listando formas disponíveis
    formas_disponiveis = gerenciador.listar_formas()
    print("Formas disponíveis:", formas_disponiveis)
    
    # Definindo pontos
    ponto1 = Ponto(1, 2)
    ponto2 = Ponto(3, 4)
    
    # Calculando distância entre pontos e até a origem
    distancia = ponto1.distancia_entre_pontos(ponto2)
    print("Distância entre pontos:", distancia)
    
    distancia_origem = ponto1.distancia_entre_pontos(Ponto(0, 0))
    print("Distância até a origem:", distancia_origem)
    
    # Verificando se pontos estão dentro das formas
    resultados = gerenciador.verificar_ponto_nas_formas(ponto1)
    for forma, contem in resultados.items():
        print(f"O ponto está dentro do {forma}: {contem}")
    
    # Inicializar e encerrar programa
    print("Programa inicializado")
    input("Pressione Enter para encerrar...")
    print("Programa encerrado")

if __name__ == "__main__":
    main()