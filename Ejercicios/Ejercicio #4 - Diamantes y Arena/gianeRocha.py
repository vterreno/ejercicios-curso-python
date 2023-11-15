def comprobar(vector):
    cantidad=len(vector)
    contador1=0
    contador2=0
    cont3=0   #<<..>>
    vector2=[0]*cantidad
    
    for i in range (0,cantidad,1):
        cadena=vector[i]
        for j in range(0,(len(cadena)),1):
            if cadena[j]=="<":
                contador1=contador1+1
            elif cadena[j] ==">":
                contador2=contador2+1
        if contador1 == contador2:
            cont3=+1
        elif contador1 > contador2:
            cont3 = contador2
        if contador2 > contador1:
            cont3 = contador1
        contador1=0
        contador2=0
        vector2[i]=cont3
        cont3= 0
    return vector2


prueba=int(input())
contador1=0
contador2=0
cont3=0
vector=[""]*prueba
for i in range(0,prueba,1):
    linea=(str(input("ingresar linea:")))
    vector[i]=linea


resultado=comprobar(vector)


for i in range (0,(len(resultado)),1):
    print(resultado[i])