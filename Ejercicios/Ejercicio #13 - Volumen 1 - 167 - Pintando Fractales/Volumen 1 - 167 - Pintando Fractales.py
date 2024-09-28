#INICIALIZACIÓN DE VARIABLES
contador = 1

#ENTRADAS
longitud = int(input())

#PROCESOS
perímetro = longitud * 4

while longitud != 1:
    perímetro = perímetro + ((4**contador)*(int(longitud/2))*4)
    contador = contador + 1
    longitud = int(longitud/2)

print(perímetro)