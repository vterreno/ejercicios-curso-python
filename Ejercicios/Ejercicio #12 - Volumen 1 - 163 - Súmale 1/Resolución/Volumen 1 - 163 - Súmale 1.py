#FUNCIÓN
def hex_siguiente(cadena):
    #INICIALIZACIÓN DE VARIABLES

    in_usuario = "0" + cadena           #Añadimos un 0 a la izquierda para los números cuyos dígitos son todos F
    in_usuario = in_usuario.upper()
    caracteres = "0123456789ABCDEF"

    capacidad_vector = 100
    vector_F = capacidad_vector * [0]
    contador = 0

    #PROCESOS
    if in_usuario[len(in_usuario)-1 : len(in_usuario)] != "F":

        #Si el último caracter NO es una F, lo aumentamos en 1.
        for i in range(len(caracteres)):
            if in_usuario[len(in_usuario)-1 : len(in_usuario)] == caracteres[i : i+1]:
                pos_encontrada = i

        #Concatenamos el nuevo caracter al resto de la cadena
        in_usuario = in_usuario[0: len(in_usuario)-1] + caracteres[pos_encontrada+1 : pos_encontrada+2]
        return in_usuario[1 : len(in_usuario)]
    else: 
        #Si el último caracter es una F significa que tenemos que hacerlo 0 y aumentar en 1 al caracter de su izquierda.
        #Disminuimos en 1 la cadena ingresada para que no se tome al último caracter, que será un 0
        in_usuario = hex_siguiente(in_usuario[0 : len(in_usuario)-1]) + "0"

        return in_usuario[1 : len(in_usuario)]

#INICIALIZACIÓN DE VARIABLES
salir = 0
vector_salidas = 100 * [""]
contador = 0

#ENTRADAS
while salir == 0:
    ceros = ""
    cadena = str(input())
    cadena = cadena.upper() 

    if cadena == "FIN":
        salir = 1
    else:
        #PROCESOS Y SALIDAS
        #Si la función devuelve todos 0, tenemos que añadir un 1 a la izquierda

        #Generamos una cadena de 0 del largo de la cadena originalmente ingresada
        for i in range(len(cadena)):
            ceros = "0" + ceros 

        if hex_siguiente(cadena) == ceros:
            vector_salidas[contador] = "1" + hex_siguiente(cadena)
        else:
            vector_salidas[contador] = hex_siguiente(cadena)

        contador = contador + 1

for i in range(100):
    if vector_salidas[i] != "":
        print(vector_salidas[i], end = "\n")