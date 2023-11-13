def contadorEstrellas(matriz, dimension):
    bandera = False
    contador = 1
    estrellas = 0
    columna = int((dimension - 1) / 2)
    fila = columna
    while bandera == False:
        # Movimiento arriba: Decremento fila i y mantengo columna j
        if fila - contador + 1>= 0:
            if contador != 1:
                for i in range(fila, fila - contador, -1):
                    estrellas += int(matriz[i][columna])
                fila = fila - contador +1
                contador += 1
                columna = columna + 1
            else:
                for i in range(fila, fila - contador - 1, -1):
                    estrellas += int(matriz[i][columna])
                fila = fila - contador
                contador += 1
                columna = columna + 1
        else:
            for i in range(fila, -1, -1):
                estrellas += int(matriz[i][columna])
            break
        
        # Movimiento derecha: Mantengo i e incremento j
        if (columna + contador - 1) <= (dimension - 1):
            for i in range(columna, columna + contador):
                estrellas += int(matriz[fila][i])
            columna = columna + contador -1
            contador += 1
            fila += 1
        else:
            for i in range(columna, dimension):
                estrellas += int(matriz[fila][i])
            break
        
        # Movimiento abajo: Incremento i y mantengo j
        if (fila + contador - 1) < dimension:
            for i in range(fila, fila + contador):
                estrellas += int(matriz[i][columna])
            fila = fila + contador - 1
            columna -= 1
            contador += 1
        else:
            for i in range(fila, dimension):
                estrellas += int(matriz[i][columna])
            break
        
        # Movimiento izquierda: Mantengo i y decremento j
        if (columna - contador + 1) > -1:
            for i in range(columna, columna - contador, -1):
                estrellas += int(matriz[fila][i])
            columna = columna - contador + 1
            fila -= 1
            contador += 1
        else:
            for i in range(columna, -1, -1):
                estrellas += int(matriz[fila][i])
            break
    return estrellas

def separarNumeros(cadena):
    nums = 0
    for i in range(len(cadena)):
        if cadena[i] == " " or i == len(cadena) - 1:
            nums += 1
    vector = [""] * nums
    indice = 0
    for i in range(len(cadena)):
        if cadena[i] != " ":
            vector[indice] += cadena[i]
        if cadena[i] == " " or i == (len(cadena) - 1):
            indice += 1
    return vector

vectorResultados = [-1] * 1000
dimension = 1
indice = 0
while dimension > 0:
    dimension = int(input())
    if dimension != 0:
        matriz = []
        for i in range(dimension):
            matriz.append(separarNumeros(input()))
        vectorResultados[indice] = contadorEstrellas(matriz, dimension)
        indice += 1
for i in range(1000):
    if vectorResultados[i] != -1:
        print(vectorResultados[i])

""" 

EJEMPLOS
matriz = [[2,4,4,4,4],[2,3,3,4,5],[5,2,2,7,1],[2,1,3,5,3],[2,4,3,1,2]]
matriz = [[3,3,4],[2,2,7],[1,3,5]]
matriz = [[2,1,2,2,3,2,3],[4,2,4,4,4,4,4],[3,2,3,3,4,5,3],[4,5,2,2,7,1,2],[5,2,1,3,5,3,6],[4,2,4,3,1,2,0],[3,9,9,9,9,2,9]]

"""














""" columna = 2
fila = 2
dimension = 5
while bandera == False:
    # Movimiento arriba: Decremento fila i y mantengo columna j
    if fila - contador + 1>= 0:
        if contador != 1:
            for i in range(fila, fila - contador, -1):
                estrellas += int(matriz[i][columna])
            fila = fila - contador +1
            contador += 1
            columna = columna + 1
        else:
            for i in range(fila, fila - contador - 1, -1):
                estrellas += int(matriz[i][columna])
            fila = fila - contador
            contador += 1
            columna = columna + 1
    else:
        for i in range(fila, -1, -1):
            estrellas += int(matriz[i][columna])
        break
    
    # Movimiento derecha: Mantengo i e incremento j
    if (columna + contador - 1) <= (dimension - 1):
        for i in range(columna, columna + contador):
            estrellas += int(matriz[fila][i])
        columna = columna + contador -1
        contador += 1
        fila += 1
    else:
        for i in range(columna, dimension):
            estrellas += int(matriz[fila][i])
        break
    
    # Movimiento abajo: Incremento i y mantengo j
    if (fila + contador - 1) < dimension:
        for i in range(fila, fila + contador):
            estrellas += int(matriz[i][columna])
        fila = fila + contador - 1
        columna -= 1
        contador += 1
    else:
        for i in range(fila, dimension):
            estrellas += int(matriz[i][columna])
        break
    
    # Movimiento izquierda: Mantengo i y decremento j
    if (columna - contador + 1) > -1:
        for i in range(columna, columna - contador, -1):
            estrellas += int(matriz[fila][i])
        columna = columna - contador + 1
        fila -= 1
        contador += 1
    else:
        for i in range(columna, -1, -1):
            estrellas += int(matriz[fila][i])
        break
    
print(estrellas) """
