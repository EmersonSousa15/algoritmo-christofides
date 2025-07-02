from sys import maxsize
import networkx as nx # type: ignore
import prim

def readGraph():
    with open("entrada.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
        
    graph = [[int(num) for num in line.split()] for line in texto]
    n = graph.pop(0)[0]
    
    return [n, graph]

def prim(g, n):
    
    #Guarda a distância mínima atual dos vértices da MST para os que estão fora dela
    key = [maxsize] * n 
    
    #Guarda o vértice e seu pai/antecessor, u (filho) e v (pai)
    parent = [None] * n
    
    #Define os vérticas que já estão na MST
    inMST = [False] * n
    
    #Vértice inicial
    key[0] = 0
    parent[0] = -1
    
    for _ in range(n - 1):
        #Busca os vértices que estão fora da MTS e após isso returna o com menor custo
        u = min((v for v in range(n) if not inMST[v]), key=lambda v: key[v])
        inMST[u] = True
        
        for v in range(n):
            #Pula os vértices que já estão na MST e para os que não estão verifica se o custo para alcançá-lo é menos do que o atual, caso sim, substitui
            if g[u][v] and not inMST[v] and g[u][v] < key[v]:
                key[v] = g[u][v]
                parent[v] = u

    
def main():
    [n, graph] = readGraph()
    
    print(n)
    print(graph)
    
    mst = prim(graph, n)
    print(mst)
    
    '''
    Verificar corretude do retorno
    '''
    G = nx.Graph()

    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    mst = nx.minimum_spanning_tree(G, algorithm="prim")

    print("Arestas na MST:")
    for u, v, data in mst.edges(data=True):
        print(f"{u} - {v} com peso {data['weight']}")
    
main()