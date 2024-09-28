# Función para imprimir números primos en el rango de un número dado `n`
# Este algoritmo es la Temiz de Eratóstenes (o Sieve of Eratosthenes)
def cant_primos(num):
    contador = 0
    #Cada posición de este vector representará un número entero. El elemento contenido dentro de este
    #vector determinará si el número de esa posición es primo (1) o no (0). Al empezar se considera que todos son primos, por lo que 
    #inicializamos a vector_primos con un 1 en cada uno de sus elementos.
    vector_primos = [1] * (num + 1) 
 
    for i in range(2, int(num**(1/2)) + 1):
        if vector_primos[i] == 1:           # comprueba si i es primo (es decir si vale 1)
            j = 2
            while i * j <= num:
                vector_primos[i * j] = 0    # múltiplos de i no son primos
                j = j + 1
 
    for i in range(2, num + 1):
        if vector_primos[i] == 1:
            contador = contador + 1   #aumentamos en 1 la cantidad de primos

    return contador


#INICIALIZACIÓN DE VARIABLES
import math
salir = 0

#ENTRADAS Y PROCESOS
while salir == 0:

    #INICIALIZACIÓN DE VARIABLES
    invalido = 0
    bandera = 0
    n = 0
    m = 0

    #ENTRADAS
    cadena_input = str(input())

    #PROCESOS
    for i in range(len(cadena_input)):
        if bandera == 0 and cadena_input[i:i+1] == " ":
            pos_espacio = i
            bandera = 1

    if len(cadena_input[0 : pos_espacio]) > 6:
        invalido = 1
    if int(cadena_input[0 : pos_espacio]) < 100000 and int(cadena_input[0 : pos_espacio]) > 0:
        n = int(cadena_input[0 : pos_espacio])
    else:
        invalido = 1

    if len(cadena_input[pos_espacio+1 : len(cadena_input)]) == 1 and (int(cadena_input[pos_espacio+1 : len(cadena_input)]) >= 0 and int(cadena_input[pos_espacio+1 : len(cadena_input)]) <=5):
        m = int(cadena_input[pos_espacio+1 : len(cadena_input)])
    else:
        invalido = 1

    if n == 0 and m == 0:
        salir = 1
    elif invalido == 0: 
        error_gauss = abs(((cant_primos(n)) / n) - (1 / (math.log(n, math.e))))

        error_decimal = (1 / (10**m))       
        if error_gauss > error_decimal:
            estado = "Mayor"
        else:
            estado = "Menor"

        if error_decimal == error_gauss:
            estado = "Igual"

        print(estado)