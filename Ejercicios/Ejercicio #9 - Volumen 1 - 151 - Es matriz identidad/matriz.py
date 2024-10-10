#problema de matrices 09

resultados = [] * 10 #vector para almacenar los resultados

def es_matriz_identidad(matriz, n):
    for i in range(n):
        for j in range(n):
            if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
                return False
    return True

#lectura de la entrada
while True:
    n = int(input()) 
    if n == 0:  
        break
    
    matriz = [[0] * n for i in range(n)]

    for i in range(n):
        fila = input()  
        num = ""  
        col = 0  
        for caracter in fila:
            if caracter != " ":  
                num += caracter
            else:
                if num:  
                    matriz[i][col] = int(num)
                    num = ""  
                    col += 1
        if num:
            matriz[i][col] = int(num)
    
    #verificamos si es matriz identidad
    if es_matriz_identidad(matriz, n):
        resultados += ["SI"]
    else:
        resultados += ["NO"]

#imprimimos todos los resultados juntos
for resultado in resultados:
    print(resultado)