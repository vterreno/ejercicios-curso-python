#FUNCIÓN
def mat_siguiente(cadena):
    cadena = cadena.upper()
    digitos = cadena[0 : 4]
    letras = cadena[5 : 8]
    caracteres = "BCDFGHJKLMNPQRSTVWXYZ"

    if digitos != "9999":
        digitos = str(int(digitos) + 1)
        salida = digitos + " " + letras

    elif digitos == "9999":
        digitos = "0000"

        #Aumentamos en 1 a letras
        if letras[2:3] != "Z":
            for i in range(len(caracteres)):
                if caracteres[i:i+1] == letras[2:3]:
                    letra_actual = i

            salida = digitos + " " + letras[0:2] + caracteres[(letra_actual+1): (letra_actual+2)]
        
        #Si sólo el último caracter es Z
        elif letras[1:2] != "Z" and letras[2:3] == "Z":
            letras = letras[0 : 2] + "B"
            for i in range(len(caracteres)):
                if caracteres[i:i+1] == letras[1:2]:
                    letra_actual = i

            salida = digitos + " " + letras[0:1] + caracteres[(letra_actual+1): (letra_actual+2)] + letras[2:3]

        #Si los últimos dos carácteres son Z
        elif letras[1:2] == "Z" and letras[2:3] == "Z":
            letras = letras[0:1] + "B" + "B"
            for i in range(len(caracteres)):
                if caracteres[i:i+1] == letras[0:1]:
                    letra_actual = i

            salida = digitos + " " + caracteres[(letra_actual+1): (letra_actual+2)] + letras[1:3]

    return salida


#INICIALIZACIÓN DE VARIABLES
salir = 0
vector_salidas = 100 * [""]
contador = 0

#ENTRADAS
while salir == 0:
    cadena = str(input())
    cadena = cadena.upper()

    if cadena == "9999 ZZZ":
        salir = 1
    else:
        #PROCESOS Y SALIDAS
        vector_salidas[contador] = mat_siguiente(cadena)
        contador = contador + 1

for i in range(100):
    if vector_salidas[i] != "":
        print(vector_salidas[i], end = "\n")