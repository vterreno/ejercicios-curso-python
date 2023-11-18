entradaDia1 = input()
entradaHorario1 = input()
entradaDia2 = input()
entradaHorario2 = input()

#Extracción de días
def extraccionDias(cadena):
    for i in range(len(cadena)):
        if cadena[i] == " ":
            return int(cadena[i+1 : ])

#Extracción de horas
def extraccionHoras(cadena):
    return int(cadena[0:2])

#Extracción de minutos
def extraccionMinutos(cadena):
    return int(cadena[5:7])

#Extracción segundos
def extraccionSegundos(cadena):
    return int(cadena[10:])

dia1 = extraccionDias(entradaDia1)
dia2 = extraccionDias(entradaDia2)
hora1 = extraccionHoras(entradaHorario1)
hora2 = extraccionHoras(entradaHorario2)
minutos1 = extraccionMinutos(entradaHorario1)
minutos2 = extraccionMinutos(entradaHorario2)
segundos1 = extraccionSegundos(entradaHorario1)
segundos2 = extraccionSegundos(entradaHorario2)

total1 = dia1 * 86400 + hora1 * 3600 + minutos1 * 60 + segundos1
total2 = dia2 * 86400 + hora2 * 3600 + minutos2 * 60 + segundos2

diferencia = total2 - total1

dias = diferencia // 86400
diferencia = diferencia - (dias * 86400)

horas = diferencia // 3600
diferencia = diferencia - (horas * 3600)

minutos = diferencia // 60
diferencia = diferencia - (minutos * 60)

segundos = diferencia

print(str(dias) + " dia(s)")
print(str(horas) + " hora(s)")
print(str(minutos) + " minuto(s)")
print(str(segundos) + " segundo(s)")