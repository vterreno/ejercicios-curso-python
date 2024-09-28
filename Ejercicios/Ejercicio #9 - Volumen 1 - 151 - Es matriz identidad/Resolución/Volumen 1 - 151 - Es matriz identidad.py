def split(cadena,sep):

    largo_vector = 100
    vector_salida = [None] * largo_vector
    vector_pos_sep = [None] * largo_vector
    cont_pos = -1

    #Buscamos las posiciones del carácter sep
    for i in range(len(cadena)):
        if cadena[i : i+1] == sep:
            cont_pos = cont_pos + 1
            vector_pos_sep[cont_pos] = i

    #Los intervalos dentro de vector_pos_sep nos definen palabras, separadas por sep
    if cont_pos != -1: #Si el usuario ingresó un sep que no está en cadena, no procesamos nada.
    
        cont_pos = 0

        for i in range(largo_vector):
            if vector_pos_sep[i] != None:

                if i == 0:
                    vector_salida[cont_pos] = int(cadena[0: vector_pos_sep[cont_pos]])

                else:
                    vector_salida[cont_pos + 1] = int(cadena[vector_pos_sep[cont_pos] + 1 : vector_pos_sep[cont_pos + 1]])
                    cont_pos = cont_pos + 1
                    
            else: #Completamos el último elemento del vector con una subcadena que va desde el elemento siguiente al último sep hasta el final de la cadena.
                vector_salida[cont_pos + 1] = int(cadena[vector_pos_sep[cont_pos] + 1 : len(cadena)])

        return vector_salida


#INICIALIZACIÓN DE VARIABLES
salir = 0
vector_salida = 100 * [""]
contador = 0

while salir == 0:
    dimension = int(input())
    
    if dimension == 0:
        salir = 1
    else:
        #Definimos una matriz cuadrada, que llenará el usuario
        matriz_usuario = [[int(0) for ind0 in range(dimension)] for ind1 in range(dimension)]
        matriz_identidad = [[int(0) for ind0 in range(dimension)] for ind1 in range(dimension)]
        #Definimos una matriz identidad
        for i in range(dimension):
            for j in range(dimension):
                if i == j:
                    matriz_identidad[i][j] = 1

        #Permitimos que el usuario llene a matriz_usuario con datos
        for num_fila in range(dimension):
            elementos_fila = str(input())

            #Utilizamos la función split para aislar los elementos de esta cadena en un vector
            vector_elementos_fila = split(elementos_fila," ")

            #Vertemos los elementos de este vector en matriz_usuario
            for i in range(dimension):
                if vector_elementos_fila[i] != None:
                    matriz_usuario[num_fila][i] = vector_elementos_fila[i]

        #Comparamos la matriz ingresada por el usuario con la identidad. Si son iguales escribimos si, caso contrario no
        if matriz_usuario == matriz_identidad:
            vector_salida[contador] = "SI"
        else:
            vector_salida[contador] = "NO"

        contador = contador + 1

for i in range(100):
    if vector_salida[i] != "":
        print(vector_salida[i],end = "\n")