from collections import defaultdict
import time

inicio = time.time()

class Grafo: 
    def __init__(self,vertices): 
        #dicionário contendo lista de adjacências
        self.grafo = defaultdict(list)
        #numero de vertice
        self.V = vertices 
  
    #adiciona uma aresta ao grafo 
    def addEdge(self,u,v): 
        self.grafo[u].append(v) 
  
    #funcao recursiva usada por topologicaSort
    def topologicaRecu(self,v,visitado,pilha): 
  
        #marcar o nó atual como visitado
        visitado[v] = True
  
        #repetir para todos os vértices adjacentes a esse vértice
        for i in self.grafo[v]: 
            if visitado[i] == False: 
                self.topologicaRecu(i,visitado,pilha) 
  
        #empurra o vértice atual para a pilha, que armazena o resultado 
        pilha.insert(0,v) 
  
    # executa a classificacao topologica
    # topologicaRecu() 
    def topologicaSort(self): 
        #marca os vertice nao visitados
        visitado = [False]*self.V 
        pilha =[] 
  
        #ordena os vertices um por um
        for i in range(self.V): 
            if visitado[i] == False: 
                self.topologicaRecu(i,visitado,pilha) 

        print (pilha) 
  
g = Grafo(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print("\n Topologia do grafo fornecido:")
g.topologicaSort()

fim = time.time()
print("\ntempo de execucao:", fim - inicio)