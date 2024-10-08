def sacar_espacios (cadena):
    n = cadena[0]
    for i in range (1,len(cadena)):
        if cadena[i] != " ":
            n += cadena[i]
    return n
def tiene_diag_principal(matriz,filas):
    contador = 0
    for i in range (filas):
        if matriz[i][i] == 0:
            contador = 1
    if contador == 0:
        return "si"
    else:
        return "no"        
def tiene_0_abajo (matriz,filas):
    contador = 0
    for col in range(0,filas-1):
        for fila in range(1,filas):
            if fila > col:
                if matriz[fila][col] != 0:
                    contador = 1
    if contador == 0:
        return "si"
    else:
        return "no"    
def tiene_0_arriba (matriz,filas):
    contador = 0
    for fila in range(0,filas-1):
        for col in range(1,filas):
            if col > fila:
                if matriz[fila][col] != 0:
                    contador = 1
    if contador == 0:
        return "si"
    else:
        return "no"
    
filas = int(input())
while (filas > 0) and (filas < 50):  # Mientras la dimencion de la matriz sea entre 1 y 49
    matriz = [[int(0)for i in range(filas)]for j in range (filas)]     
    for i in range (filas):
        entrada = input()
        entrada = sacar_espacios(entrada)                             
        for j in range (filas):
            matriz[i][j] = int(entrada[j])      # Matriz definida con sus elementos    
    if tiene_diag_principal(matriz,filas) == "si":       # Verificar si tiene diagonal principal diferente a 0
        if (tiene_0_abajo(matriz,filas) == "si")or(tiene_0_arriba(matriz,filas) == "si"):  # Verificar si tiene todos ceros abajo o arriba
            print("SI")
        else:
            print("NO")
    else:
        print("NO")
    filas = int(input())
    
