# migrated from python 2.7
from itertools import permutations
import time

inicio = time.time()

def checkio(move_string):
    '''
    Find a length of the shortest path of knight
    '''
    # I'll use Dijkstra ! Shortest path from initial point to all other (in wich there is our objective)
    
    # 1) Get cells' indices (matrix like) from move_string
    s = move_string
    letterToIndex = lambda c:ord(c)-ord('a')
    i0,j0 , i1,j1 = int(s[1])-1,letterToIndex(s[0]) , int(s[4])-1,letterToIndex(s[3])
    
    # 1bis) Initialize the possible displacements (relatives)
    lMoves = [cpl for cpl in permutations([-1,1,-2,2], 2) if abs(cpl[0])+abs(cpl[1]) == 3]
    
    # 2) Dijkstra
    #  nodes : couple (the value of the cost to get there, boolean if it is definitely explored). One per cell
    #  A grid contains the nodes, one per cell...
    grid = [ [(None,False) for j in range(8)] for i in range(8) ]
    tempNodes = { (i0,j0) } # set of couples of indices of nodes visited, but not yet explored.
    grid[i0][j0] = (0,False) # first node has cost 0 (0 shots to get there) and is not definitive, so that I can use it as a strating point for the algorithm
    lastIJ = (i0,j0)
    while tempNodes and lastIJ != (i1,j1):
        i,j = min(tempNodes, key=lambda cpl:grid[cpl[0]][cpl[1]][0]) # Temp node with the smallest cost. Key of Dijkstra's algo.
        # Calculate reachable cells
        for di,dj in lMoves:
            # Does not look at outbound cells
            k,l=i+di,j+dj
            if k not in list(range(8)) or l not in list(range(8)) :
                continue
            # Updates Reachable cell
            cost,bDef = grid[k][l]
            if not cost: # Never seen before, "init"
                cost = grid[i][j][0]+1
                tempNodes.add( (k,l) )
            elif cost and not bDef:
                # Seen, but may change
                # In fact, no. As cost progresses by 1, the following condition will never met.
                if cost > grid[i][j][0]+1:
                    cost = grid[i][j][0]+1
            else: # Do nothing
                pass
            # Updates current cell
            grid[k][l] = cost,True
        tempNodes.remove( (i,j) )
        lastIJ = (i,j)
    
    return grid[i1][j1][0]
    

if __name__ == "__main__":
    # assert checkio("b1-d5") == 2, "First"
    # assert checkio("a6-b8") == 1, "Second"
    # assert checkio("h1-g2") == 4, "Third"
    # assert checkio("h8-d7") == 3, "Fourth"
    # assert checkio("a1-h8") == 6, "Fifth"
    
    teste1 = checkio("b1-d5")
    print(teste1)

    fim = time.time()
    print("\n")
    print("Tempo de execucao:", fim - inicio)


