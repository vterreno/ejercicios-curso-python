dimension=int(input())
def carga_matriz(tamaño):
    matriz = [[0 for c in range(tamaño)]for f in range(tamaño)]
    for filas in range(tamaño):
        palabra = input()
        if palabra[-1] == " ": palabra = palabra[0:len(palabra)-1]
        numero,col = "",0
        for i in range(len(palabra)):
            if palabra[i] != " ": numero+=palabra[i]
            else:
                matriz[filas][col] = int(numero)
                col+=1
                numero = ""
        matriz[filas][col] = int(numero)
    return matriz
while dimension!=0:
    bandera=0
    matriz=carga_matriz(dimension)
    for i in range(dimension):
        for j in range(dimension):
            if matriz[i][i]!=1 or (j>i and (matriz[i][j]!=0 or matriz[j][i]!=0)):
                bandera=1
    if bandera==0: print("Si")
    else: print("No")
    dimension=int(input())
