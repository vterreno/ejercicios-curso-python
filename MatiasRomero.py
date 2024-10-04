resultado = ""

while True:
    dimension = int(input())

    if dimension == 0:
        break

    matriz_identidad = [[1 if i == j else 0 for j in range(dimension)] for i in range(dimension)]

    matriz_usuario_es_identidad = True

    for i in range(dimension):
        fila_usuario = list(map(int, input().split()))

        if fila_usuario != matriz_identidad[i]:
            matriz_usuario_es_identidad = False

    if matriz_usuario_es_identidad:
        resultado += "SI\n"
    else:
        resultado += "NO\n"

print(resultado)
