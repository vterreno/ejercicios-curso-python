def ubi_espacio(dimensiones):
    espacio = -1
    for i in range(len(dimensiones)):
        if dimensiones[i:i+1] == " ":
            espacio = i

    return espacio

def verif_fila(cadena):
    valido = True
    for i in range(len(cadena)):
        if cadena[i:i+1] != "*" and cadena[i:i+1] != "-":
            valido = False

    return valido

def verif_dimension(dimensiones,espacio):
    valido = True
    for i in range(espacio):
        if dimensiones[i:i+1] != "0" and dimensiones[i:i+1] != "1" and dimensiones[i:i+1] != "2" and dimensiones[i:i+1] != "3" and dimensiones[i:i+1] != "4" and dimensiones[i:i+1] != "5" and dimensiones[i:i+1] != "6" and dimensiones[i:i+1] != "7" and dimensiones[i:i+1] != "8" and dimensiones[i:i+1] != "9":
            valido = False

    if valido == True:
        for i in range(espacio+1,len(dimensiones)):
            if dimensiones[i:i+1] != "0" and dimensiones[i:i+1] != "1" and dimensiones[i:i+1] != "2" and dimensiones[i:i+1] != "3" and dimensiones[i:i+1] != "4" and dimensiones[i:i+1] != "5" and dimensiones[i:i+1] != "6" and dimensiones[i:i+1] != "7" and dimensiones[i:i+1] != "8" and dimensiones[i:i+1] != "9":
                valido = False

    return valido


#INICIALIZACIÓN DE VARIABLES
invalido = 0
contador = 0
vacias_con6minas = 0

#E N T R A D A S
dimensiones = str(input("Ingrese las dimensiones: ")) #Se ingresa ancho x alto

while ubi_espacio(dimensiones) == -1:
    dimensiones = str(input("ERROR - Reingrese las dimensiones: "))

    if ubi_espacio(dimensiones) != -1:
        while (verif_dimension(dimensiones,ubi_espacio(dimensiones)) == False):
            dimensiones = str(input("ERROR - Reingrese las dimensiones: "))

espacio = ubi_espacio(dimensiones)
ancho = int(dimensiones[0:espacio])
alto = int(dimensiones[espacio+1 : len(dimensiones)])

#Definimos una matriz del tamaño ancho x alto
matriz = [[str("0") for ind0 in range(ancho)] for ind1 in range(alto)]

for i in range(alto):
    #Permitimos que el usuario ingrese una cadena de longitud ancho, que colocaremos en la primer fila de matriz
    cadena = str(input("Ingrese la fila: "))

    while (verif_fila(cadena) == False) or (len(cadena) != ancho):
        cadena = str(input("ERROR - Ingrese la fila nuevamente: "))

    #Pasamos la cadena a la posición respectiva en la matriz
    for j in range(ancho):
        matriz[i][j] = cadena[j:j+1]

#P R O C E S O S

#Encontramos una celda vacía que no esté en los bordes de la matriz, ya que como max estas pueden estar rodeadas por 5 *
for i in range(1,alto-1):
    for j in range(1,ancho-1):
        if matriz[i][j] == "-":
            #Una vez encontramos una posición con un -, recorremos un espacio 3x3 en su alrededor, y contamos cada vez que aparezca un *
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if matriz[k][l] == "*":
                        contador = contador + 1

            if contador >= 6:
                vacias_con6minas = vacias_con6minas + 1
            contador = 0

#S A L I D A S
print("------------------------------")
print("Celdas vacías rodeadas por 6 o más minas:",vacias_con6minas)
print("------------------------------")
print("MATRIZ INGRESADA")
print("------------------------------")
for i in range(alto):
    for j in range(ancho):
        print(matriz[i][j],end = " ")
    print("",end = "\n")
print("------------------------------")

