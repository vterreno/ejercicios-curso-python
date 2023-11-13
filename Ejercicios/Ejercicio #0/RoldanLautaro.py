filas=1
while filas> 0 and filas<50:
    filas = int(input())
    columnas = filas
    if filas> 0 and filas<50: 
        matriz = [[int() for ind0 in range(1*columnas)]for ind1 in range(1*filas)]
        for i in range(filas):
            pal =str(input())
            vec = pal.split(" ")
            for m in range(columnas):
                matriz[i][m] = int(vec[m])
                
        vector = [0]*2
        for i in range(filas):
            for m in range(columnas):
                if matriz[i][m] == 0:
                    if i>m:
                        vector[0] = vector[0] + 1
                    elif i<m:
                        vector[1] = vector[1] + 1   
        
        if vector[0]%3 == 0 or vector[0]%3 == 0:
            print("Es triangular")
        else:
            print("No es triangular")