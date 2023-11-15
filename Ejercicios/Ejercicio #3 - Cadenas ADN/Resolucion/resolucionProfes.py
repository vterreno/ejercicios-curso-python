""" 
ENTRADA

La entrada estara formada por distintos casos de prueba. Cada uno comienza con una linea que
indica el numero de cadenas de ADN que se daran (hasta 40.000). A continuacion vendra una linea con
cada una de las cadenas, todas con la misma longitud (como mucho 50 caracteres).
Cada cadena de ADN tendra los caracteres A, C, G y T indicando el nucleotido colocado en esa
posicion o un guion (-) indicando un hueco (nucleotido desconocido) en la cadena. De haber huecos o
guiones estos estaran colocados principalmente en los laterales de la cadena; en la parte central nunca
habra mas de 2.
Dos cadenas pueden pertenecer al mismo individuo si en las posiciones en las que ambas tienen
nucleotido conocido, este coincide. 

SALIDA

Por cada caso de prueba se escribira una linea con tantos numeros como cadenas de ADN se han
dado. El numero en la posicion i indicara cuantas cadenas iguales a la cadena colocada en la posicion i
hay (sin contar a ella misma), teniendo en cuenta que los guiones se consideran igual a cualquier otro
nucleotido (o a otro guion)
"""

casos = 1
salida = []
while casos > 0:
    casos = int(input())
    if casos != 0:
        vectorCadenas = [""] * casos

        #Recepción de cadenas
        for i in range(casos):
            vectorCadenas[i] = input()
        
        #Averigüo cantidad de símbolos de las cadenas
        cantidadSimbolos = len(vectorCadenas[0])

        #Creo la matriz para almacenar los caracteres
        matriz = [[' ' for _ in range(cantidadSimbolos)] for _ in range(casos)]

        #Cargo la matriz con los caracteres
        for i in range(casos):
            cadena = vectorCadenas[i]
            for j in range(cantidadSimbolos):
                matriz[i][j] = cadena[j]
        
        #Análisis
        vectorResultados = [0] * casos
        vectorVerificaciones = [False] * casos #Si es False, es porque en esa fila/cadena, no se encontró diferencias todavía
        resultado = casos - 1
        for k in range(casos): # Elegir la fila donde pivotamos, y a partir de esa comparamos
            for i in range(cantidadSimbolos):
                simbolo = matriz[k][i]
                #Si es un -, es comodín y anda con cualquiera. Si es diferente a -, hay que analizar.
                if simbolo != "-":
                    for j in range(casos):
                        #Si k y j son iguales significa que compararía con la misma fila en la que estoy parado
                        if k != j:
                            simbolo2 = matriz[j][i]
                            if simbolo != simbolo2 and vectorVerificaciones[j] == False and simbolo2 != "-":
                                resultado -= 1
                                vectorVerificaciones[j] = True
            vectorResultados[k] = resultado
            resultado = casos - 1
            vectorVerificaciones = [False] * casos

        salida.append(vectorResultados)

for i in range(len(salida)):
    for j in range(len(salida[i])):
        print(salida[i][j], end = " ")
    print("")