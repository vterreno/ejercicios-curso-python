dimTablero = str(input())
dimension= dimTablero.split(" ")
columnas=int(dimension[0])
filas=int(dimension[1])

tablero=[""]*filas
for i in range(filas):
        tablero[i]=[""]*columnas

for i in range(filas):
    for j in range(columnas):
         tablero[i][j]=str(input())

contMinas=0
cont2=0
for i in range(filas):
    for j in range(columnas):
        if i!=0 and j!=0 and i!=(columnas-1) and j!=(filas-1):
            if tablero[i][j]=="-":
                for h in range(3):
                    for z in range(3):
                         if tablero[((i-1)+h)][((j-1)+z)]=="*":
                                contMinas+=1
        if contMinas>=6:
            cont2+=1
            contMinas=0
        else:
            contMinas=0

for filas in tablero:
    print(filas)

print(cont2)

