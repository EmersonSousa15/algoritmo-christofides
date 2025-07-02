
from sys import maxsize


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
                    
    mst_edges = []
    for v in range(1, n):
        u = parent[v]
        #Adiciona as tuplas à lista (u, v, peso)
        mst_edges.append((u, v, g[u][v]))
         
    return mst_edges