def crear_matriz(dimension):
    identidad = [[1 if i == j else 0 for j in range(dimension)] for i in range(dimension)]
    return identidad

def imprimir_resultados(resultados):
    for resultado in resultados:
        print(resultado)

def matriz_identidad():
    resultados = []  #donde almacenaremos los resultados
    
    while True: 
        #se solicita la dimensión de la matriz
        n = int(input("Ingresar un numero para la dimension de la matriz:"))
        if n == 0:
            imprimir_resultados(resultados)  #imprimir los resultados acumulados
            print("Programa terminado")
            break
        
        identidad = crear_matriz(n)  #se crea la matriz identidad
        matriz_usuario = []  #inicializar la matriz vacía
        for i in range(n):
            fila = [0] * n  #para crear una fila de ceros
            matriz_usuario += [fila]
        
        print("Ingresar la matriz fila por fila")
        for i in range(n): 
            fila = input(f"Ingrese la fila {i + 1}: ")
            num_actual = ""
            pos = 0
            for caracter in fila:
                if caracter != " ":  #si no es un espacio, se añade al número actual
                    num_actual += caracter
                else:  #si lo es, convertir el número acumulado y ponerlo en la matriz
                    matriz_usuario[i][pos] = int(num_actual)
                    num_actual = ""
                    pos += 1
            if num_actual:  
                matriz_usuario[i][pos] = int(num_actual)
        
        es_identidad = True
        for i in range(n):
            for j in range(n):
                if matriz_usuario[i][j] != identidad[i][j]:
                    es_identidad = False
                    break
                
        if es_identidad:
            resultados += ["SI"]  
        else:
            resultados += ["NO"]

matriz_identidad()
