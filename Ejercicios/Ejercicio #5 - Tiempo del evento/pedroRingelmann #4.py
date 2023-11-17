#Inicio
DiaI=int(input('Dia '))
horaI=str(input())
x=horaI.split(':')

#Final
DiaF=int(input('Dia '))
horaF=str(input())
z=horaF.split(':')

#Dia total
totalD=DiaF-DiaI-1
#Tiempo
horas=24-int(x[0])+int(z[0])
minutos=int(z[1])-int(x[1])
if minutos==0:
    minutos=1
segundos=int(z[2])-int(x[2])

print(f'{totalD} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')