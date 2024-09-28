"""
REFINAMIENTOS: Pág 24 final y 25 cuaderno AyED primer año

Función 1 - orden(cadena):
De una cadena, toma al primer caracter como el primero, el segundo como el último, el tercero como el segundo, el cuarto
como el penúltimo, el quinto como el tercero, etc.
Aauirnedleiua nBo → AurelianoB uednia

Función 2 - img_especular(cadena):
Invierte la cadena convertida entre inicio y vocal, entre vocales y entre vocal y final, manteniendo la posición de las vocales.
[]B[o]J ,dn[a]m[e]B s[o]dn[] → []B[o]nd, J[a]m[e]s B[o]nd[]
"""

def orden(cadena):
    cadena_referencia = cadena
    salida = ""
    auxiliar = ""
    for i in range(len(cadena_referencia)):
        if i % 2 == 0:
            salida = salida + cadena_referencia[i:i+1]

    for i in range(len(cadena_referencia)):
        if ((i+1) % 2) == 0:
            auxiliar = auxiliar + cadena_referencia[i:i+1]

    salida = salida + auxiliar[::-1]
    
    return salida

def img_especular(cadena):
    cadena_referencia = cadena
    cadena_referencia_lower = cadena.lower()
    salida = ""
    vocales = "aeiou"

    contador = 1
    cant_vocales = 100
    vector_vocales = cant_vocales * [-1]

    #Ubicamos la posición de las vocales dentro de vector_vocales
    for i in range(len(cadena_referencia)):
        for j in range(len(vocales)):
            if cadena_referencia_lower[i:i+1] == vocales[j:j+1]:
                vector_vocales[contador] = i
                contador = contador + 1
    
    #Añadimos en la última posición el largo de la cadena. Esto junto a la primera posición que es 0 nos hará más fácil trabajar
    vector_vocales[contador] = len(cadena_referencia)

    #Entre los intervalos definidos dentro de vector_vocales, invertimos la cadena
    for i in range(cant_vocales):
        auxiliar = ""

        if i == 0:
            auxiliar = cadena_referencia[0:vector_vocales[1]]
            auxiliar = auxiliar[::-1]
            salida = salida + auxiliar

        if (i != 0) and (vector_vocales[i] != -1):
            auxiliar = cadena_referencia[vector_vocales[i]+1:vector_vocales[i+1]]
            auxiliar = auxiliar[::-1]
            salida = salida + cadena_referencia[vector_vocales[i]:vector_vocales[i]+1] + auxiliar

    return salida 


#ENTRADAS
cadena_input = str(input())

#PROCESOS
cadena_procesada = cadena_input
cadena_procesada = orden(cadena_procesada)
cadena_procesada = img_especular(cadena_procesada)

#SALIDAS
print(cadena_input, "=>",cadena_procesada)