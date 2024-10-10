while True:
    rango = int(input(''))
    if rango == 0:
        break
    else:
        matriz = [[int() for _ in range(rango)] for _ in range(rango)]
        for e in range(rango):
            elementos = input().split(' ')
            for j in range(rango):
                matriz[e][j] = int(elementos[j])
        estado = True
        for f in range(rango):
            for c in range(rango):
                if f != c and matriz[f][c] != 0:
                    estado = False
                if f == c and matriz[f][c] != 1:
                    estado = False
        if estado:
            print('SI')
        else:
            print('NO')
