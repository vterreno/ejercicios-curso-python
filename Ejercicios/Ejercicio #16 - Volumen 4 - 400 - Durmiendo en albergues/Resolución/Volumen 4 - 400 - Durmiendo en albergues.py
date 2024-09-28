print("Ingrese la disposición de camas (. = libre; X = ocupado)")
cadena = str(input("→ "))

if len(cadena) < 500000:
    #Revisamos que la cadena ingresada esté formada solamente por . y X
    cadena_lower = cadena.lower()
    input_erroneo = 0

    for i in range(len(cadena_lower)):
        if cadena_lower[i : i+1] != "." and cadena_lower[i : i+1] != "x":
            print("analizando",cadena_lower[i:i+1])
            input_erroneo = 1

    if input_erroneo == 0:

        #Ubicamos la posición de cada cama ocupada X
        camas_ocupadas = 20 * [-1]
        cant_ocupadas = 0
        for i in range(len(cadena_lower)):
            if cadena_lower[i : i+1] == "x":
                camas_ocupadas[cant_ocupadas] = i
                cant_ocupadas = cant_ocupadas + 1
        
        print(camas_ocupadas,cant_ocupadas)
        #Analizamos los espacios ENTRE las camas ocupadas
        distancia_max = 0
        for i in range(cant_ocupadas-1):
            if cadena_lower[i+1] != -1:
                distancia_neta = len(cadena_lower[camas_ocupadas[i]+1 : camas_ocupadas[i+1]])
        
            if distancia_neta % 2 == 0:
                distancia_auxiliar = (distancia_neta / 2) - 1

            if distancia_neta == 1:
                distancia_auxiliar = 0
            
            if (distancia_neta != 1) and ((distancia_neta % 2) != 0):
                distancia_auxiliar = int(distancia_neta/2)

            #Si encontramos una distancia mayor a la actual, la reemplazamos
            if distancia_auxiliar > distancia_max:
                distancia_max = distancia_auxiliar

        
        #Analizamos los espacios de los EXTREMOS: Desde el inicio hasta la primer cama ocupada y desde la última cama hasta el final
        
        #Extremo izquierdo
        distancia_neta = len(cadena_lower[0 : camas_ocupadas[0]])
        distancia_auxiliar = distancia_neta - 1
        if distancia_auxiliar > distancia_max:
            distancia_max = distancia_auxiliar

        #Extremo derecho
        distancia_neta = len(cadena_lower[camas_ocupadas[cant_ocupadas-1]+1 : len(cadena_lower)])
        distancia_auxiliar = distancia_neta - 1
        if distancia_auxiliar > distancia_max:
            distancia_max = distancia_auxiliar

print(int(distancia_max))