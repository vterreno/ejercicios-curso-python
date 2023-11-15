ingreso=str(input())
if int(ingreso)>0 and int(ingreso)<50:   
    matriz=[[str()for ind0 in range(1*(int(ingreso)))]for ind1 in range (1*(int(ingreso)))]
    for i in range(int(ingreso)):
        v=str(input())
        for j in range(len(v)):
            matriz[i][j]=v[j]

cs=ci=0
#condicion
for i in range(int(ingreso)):
    for j in range(int(ingreso)):
        if i>j and i!=j:
            if matriz[i][j]==0:
                ci+=1
        else:
            if matriz[i][j]==0:
                cs+=1
if ci%3==0:
    print("es triangular")
elif ci%3!=0:
    print("no es triangular")
elif cs%3==0:
    print("es triangular")
elif cs%3!=0:
    print("no es triangular")


#imprimir matriz
""" for i in range(int(ingreso)):
    for j in range(int(ingreso)):
        print(matriz[i][j],end=" ")    
    print(" ") 
 """
