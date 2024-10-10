horario = input().split(':')
hora = horario[0]
min = horario[1]

if hora[0] == '0':
    hora = int(hora[1])
else:
    hora = int(hora)
if min[0] == '0':
    min = int(min[1])
else:
    min = int(min)

print(((24 - hora) * 60) - min)
