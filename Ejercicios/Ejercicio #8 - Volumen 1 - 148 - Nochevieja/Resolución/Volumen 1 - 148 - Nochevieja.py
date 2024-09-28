salir = 0
contador = 0
vector_salida = [0] * 100

while salir == 0:
    #INICIALIZACIÓN DE VARIABLES
    minutos = 0
    horas = 0
    
    #ENTRADAS
    cadena = str(input())

    if cadena == "00:00":
        salir = 1
    else:
        if cadena[0:2] != "00":
            minutos = int(cadena[3 : 5])
            horas = 24 - int(cadena[0 : 2])
            minutos = horas * 60 - minutos
        else:
            minutos = int(cadena[3:5])
            horas = 24 + int(cadena[0:2])
            minutos = horas*60 - minutos

    vector_salida[contador] = minutos
    contador = contador + 1

for i in range(100):
    if vector_salida[i] != 0:
        print(vector_salida[i], end = "\n")