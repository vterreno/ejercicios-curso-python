dimension = int(input("Ingrese tamaño de matriz: "))
matriz = [[None for i in range(dimension)]for j in range(dimension)]

for i in range(dimension):
    elementos = input("Ingrese los elementos de cada fila: ")
    for j in range(dimension):
        matriz[i][j] = int(elementos[j])

centro = int((dimension/2) + 0.5)-1

# Declarar variables iniciales
filas = centro
columnas = centro
solucion = matriz[centro][centro]
contador = 1
Flag = True

    
while Flag:
    #Resta 1 fila, sube
    if filas - contador >= 0:
        for i in range(contador):
            filas -= 1
            solucion += matriz[filas][columnas]
        contador +=1
    else:
        for i in range(dimension-1):
            filas -= 1
            solucion += matriz[filas][columnas]
        Flag = False
        contador +=1

    #Sumo 2 columna, derecha
    if Flag:
        if columnas+contador < dimension:
            for i in range(contador):
                columnas += 1
                solucion += matriz[filas][columnas]
            contador += 1
        else:
            for i in range(columnas, dimension-1):
                columnas += 1
                solucion += matriz[filas][columnas]
            Flag = False
            contador +=1
    
    #Sumo 3 filas, abajo
    if Flag:
        if filas + contador < dimension:
            for i in range(contador):
                filas += 1
                solucion += matriz[filas][columnas]
            contador += 1
        else:
            for i in range(dimension-1):
                columnas += 1
                solucion += matriz[filas][columnas]
            Flag = False
            contador +=1


    #Resto 4 columnas, izquierda
    if Flag:
        if columnas - contador >= 0:
            for i in range(contador):
                columnas -= 1
                solucion += matriz[filas][columnas]
            contador +=1
        else:
            for i in range(dimension-1):
                columnas -= 1
                solucion += matriz[filas][columnas]
            Flag = False
            contador +=1
            

print(solucion)

