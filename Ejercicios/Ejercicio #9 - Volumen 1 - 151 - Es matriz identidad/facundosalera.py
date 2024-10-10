while True:
    f=int(input())
    if f==0:
        break
    m=[[0]*f for i in range(f)]
    t=True
    for i in range(f):
        #contador columna
        c=0
        #indice donde comienza cada numero
        ui=0
        #ingresa la fila como cadena
        fila=str(input())+" "
        #recorremos la cadena
        for z in range(len(fila)):
            #guardamos el numero cada vez que encontramos un espacio
            if fila[z]==" ":
                m[i][c]=int(fila[ui:z])
                #actualizamos el ultimo indice y contador
                ui=z+1
                c+=1
    for i in range(f):
        for z in range(f):
            #comprobamos diagonal principal
            if i==z:
                if m[i][z]!=1:
                    t=False
            #comprobamos resto de la matriz
            else:
                if m[i][z]!=0:
                    t=False
    if t==True:
        print("SI")
    else:
        print("NO")
