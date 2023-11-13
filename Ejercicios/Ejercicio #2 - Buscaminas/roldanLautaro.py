filas = 1
columnas = 1

while columnas!=0 and filas!=0:
    FC = str(input())
    AF = FC.split(" ")
    filas = int(AF[1])
    columnas = int(AF[0])
    matriz = [[str() for ind0 in range(1*columnas)]for ind1 in range(1*filas)]

    if columnas!=0 and filas!=0 :

        for i in range(filas):
            carga = str(input())
            for h in range(len(carga)):
                matriz[i][h]=carga[h]

        print(" ")

        for i in range(filas):
            for h in range(columnas):
                print(matriz[i][h],end="")
            print(" ")

        cont2 = 0
        cont = 0

        for i in range(filas):
            for h in range(columnas):
                if h != 0 and h != columnas-1 and i != 0 and i != filas-1:
                    if matriz[i][h] == "-": 
                        for j in range(3):
                            for z in range(3):
                                if matriz[((i-1)+j)][((h-1)+z)]== "*":
                                    cont = cont+1

                    if cont >= 6:
                        cont2 = cont2+1
                        cont = 0
                    else:
                        cont = 0

        print(cont2)

                    
                    

