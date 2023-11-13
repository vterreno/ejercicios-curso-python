entrada = int(input())
matriz = [[int() for i in range(entrada)] for k in range(entrada)]
elemento_cero = int(0)
pal = []
es_triangular_sup = int(1)
es_triangular_inf = int(1)

for i in range(entrada):  # filas
    pal = str(input()).split(" ")
    for k in range(entrada):  # columnas
        matriz[i][k] = int(pal[k])
    
for i in range(len(matriz)):  # t sup
    for k in range(i + 1, len(matriz)):
        if matriz[i][k] != 0:
            es_triangular_sup = int(0)
            
for i in range(len(matriz)):  # t inf
    for k in range(0, i):
        if matriz[i][k] != 0:
            es_triangular_inf = int(0)

if es_triangular_inf and es_triangular_sup:
    print("Es triangular sup y inf")
else:
    if es_triangular_sup:
        print("Es triangular sup")
    if es_triangular_inf:
        print("Es triangular inf")
    if es_triangular_inf == 0 and es_triangular_sup == 0:
        print("No es triangular")

print(matriz)
        
# i, k
# 00 01 02
# 10 11 12
# 20 21 22
