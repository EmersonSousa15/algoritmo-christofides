from sys import maxsize
import networkx as nx # type: ignore
import prim

def readGraph():
    with open("entrada.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
        
    graph = [[int(num) for num in line.split()] for line in texto]
    n = graph.pop(0)[0]
    
    return [n, graph]
    
def main():
    [n, graph] = readGraph()
    
    print(n)
    print(graph)
    
    mst = prim(graph, n)
    print(mst)

main()