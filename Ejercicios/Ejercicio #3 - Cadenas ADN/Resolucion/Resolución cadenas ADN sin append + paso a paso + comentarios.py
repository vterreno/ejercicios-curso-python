#INICIALIZACIÓN DE VARIABLES
salida = 0
contador_filas_matriz = -1

#Generamos una matriz, cuyas columnas representan una cadena, y las filas indican las distintas iteraciones del algoritmo realizadas.
#Se sobredimensiona, originalmente se planteó con 20x20
filas = 5
columnas = 5
matriz = [[int(-1) for ind0 in range(columnas)] for ind1 in range(filas)]

while salida == 0:
    #INICIALIZACIÓN DE VARIABLES
    contador_iguales = 0

    #ENTRADAS
    #Le pedimos al usuario que ingrese la cantidad de cadenas a analizar
    cant_cadenas = int(input())

    if cant_cadenas != 0:
        #INICIALIZACIÓN DE VARIABLES - Contadores
        vector_cadenas_ADN = [0] * cant_cadenas
        contador_filas_matriz = contador_filas_matriz + 1 #Este contador cambia de fila la matriz para cada intento nuevo
    
        #ENTRADAS
        #Le pedimos al usuario que ingrese cada una de las cadenas dentro del vector
        for i in range(cant_cadenas):
            vector_cadenas_ADN[i] = str(input())

        #PROCESOS
        print("vector =",vector_cadenas_ADN)
        #Recorremos el vector posición por posición. 
        for i in range(cant_cadenas):
            contador_iguales = 0
            for j in range(cant_cadenas):
                #Comparamos la posición actual con el resto (no comparamos con ella misma)
                if j != i:

                    iguales = True
                    cadena1 = str(vector_cadenas_ADN[i])
                    cadena2 = str(vector_cadenas_ADN[j])

                    print("comparando",cadena1,"con",cadena2)

                    #Recorremos cadena1 y cadena2 elemento por elemento, y comparamos las posiciones homólogas. Si son distintas, 
                    #verificamos si alguna de las 2 es un guión, caso en el que damos a las posiciones como iguales. 
                    #Si en algún momento la comparación nos da distinta; no sumamos 1 a contador_iguales. Si da igual, sumamos 1

                    for k in range(len(cadena1)):
                        #Compararemos siempre y cuando todos los elementos analizados sean iguales
                        if iguales == True:
                            #Si son dos elementos iguales, no hace falta comparar más
                            if cadena1[k : k + 1] == cadena2 [k : k+1]:
                                print("caracter1 =",cadena1[k:k+1],"caracter2",cadena2[k:k+1])
                                iguales = True
                                print("iguales =",iguales)
                            #Si uno de los elementos es un guión, damos la comparación como válida
                            elif cadena1[k : k +1] == "-" or cadena2[k : k+1] == "-":
                                print("caracter1 =",cadena1[k:k+1],"caracter2",cadena2[k:k+1])
                                iguales = True
                                print("iguales =",iguales)
                            #Si no se cumple ninguna de las anteriores, damos la comparación como negativa
                            elif cadena1[k : k+1] != cadena2 [k : k+1]:
                                print("caracter1 =",cadena1[k:k+1],"caracter2",cadena2[k:k+1])
                                iguales = False
                                print("iguales =",iguales)
                            
                    #Si al terminar el ciclo for, iguales es True, significa que las cadenas analizadas son iguales; por lo que añadimos
                    #1 a contador_iguales

                    if iguales == True:
                        print("IGUALES")
                        contador_iguales = contador_iguales + 1
                    else:
                        print("DISTINTOS")
                        iguales == True
                    
                    print("\n")

            #Al terminar de ciclar por todas las posibilidades j de i; colocamos el valor de contador_iguales en la matriz
            print("contador",i,"=",contador_iguales)
            print("fila=",contador_filas_matriz)
            matriz[contador_filas_matriz][i] = contador_iguales
            print("-----------------------")
    else:
        salida = 1

#SALIDAS
#Imprimimos la matriz con todos los resultados
print("contador filas =",contador_filas_matriz)
for i in range(filas):
    for j in range(columnas):
        #Imprimimos todos los elementos que no sean -1
        if matriz[i][j] != (-1):
            print(matriz[i][j],end = " ") 
    if i <= contador_filas_matriz:    
        print("",end = "\n")

print(matriz)