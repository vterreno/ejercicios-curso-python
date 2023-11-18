def matriz_triangular(matriz, n):
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != 0:
                return "SI"
    return "NO"

while True:
    n = int(input())
    if n == 0:
        break

    matriz = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        matriz.append(fila)

    resultado = matriz_triangular(matriz, n)
    print(resultado)
