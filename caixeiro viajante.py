import random

# Lista de estados brasileiros (siglas)
estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", 
    "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]
# Gerando distâncias fictícias entre os estados (aproximações em km)
#random.seed(100)  # Para reproduzir os mesmos resultados
distancias = {(a, b): random.randint(500, 3000) for a in estados for b in estados if a != b}
# Como o grafo é não direcionado, adicionamos as distâncias invertidas
for (a, b), d in list(distancias.items()):
    distancias[(b, a)] = d
def calcular_distancia_total(percurso):
    """Calcula a distância total de um percurso passando por todos os estados."""
    distancia = 0
    for i in range(len(percurso) - 1):
        distancia += distancias.get((percurso[i], percurso[i + 1]), float('inf'))
    distancia += distancias.get((percurso[-1], percurso[0]), float('inf'))  # Voltar ao início
    return distancia
def tsp_vizinho_mais_proximo(estados):
    """Heurística do vizinho mais próximo para encontrar um caminho aproximado."""
    estado_atual = random.choice(estados)  # Começa de um estado aleatório
    nao_visitados = set(estados) - {estado_atual}
    caminho = [estado_atual]
    while nao_visitados:
        proximo_estado = min(nao_visitados, key=lambda estado: distancias[(estado_atual, estado)])
        caminho.append(proximo_estado)
        nao_visitados.remove(proximo_estado)
        estado_atual = proximo_estado

    return caminho, calcular_distancia_total(caminho)
# Resolvendo o problema
melhor_rota, menor_dist = tsp_vizinho_mais_proximo(estados)
# Exibindo o resultado
print("Melhor rota encontrada:", " → ".join(melhor_rota))
print(f"Menor distância total: {menor_dist} km")
