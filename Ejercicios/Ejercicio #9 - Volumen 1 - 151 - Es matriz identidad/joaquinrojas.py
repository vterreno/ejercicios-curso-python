def cuadradaMatriz(arr):
    matriz = [[0 for i in range(arr)] for j in range(arr) ]
    return matriz

def mostrarMatriz(matriz,arr):
    for i in range(arr):
        for j in range(arr):
            print(matriz[i][j],end=" ")
        print(" ")

def rellenarMatriz(matriz,arr):
    for i in range(arr):
        for j in range(arr):
            matriz[i][j]=int(input())
    return matriz

def verificadorDiagonal(matriz,arr):
    flag = True
    # parte superior
    for i in range(arr):
        for j in range(arr):
            if i > j and matriz[i][j] != 0:
               flag = False
               break 
    # parte inferior
    for i in range(arr):
        for j in range(arr):
            if i < j and matriz[i][j] != 0: 
                flag = False
                break
    # diagonal principal 
    for i in range(arr):
        for j in range(arr):
            if matriz[i][i] != 1:
                flag = False
                break
    if flag == True:
        return print("SI")
    else:
        return print("NO")

caso = int(input("Numero caso:"))
i = 0
while i < caso: 
    fila_columna = int(input("Ingrese una fila: "))
    matriz = cuadradaMatriz(fila_columna)
    matriz_dato = rellenarMatriz(matriz,fila_columna)
    mostar = mostrarMatriz(matriz_dato,fila_columna)    
    verifacion = verificadorDiagonal(matriz_dato,fila_columna)
    i+=1