
f = 10
c = 10
matriz = [[0 for j in range(c)] for i in range(f)] 
#Ver como meter numero por numero
filas = 1

while filas!=0:
    filas=int(input())
    if filas == 0:
        break
    acum1=0
    acum2=0
    principal=0
    for i in range(filas):
        for j in range(filas):
            matriz[i][j]=str(input())

   
    for x in range(filas):
        for i in range(filas):  #arriba de la diagonal principal
            if x<i: 
                acum1+=matriz[x][i]

    for x in range(filas):
        for i in range(filas):  #debajo de la diagonal principal
            if x>i: 
                acum2+=matriz[x][i]

    if acum1 ==0 or acum2 ==0 :
        print("SI")
    else:
        print("NO")
    
