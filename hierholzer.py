def hierholzer(graph):
    """
    Esta função determina um ciclo euleriano em um grafo G e retorna uma lista representando o circuito euleriano.
    
    graph: um dicionário onde as chaves são nós e os valores são listas de nós adjacentes.
    """

    # Podemos inciar o algoritmo de qualquer vétice
    initial_vertex = next(iter(graph))
    # Lista que armazenará o ciclo euleriano
    eulerian_cycle = []
    # Pilha auxiliar para armazenar os vértices 
    stack = [initial_vertex]

    # Enquanto houver vértices na pilha, continuamos a explorar os seus vizinhos. 
    # Se encontrarmos um vizinho, o removemos do grafo e adicionamos à pilha.
    # Se não houver mais vizinhos, removemos o vértice do topo da pilha e o adicionamos ao ciclo euleriano.
    # Isso garante que visitamos todos os vértices e arestas do grafo, formando um ciclo euleriano ao final.
    while stack:
        current_vertex = stack[-1]
        if graph[current_vertex]:
            next_vertex = graph[current_vertex].pop()
            graph[next_vertex].remove(current_vertex)
            stack.append(next_vertex)
        else:
            eulerian_cycle.append(stack.pop())

    # Invertendo a lista para obter o ciclo euleriano na ordem correta
    return eulerian_cycle[::-1] 