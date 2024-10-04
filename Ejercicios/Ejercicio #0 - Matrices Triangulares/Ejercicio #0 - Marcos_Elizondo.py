numero=1
while numero != 0:
    triangular_superior=1
    triangular_inferior=1
    numero=int(input())
    Matriz=[[int(0) for fila in range(numero)]for columna in range (numero)]
    for i in range (numero):
        j2=0
        num=input("")
        for j in range((numero)+(numero-1)):
            if num[j:j+1] != ' ':
                Matriz[i][j2]=int(num[j:j+1])
                j2+=1
    
    #for i in range (numero):
    #    for j in range (numero):
    #        Matriz[i][j]=int(input())
    for fila in range (numero):
        for columna in range (numero):
            if fila != columna:
                if fila<columna and Matriz[fila][columna]!=0:
                    triangular_superior=0
                elif fila>columna and Matriz[fila][columna]!=0:
                    triangular_inferior=0
    if triangular_inferior == 1 or triangular_superior == 1:
        print("SI")
    else:
        print("NO")