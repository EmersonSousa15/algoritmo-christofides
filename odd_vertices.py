def odd_vertices(edges):
    '''
    edges: lista de tuplas (u, v, w), representando as arestas do grafo
    Retorna uma lista dos vértices com grau ímpar
    '''

    # Cria um dicionário onde a chave é o nome da aresta e o valor é o grau
    grau = {}

    for u, v, _ in edges:
        # Onde tenho a chave u, pego o valor correspondente e somo a 1. Caso a chave ainda não exista, retorno o valor 0
        # Se a chave não existir, o grau[u] cria ela
        grau[u] = grau.get(u, 0) + 1
        grau[v] = grau.get(v, 0) + 1

    return [v for v in grau if grau[v] % 2 == 1]
