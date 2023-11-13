def triangular(matriz, cantFilas):
    for i in range(cantFilas):
        for j in range(cantFilas):
            if i > j and matriz[i][j] != 0:
                return False
            if i < j and matriz[i][j] != 0:
                return False
    return True

cantFilas = int(input())

if 0 < cantFilas < 50:
    matriz = [[0] * cantFilas for i in range(cantFilas)]

    for i in range(cantFilas):
        for j in range(cantFilas):
            matriz[i][j] = int(input())

    for filas in matriz:
        print(filas)

    if triangular(matriz, cantFilas):
        print("SI")
    else:
        print("NO")




"""
cantFilas=int(input())
cantdeCeros=0
if cantFilas>0 and cantFilas<50:
    matriz=[0]*cantFilas
    for i in range(cantFilas):
        matriz[i]=[0]*cantFilas

for i in range(cantFilas):
    for j in range(cantFilas):
        matriz[i][j]=int(input())
        if matriz[i][j]:
            cantdeCeros+=1

for filas in matriz:
    print(filas)


if (i != j and j > i):
    print("SI")

else:
    print("NO")
"""