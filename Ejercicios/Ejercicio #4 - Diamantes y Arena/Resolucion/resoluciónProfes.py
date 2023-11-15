"""
FUNCIONES
"""
def contarDiamantes(cadena):
    contador = 0
    bandera = True

    while bandera == True:
        bandera = False
        b1 = False

        for i in range(len(cadena)):
            if cadena[i] == "<":
                b1 = True
                indiceA = i 

            if cadena[i] == ">" and b1 == True:
                contador = contador + 1
                bandera = True
                b1 = False 
            
                #Signo cierre
                cadena = cadena[0 : i] + "0" + cadena[i+1 : len(cadena)]

                cadena = cadena[0 : indiceA] + "0" + cadena[indiceA+1 : len(cadena)]

                break

    return contador

"""
MAIN
"""

#INICIALIZACIÓN DE VARIABLES
casosUso = int(input())
vectorResultado = [0] * casosUso

#ENTRADAS Y PROCESOS
for i in range(casosUso):
    entrada = str(input())
    vectorResultado[i] = contarDiamantes(entrada)

#SALIDAS
for i in range(casosUso):
    print(vectorResultado[i])