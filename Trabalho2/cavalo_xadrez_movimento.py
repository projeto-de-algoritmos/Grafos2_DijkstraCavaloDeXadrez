from itertools import permutations
import time

inicio = time.time()

def movimento(coord):
    
    # Obtem indices das celulas a partir da coord
    s = coord
    indice = lambda c:ord(c)-ord('a')
    i0,j0 , i1,j1 = int(s[1])-1,indice(s[0]) , int(s[4])-1,indice(s[3])
    
    # Inicialize os possiveis deslocamentos (parentes)
    moveL = [cpl for cpl in permutations([-1,1,-2,2], 2) if abs(cpl[0])+abs(cpl[1]) == 3]
    
    # Dijkstra
    # Construcao da matriz
    tabu = [ [(None,False) for j in range(8)] for i in range(8) ]
    nosTemp = { (i0,j0) } # conjunto de pares de indices de nos visitados, mas ainda nao explorados
    tabu[i0][j0] = (0,False) # O primeiro no custou 0 para chegar la
    ultimoIJ = (i0,j0)
    while nosTemp and ultimoIJ != (i1,j1):
        z = 0
        i,j = min(nosTemp, key=lambda cpl:tabu[cpl[0]][cpl[1]][0]) 
        # Calcula celulas alcancavel
        for di,dj in moveL:
            # Nao examina celulas de saida
            k,l=i+di,j+dj
            if k not in list(range(8)) or l not in list(range(8)) :
                continue
            # Atualiza celulas alcancaveis
            cost,bDef = tabu[k][l]
            if not cost:
                cost = tabu[i][j][0]+1
                nosTemp.add( (k,l) )
            elif cost and not bDef:
                # A medida que o custo avanca 1, a seguinte condicao nunca sera atendida
                if cost > tabu[i][j][0]+1:
                    cost = tabu[i][j][0]+1
            else:
                pass
            # Atualiza celulas atuais
            tabu[k][l] = cost,True
        nosTemp.remove( (i,j) )
        ultimoIJ = (i,j)
        
    return tabu[i1][j1][0]
    

if __name__ == "__main__":

    caso1 = movimento("b1-d5")
    caso2 = movimento("a6-b8")
    caso3 = movimento("h1-g2")
    caso4 = movimento("h8-d7")
    caso5 = movimento("a1-h8")
    print(caso1)

    fim = time.time()
    print("\n")
    print("Tempo de execucao:", fim - inicio)
