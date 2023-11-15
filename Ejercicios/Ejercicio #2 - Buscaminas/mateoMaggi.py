tablero = str(input())
vector_tab = tablero.split()
ancho = int(vector_tab[0])
alto = int(vector_tab[1])
minas = int(0)
celdas_vacias = int(0)
matriz = [[str() for i in range(ancho)] for k in range(alto)]

if ancho != 0 and alto != 0:
    for i in range(alto):  # filas
        pal = str(input()).split()
        for k in range(ancho):  # columnas
            matriz[i][k] = pal[k]    
    i = int(0)
    k = int(0)
    for i in range(1,alto - 1): #0,1,2,3,4
        for k in range(1, ancho - 1):
                if matriz[i][k] == '-':
                    for a in range(i - 1, i + 2): 
                        for b in range(k - 1, k + 2):
                            if matriz[a][b] == "*":
                                minas += 1                               
                if minas >= 6:
                    celdas_vacias += 1
                minas = int(0)
print(celdas_vacias)
