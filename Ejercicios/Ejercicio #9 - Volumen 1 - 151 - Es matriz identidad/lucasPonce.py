resultado = ""  # Cadena vacía para acumular los resultados

while True:
    dimension = int(input())

    if dimension == 0:  # Si la dimensión es 0, finaliza el programa
        break
    
    # Creamos la matriz identidad
    matriz_identidad = [[1 if i == j else 0 for j in range(dimension)] for i in range(dimension)]

    matriz_usuario = True  # "Bandera/Flag" para verificar si la matriz es igual a la matriz identidad

    for i in range(dimension):
        fila = input()  # Leemos la fila ingresada por el usuario
        contador, numero = 0, ""

        # Procesamos la fila y comparamos con la matriz identidad
        for caracter in fila:
            if caracter == " ":
                if numero:
                    if int(numero) != matriz_identidad[i][contador]:
                        matriz_usuario = False
                    contador += 1
                    numero = ""
            else:
                numero += caracter

        if numero:  # Comparamos el último número de la fila
            if int(numero) != matriz_identidad[i][contador]:
                matriz_usuario = False

    # Acumulamos los resultados en la primer cadena vacía
    if matriz_usuario:
        resultado += "SI\n"
    else:
        resultado += "NO\n"

print(resultado)