filas = int(input("Ingrese el número de filas: "))



matriz = [[0 for y in range(filas)] for x in range(filas)]
for x in range(filas):
    for y in range(filas):
        matriz[x][y] = int(input(f"Introduzca el valor para la posición ({x+1},{y+1}): "))

es_identidad = True  # Suponemos que es identidad al inicio


for i in range(filas):
    for j in range(filas):
        if i == j:  
            if matriz[i][j] != 1:
                es_identidad = False
        else:  
            if matriz[i][j] != 0:
                es_identidad = False


if es_identidad:
    print("SI")
else:
    print("NO")
