from collections import defaultdict
import time

inicio = time.time()

class Grafo: 
    def __init__(self,vertices): 
        #dicionario contendo lista de adjacencias
        self.grafo = defaultdict(list)
        #numero de vertice
        self.V = vertices 
  
    #adiciona uma aresta ao grafo 
    def addEdge(self,u,v): 
        self.grafo[u].append(v) 
  
    #funcao recursiva usada por topologicaSort
    def topologicaRecursiva(self,v,visitado,vetor): 
  
        #marcar o no atual como visitado
        visitado[v] = True
  
        #repetir para todos os vertices adjacentes a esse vertice
        for i in self.grafo[v]: 
            if visitado[i] == False: 
                self.topologicaRecursiva(i,visitado,vetor) 
  
        #empurra o vertice atual para a vetor, que armazena o resultado 
        vetor.insert(0,v) 
  
    # executa a classificacao topologica
    # topologicaRecursivarsiva() 
    def topologicaSort(self): 
        #marca os vertice nao visitados
        visitado = [False]*self.V 
        vetor =[] 
  
        #ordena os vertices um por um
        for i in range(self.V): 
            if visitado[i] == False: 
                self.topologicaRecursiva(i,visitado,vetor)
                print("Vetor: ", vetor)

  
g = Grafo(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print("\n Topologia do grafo 1:")
print("\n")
g.topologicaSort()

g1 = Grafo(10) 
g1.addEdge(5, 1); 
g1.addEdge(5, 0); 
g1.addEdge(4, 3); 
g1.addEdge(4, 2); 
g1.addEdge(3, 2); 
g1.addEdge(3, 1);
g1.addEdge(8, 7);
g1.addEdge(6, 9);
g1.addEdge(6, 5);
g1.addEdge(9, 0);

print("\n Topologia do grafo 2:")
print("\n")
g1.topologicaSort()

fim = time.time()
print("\n")
print("Tempo de execucao:", fim - inicio)
