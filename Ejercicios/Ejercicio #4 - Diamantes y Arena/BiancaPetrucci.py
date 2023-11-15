def contar_diam(diamantes):
    diamnte = []
    c2 = 0
    for i in range(len(diamantes)):
        if diamantes[i]== "<": 
            diamnte.append(diamantes[i])
        elif diamantes[i] == ">"and diamnte:
            diamnte.pop()
            c2 += 1
    return c2


# Ingresar la cantidad de pruebas
cantidad_pruebas = int(input(" "))
# Realizar las pruebas
for _ in range(cantidad_pruebas):
    diamantes = str(input(""))
    resultado = contar_diam(diamantes)
    print(resultado)