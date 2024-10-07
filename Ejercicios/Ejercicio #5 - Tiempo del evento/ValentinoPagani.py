inicio = input()
inicio_horario = input().split(':')
fin = input()
fin_horario = input().split(':')
dia_i = int(inicio[4:])
hora_i = inicio_horario[0]
min_i = inicio_horario[1]
seg_i = inicio_horario[2]
dia_f = int(fin[4:])
hora_f = fin_horario[0]
min_f = fin_horario[1]
seg_f = fin_horario[2]
if hora_i[0] == '0':
    hora_i = hora_i[1]
if hora_f[0] == '0':
    hora_f = hora_f[1]
if min_i[0] == '0':
    min_i = min_i[1]
if min_f[0] == '0':
    min_f = min_f[1]
if seg_i[0] == '0':
    seg_i = seg_i[1]
if min_f[0] == '0':
    seg_f = seg_f[1]
hora_i = int(hora_i)
min_i = int(min_i)
seg_i = int(seg_i)
hora_f = int(hora_f)
min_f = int(min_f)
seg_f = int(seg_f)

dias_t = dia_f - dia_i
horas_t = hora_f - hora_i
min_t = min_f - min_i
seg_t = seg_f - seg_i

if hora_i > hora_f:
    horas_t = 24 + horas_t
    dias_t -= 1
if min_i > min_f:
    min_t = 60 + min_t
    horas_t -= 1
if seg_i > seg_f:
    seg_t = 60 + seg_t
    min_t -= 1

print(dias_t, 'dia (s)')
print(horas_t, 'hora (s)')
print(min_t, 'minuto (s)')
print(seg_t, 'segundo (s)')
