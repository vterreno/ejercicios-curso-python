def diagonalMatriz (matriz, longitud):
    # diagonalSuperior
    contador = 0
    for i in range(longitud):
        for k in range(longitud):
            if i != k and k > i:
                if matriz[i][k] == "0":
                    contador += 1
    
    if contador % 3 == 0 and contador != 0:
        return "SI"
    
    # diagonalInferior
    contador = 0
    for i in range(longitud):
        for k in range(longitud):
            if i != k and k < i:
                if matriz[i][k] == "0":
                    contador += 1
    
    if contador % 3 == 0 and contador != 0:
        return "SI"
    else:
        return "NO"

def separarCadena (cadena, entrada):
    acumulador = ""
    a = 0
    vector = [""] * entrada
    for i in range(len(cadena)):
        if cadena[i] != " ":
            acumulador += cadena[i]
        
        if cadena[i] == " " or i == len(cadena)-1:
            vector[a] = acumulador
            a += 1
            acumulador = ""
    
    return vector

entrada = 1
a = 0
resultados = [0] * 100
while entrada != 0:
    entrada = int(input())
    if entrada != 0:
        matriz = [[int() for ind0 in range(entrada)] for ind1 in range(entrada)]
        
        for i in range(entrada):
            linea = str(input())
            linea = separarCadena(linea, entrada)
            for k in range(entrada):
               matriz[i][k] = linea[k] 

        resultados[a] = diagonalMatriz(matriz, entrada)
        a += 1

for i in range(len(resultados)):
    if resultados[i] != 0:
        print(resultados[i])