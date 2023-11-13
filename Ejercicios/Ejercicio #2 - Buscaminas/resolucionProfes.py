def separarCadena (cadena):
    vector = [""] * len(cadena)
    for i in range(len(cadena)):
        vector[i] = cadena[i]
    return vector

def contarMinasAlrededor(y, tablero):
    contador = 0
    for i in range(y+1):
        for j in range(y+1):
            if tablero[i][j] == '*':
                contador += 1
    return contador

def celdasVacias(columnas, filas, tablero):
    contador = 0
    
    for y in range(1, filas-1):
        for x in range(1, columnas-1):
            if tablero[y][x] == '-':
                minas_alrededor = contarMinasAlrededor(y, tablero)
                if minas_alrededor >= 6:
                    contador += 1
                    
    return contador

vectorResultados = [0] * 100
a = 0
while True:
    entrada = input()
    ancho = int(entrada[0]) # Columnas
    alto = int(entrada[2]) # Filas
    
    if ancho == 0 and alto == 0:
        break  # Fin de la entrada
    
    tablero = [[str() for ind0 in range(ancho)] for ind1 in range(alto)]
    for i in range(alto):
            linea = str(input())
            linea = separarCadena(linea)
            for k in range(ancho):
               tablero[i][k] = linea[k] 
    
    vectorResultados[a] = celdasVacias(ancho, alto, tablero)
    a += 1

for i in range(a):
    print(vectorResultados[i])
