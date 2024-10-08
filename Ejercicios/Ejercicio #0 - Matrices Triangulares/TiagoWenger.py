bandera=False
while bandera==False:
    filas= int(input())
    if filas!=0 and filas<=50:
        matriz=[[0]*filas]*filas
        for i in range(filas):
            for j in range(filas):
                matriz[i][j]=int(input())
        arriba=0
        abajo=0
        for i in range(filas):
            for j in range(filas):
                if (i-j)<0:
                    if matriz[i][j]!=0:
                        arriba+=1
                elif (i-j)>0:
                    if matriz[i][j]!=0:
                        abajo+=1
        if arriba==0 or abajo==0:
            print("SI")
        else:
            print("NO")
    else:
        bandera=True