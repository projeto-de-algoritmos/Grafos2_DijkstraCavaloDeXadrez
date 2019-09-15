
import time

inicio = time.time()

def vaiCavalo(origem, destino):
   
   #matriz 8 por 8 representado o tabuleiro
   casasTestadas = [[False]*8 for i in range(8)]
   passos = [origem+[[]]]

  #movimenta o cavalo ate o mesmo chegar ao destino
   while True:
      proximosPassos = []
      for passo in passos:
         # movimento em L percorrido pelo cavalo
         for movimento in [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]:
            x,y = passo[0]+movimento[0], passo[1]+movimento[1]
            if [x,y] == destino:
               return passo[2]+[[x,y]]
            if 0 <= x < 8 and 0 <= y < 8 and not casasTestadas[x][y]:
               proximosPassos.append([x,y,passo[2]+[[x,y]]])
               casasTestadas[x][y] = True
      passos = proximosPassos

movimentosNecessarios = vaiCavalo([1,1],[1,2])
print(movimentosNecessarios)

fim = time.time()
print("\ntempo de execucao:", fim - inicio)