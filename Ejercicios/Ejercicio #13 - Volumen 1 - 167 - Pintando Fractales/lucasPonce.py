N = int(input())
contador = 1
lados = N * 4

while N != 1:
    N = N // 2
    lados += (N * 4 * (4**contador))
    contador += 1

print(lados)