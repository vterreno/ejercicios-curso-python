entrada1=1
entrada=1
c=0
elemento=0
while entrada !=0 and entrada1 != 0:
    entrada = int(input("columna:")) #columnas
    entrada1 = int(input("filas:")) #filas
    if entrada and entrada1 != 0:
        matriz = [[int() for ind0 in range(entrada)] for ind1 in range(entrada1)]
        
        for i in range(entrada1):
            linea = str(input())
            for k in range(entrada):
               matriz[i][k] = linea[k] 
    for i in range (1,entrada1-1,1):#fila
        for k in range(1,entrada-1,1):#columna
            if matriz[i][k]=="-":
                if matriz[i-1] [k-1]=="*":
                    c+=1
                if matriz[i-1][k]=="*":
                    c+=1
                if matriz[i-1][k+1]=="*":
                    c+=1
                if matriz[i][k+1]=="*":
                    c+=1
                if matriz[i+1][k+1]=="*":
                    c+=1
                if matriz[i+1][k]=="*":
                    c+=1
                if matriz[i+1][k-1]=="*":
                    c+=1
                if matriz [i][k-1]=="*":
                    c+=1
                if c>=6:
                    elemento+=1
                c=0
print("hay", elemento,"elementos con por lo menos 6 minas alrededor")