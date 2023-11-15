
vec = [str]

for i in range(2):
    dias = str(input())
    horas = str(input())
    vec.append(dias)
    vec.append(horas)


f1 = vec[1].split(" ")
h1 = vec[2].split(":")


f2 = vec[3].split(" ")
h2 = vec[4].split(":")

dia1 = int(f1[1])
horas = int(h1[0])
minutos = int(h1[1])
segundos = int(h1[2])

dia2 = int(f2[1])
horas2 = int(h2[0])
minutos2 = int(h2[1])
segundos2 = int(h2[2])

diasT = dia2 - dia1

segundosT = segundos2 - segundos

if segundosT < 0:
    segundosT = 60 + segundosT
    minutos2 = minutos2 - 1

minutosT = minutos2 - minutos

if minutosT < 0:
    minutosT = 60 + minutosT
    horas2 = horas2 - 1

horasT = horas2 - horas

if horasT < 0:
    horasT = 24 + horasT
    diasT = diasT - 1

print(f"{diasT} dia(s)")
print(f"{horasT} hora(s)")
print(f"{minutosT} minuto(s)")
print(f"{segundosT} segundo(s)")