i = j = filxcol = f = f2 = fr = numerito = 0
mat = [[0 for _ in range(50)] for _ in range(50)]
resultados = [0.0 for _ in range(100)]

while True:
   
    filxcol = int(input("Dimension: ")) 
    if 0 < filxcol <= 50:
        f = f2 = 0
        for i in range(filxcol):
            for j in range(filxcol):
                numerito = int(input())
                if not (-1000 <= numerito <= 1000):
                    f = f2 = 1
                else:
                    mat[i][j] = numerito
        if not f:
            for i in range(filxcol):
                for j in range(filxcol):
                    if (i == j and mat[i][j] != 1) or (i != j and mat[i][j] != 0):
                        f2 = 1
        resultados[fr] = 1 if not f2 else 0
        fr += 1
    else:
        if filxcol != 0:
            resultados[fr] = -1
            fr += 1
    if filxcol == 0:
        break

for i in range(fr):
    if resultados[i] == 1:
        print("SI")
    elif resultados[i] == 0:
        print("NO")
    elif resultados[i] == -1:
        print("INVALIDO") #por si ingresa un valor para la dimension fuera del rango (0 a 50)
