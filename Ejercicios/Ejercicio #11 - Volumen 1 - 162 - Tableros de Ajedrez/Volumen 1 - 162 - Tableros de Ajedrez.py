#ENTRADAS

#El usuario ingresará en una sola línea el tamaño de los cuadrados y qué carácter estáran formados los recuadros negros
cadena = str(input())

#PROCESOS
#Extraemos el tamaño de los cuadrados y el caracter
for i in range(len(cadena)):
    if cadena[i : i+1] == " ":
        espacio = i

tamaño = int(cadena[0 : espacio])
caracter_negro = cadena[espacio+1 : len(cadena)]

#Generamos cadenas del tamaño designado
cadena_blanco = ""
cadena_negro = ""

#Para los cuadrados blancos usamos el espacio
for i in range(tamaño):
    cadena_blanco = cadena_blanco + " "

#Para los cuadrados negros usamos el indicado por el usuario
for i in range(tamaño):
    cadena_negro = cadena_negro + caracter_negro


#SALIDAS

#Encabezado
encabezado = ""
for i in range(tamaño * 8):
    encabezado = encabezado + "-"
encabezado = "|" + encabezado + "|"


print(encabezado)
for i in range(8):
    for j in range(tamaño):
        if i % 2 == 0:
            for k in range(8):
                if k % 2 == 0:
                    if k == 0:
                        print("|", end = "")
                    
                    print(cadena_blanco, end = "")

                    if k == 7:
                        print("|", end = "")
                else:
                    if k == 0:
                        print("|", end = "")
        
                    print(cadena_negro, end = "")

                    if k == 7:
                        print("|", end = "")
        else:
            for k in range(8):
                if k % 2 == 0:
                    if k == 0:
                        print("|", end = "")

                    print(cadena_negro, end = "")

                    if k == 7:
                        print("|", end = "")
                else:
                    if k == 0:
                        print("|", end = "")

                    print(cadena_blanco, end = "")

                    if k == 7:
                        print("|", end = "")
        print("")
print(encabezado)