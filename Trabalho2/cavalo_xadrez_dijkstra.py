# migrated from python 2.7
from itertools import permutations
import time

inicio = time.time()

def movimento(coord):
    
    # Obtem indices das celulas a partir da coord
    s = coord
    letterToIndex = lambda c:ord(c)-ord('a')
    i0,j0 , i1,j1 = int(s[1])-1,letterToIndex(s[0]) , int(s[4])-1,letterToIndex(s[3])
    
    # Inicialize os possíveis deslocamentos (parentes)
    lMoves = [cpl for cpl in permutations([-1,1,-2,2], 2) if abs(cpl[0])+abs(cpl[1]) == 3]
    
    # Dijkstra
    # Construcao da matriz
    grid = [ [(None,False) for j in range(8)] for i in range(8) ]
    tempNodes = { (i0,j0) } # conjunto de pares de índices de nos visitados, mas ainda nao explorados
    grid[i0][j0] = (0,False) # O primeiro no custou 0 para chegar la
    lastIJ = (i0,j0)
    while tempNodes and lastIJ != (i1,j1):
        i,j = min(tempNodes, key=lambda cpl:grid[cpl[0]][cpl[1]][0]) # Temp node with the smallest cost. Key of Dijkstra's algo.
        # Calcula celulas alcancavel
        for di,dj in lMoves:
            # Nao examina celulas de saida
            k,l=i+di,j+dj
            if k not in list(range(8)) or l not in list(range(8)) :
                continue
            # Atualiza celulas alcancaveis
            cost,bDef = grid[k][l]
            if not cost: # Never seen before, "init"
                cost = grid[i][j][0]+1
                tempNodes.add( (k,l) )
            elif cost and not bDef:
                # A medida que o custo avanca 1, a seguinte condicao nunca sera atendida
                if cost > grid[i][j][0]+1:
                    cost = grid[i][j][0]+1
            else:
                pass
            # Atualiza celulas atuais
            grid[k][l] = cost,True
        tempNodes.remove( (i,j) )
        lastIJ = (i,j)
    
    return grid[i1][j1][0]
    

if __name__ == "__main__":
    # assert movimento("b1-d5") == 2, "First"
    # assert movimento("a6-b8") == 1, "Second"
    # assert movimento("h1-g2") == 4, "Third"
    # assert movimento("h8-d7") == 3, "Fourth"
    # assert movimento("a1-h8") == 6, "Fifth"
    
    teste1 = movimento("b1-d5")
    print(teste1)

    fim = time.time()
    print("\n")
    print("Tempo de execucao:", fim - inicio)


