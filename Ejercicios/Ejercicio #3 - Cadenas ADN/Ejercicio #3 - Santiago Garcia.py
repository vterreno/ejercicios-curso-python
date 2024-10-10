def compdecadenas(numero,vector):
    vector2=[int]*numero
    for i in range(numero):
        cont=0
        subcadena=vector[i]
        for j in range(len(subcadena)):
            if j!=i:
                if j<numero:
                    subcadena2=vector[j]
                if subcadena[j]!=subcadena2[j] and subcadena2[j]!="-" and subcadena[j]!="-":
                    bandera=1
                if bandera==0:
                    cont+=1
            bandera=0
        vector2[i]=cont
    return vector2    
numerodelineas=int(input())
cont=-1
vector3=[str]*(cont+10)
while numerodelineas!=0:
    cont+=1
    vector=[str]*numerodelineas
    vector3=vector3*(cont+10)
    for i in range(numerodelineas):
        vector[i]=str(input())
    vector3[cont]=str(compdecadenas(numerodelineas,vector))
    numerodelineas=int(input())
for i in range(cont+1):
    print(vector3[i])
