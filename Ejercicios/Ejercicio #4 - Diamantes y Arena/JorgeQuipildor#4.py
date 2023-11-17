def diamantee(cadena):
    contador = 0
    almacen = []
    
    # Recorremos la cadena para encontrar los diamantes la condicion que abre y tiene que cerrar "<>",
    #el resto de "." no se tiene en cuenta
    for caracter in cadena:
        if caracter == "<":
            almacen.append(caracter)
        elif caracter == ">":
            if almacen:
                almacen = almacen[:-1]
                contador += 1
    
    return contador

# Entrada
entrada = int(input())
for i in range(entrada):
    cadena = input()
    diamantes = diamantee(cadena)
    print(diamantes)
