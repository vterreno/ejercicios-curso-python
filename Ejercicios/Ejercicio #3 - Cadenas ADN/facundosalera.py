while True:
    nc=int(input()) #num de cadenas
    if nc==0:
        break
    for j in range(nc): #guardar las cadenas en un vector
        cadena=str(input())
        if j==0:
            v=[""]*nc
        v[j]=cadena
    for i in range(nc): #recorrer cada cadena
        c=nc-1
        for z in range(nc):  #compararla con las otras cadenas y comprobar si son iguales
            if i!=z:
                for j in range(len(cadena)):
                    if v[i][j]!=v[z][j] and v[i][j]!="-" and v[z][j]!="-":
                        c-=1
                        break
        print(c, end=" ")
    print("\n")
