def main():
    dim = int(input('Dim: '))
    while dim <= 50 and dim != 0:
        # llamo a las funciones
        matriz = crear_matriz(dim)
        cargar_matriz(matriz, dim)
        bandera = verificar_identidad(matriz, dim)
        # verifico si es identidad o no
        if bandera == 1:
            print('SI')
        else:
            print('NO')

        dim = int(input('Dim: '))

def crear_matriz(dim):
    matriz = [[0 for i in range(dim)] for j in range(dim)]
    return matriz

def cargar_matriz(matriz, dim):
    for i in range(dim):
        for j in range(dim):
            matriz[i][j] = int(input(f"Pos ({i},{j}): "))
    return matriz

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
