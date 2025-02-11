import random

# Lista de estados brasileiros (siglas)
estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", 
    "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

# Criando um dicionário para armazenar as distâncias entre os estados
distancias = {}

# Geração de distâncias válida entre os estados
for i in range(len(estados)):
    for j in range(i + 1, len(estados)):
        distancia = random.randint(500, 3000)
        distancias[(estados[i], estados[j])] = distancia
        distancias[(estados[j], estados[i])] = distancia 

def calcular_distancia_total(percurso):
    """Calcula a distância total de um percurso garantindo que todas as distâncias existam."""
    distancia_total = 0
    for i in range(len(percurso) - 1):
        par = (percurso[i], percurso[i + 1])
        if par not in distancias:
            print(f"Erro: Distância entre {percurso[i]} e {percurso[i+1]} não encontrada!")
            return float('inf')
        distancia_total += distancias[par]
    return distancia_total

def tsp_vizinho_mais_proximo_recursivo(estado_atual, nao_visitados, caminho):
    """Versão recursiva da heurística do vizinho mais próximo."""
    if not nao_visitados:
        return caminho

    estados_validos = [estado for estado in nao_visitados if (estado_atual, estado) in distancias]

    if not estados_validos:
        print(f"Erro: Não há estados conectados a {estado_atual}!")
        return caminho

    proximo_estado = min(estados_validos, key=lambda estado: distancias[(estado_atual, estado)])

    return tsp_vizinho_mais_proximo_recursivo(
        proximo_estado, 
        nao_visitados - {proximo_estado}, 
        caminho + [proximo_estado]
    )

# Escolhe um estado inicial aleatório
estado_inicial = random.choice(estados)
caminho_recursivo = tsp_vizinho_mais_proximo_recursivo(estado_inicial, set(estados) - {estado_inicial}, [estado_inicial])
menor_dist_recursivo = calcular_distancia_total(caminho_recursivo)

print("\nMelhor rota encontrada (recursiva):", " → ".join(caminho_recursivo))
print(f"Menor distância total: {menor_dist_recursivo} km")
