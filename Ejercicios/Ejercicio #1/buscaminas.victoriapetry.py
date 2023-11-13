#entrada de datos linea por linea
ingreso=str(input())
#separo por espacios para saber las columnas y filas
ingreso=ingreso.split(" ")
matriz=[[str()for ind0 in range(1*(int(ingreso[0])))]for ind1 in range (1*(int(ingreso[1])))]
for i in range(int(ingreso[1])):
    v=str(input())
    for j in range(len(v)):
        matriz[i][j]=v[j]
#vector ingreso tiene las dimensiones de la matriz
filas=int(ingreso[1])
columnas=int(ingreso[0])
cont=0
c=0
#busco el -, y con un contador se buscan cuantos * hay
for i in range(int(ingreso[1])):
    for j in range(int(ingreso[0])):
        if i!=0 and j!=0 and i!=(filas-1) and j!=(columnas-1):
            if matriz[i][j]=="-":
                for a in range(3):
                    for b in range(3):
                        if matriz[(i-1)+a][(j-1)+b]=="*":
                            cont+=1
                if cont==6:
                    c+=1
                    cont=0
                else:     
                    cont=0
print(c)
#salida sera cuando el contador sea igual a seis, es decir que se encontraron 6 (*).