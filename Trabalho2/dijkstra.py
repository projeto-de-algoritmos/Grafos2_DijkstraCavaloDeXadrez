import time

inicio = time.time()

#inicializa o grafo
def inicializa_grafo(g, s):
    
    #vertice
    n = len(g)
    
    #distancia
    dist = [None] * n
    
    #origem
    origem = [None] * n
    
    #configuracoes iniciais do grafo
    for v in range(n):
        dist[v] = float("+infinity")
        origem[v] = None
    dist[s] = 0
    return dist, origem

#calcula o menor caminho percorrido 
def minimo(Q, S):
    n = len(Q)
    min = None
    for v in range(n):
        if not S[v]:
           if min == None:
               min = v
           elif Q[v] < Q[min]:
               min = v
    return min

#funcao principal
def dijkstra(g, s):
    dist, origem = inicializa_grafo(g, s)
    
    #comprimento do grafo
    n = len(g)
    
    #conjunto de caminhos minimos
    S = [False] * n
    
    #distancia percorrida
    Q = dist
    
    #arvore geradora minima
    for i in range(n):
        u = minimo(Q, S)
        S[u] = True

        #calcula o peso das aresta (u,v)
        for w, v in g[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                origem[v] = u
        
        print (origem, dist, Q, S)

    return dist, origem

#grafo
def grafo():
    #lista de adjacentes do vertice u que e ligado a (w, v)
    #onde w e o peso da arestas (u, v)
    g = [
        [(10, 1), (5, 3)],
        [(1, 2), (2, 3)],
        [(4, 4)],
        [(3, 1), (9, 2), (2, 4)],
        [(6, 2), (7, 0)]
    ]

    dist, origem = dijkstra(g, 0)
   
    print ("\ntabela distancia =", dist)

    print ("tabela de origem =", origem)

    fim = time.time()
    print("\ntempo de execucao:", fim - inicio)

if __name__ == "__main__":
    grafo()
