import sys

def distancia(cidade1, cidade2):
    # Função para calcular a distância entre duas cidades (pode ser a distância euclidiana, por exemplo)
    return ((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)**0.5

def vizinho_mais_proximo(cidades):
    num_cidades = len(cidades)
    visitados = [False] * num_cidades
    caminho = [0]  # Começamos a partir da primeira cidade

    visitados[0] = True

    for _ in range(num_cidades - 1):
        cidade_atual = caminho[-1]
        cidade_mais_proxima = None
        menor_distancia = sys.maxsize

        for proxima_cidade in range(num_cidades):
            if not visitados[proxima_cidade]:
                d = distancia(cidades[cidade_atual], cidades[proxima_cidade])
                if d < menor_distancia:
                    menor_distancia = d
                    cidade_mais_proxima = proxima_cidade

        caminho.append(cidade_mais_proxima)
        visitados[cidade_mais_proxima] = True

    # Adicionar a última aresta de volta para a cidade inicial para formar um ciclo
    caminho.append(caminho[0])

    return caminho

# Exemplo de uso:
cidades = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
caminho_otimo = vizinho_mais_proximo(cidades)
print("Caminho ótimo:", caminho_otimo)
