def main():
    dimension = int(input('Dim: '))
    while dimension <= 50 and dimension != 0:
        # llamo a las funciones
        matriz = crear_matriz_desde_vectores(dimension)
        bandera = verificar_identidad(matriz, dimension)

        # verifico si es identidad o no
        if bandera == 1:
            print('SI')
        else:
            print('NO')

        dimension = int(input('Dim: '))

def crear_matriz_desde_vectores(dimension):
    matriz = []
    for i in range(dimension): # [0] porque solo queremos el primer elemento del vector que son las filas
        filas = vector(input('Fila: '))
        matriz += [filas]

    return matriz

# Convierte la cadena leída en una lista de enteros (un vector)
def vector(cadena):  # cadena es una copia de fila
    v = []  # Inicializa un vector vacío donde se almacenarán los números
    sub = ""  # Inicializa una subcadena vacía para construir cada número de la cadena

    # Itera a través de cada carácter de la cadena
    for i in range(len(cadena)):
        if cadena[i] == " ":  # Si el carácter actual es un espacio
            v += [int(sub)]  # Convierte la subcadena actual en entero y la agrega al vector
            sub = ""  # Reinicia la subcadena para el siguiente número
        else:
            sub = sub + cadena[i]  # Agrega el carácter actual a la subcadena

    # Al final del bucle, agrega la última subcadena al vector si no termina en espacio
    if cadena[len(cadena)-1] != " ":
        v += [int(sub)]  # Convierte la última subcadena en entero y la agrega al vector

    return v  # Devuelve el vector resultante de enteros

def verificar_identidad(matriz, dim):
    for i in range(dim):
        for j in range(dim):
            if i == j: # diagonal principal
                if matriz[i][j] != 1:
                    return 0
            else: # elementos fuera de la diagonal
                if matriz[i][j] != 0:
                    return 0
    # si devuelve 1 es porque los elementos son 1 y 0, en sus ubicaciones correspondientes
    return 1
main()