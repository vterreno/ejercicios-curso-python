#entrada
Dia_inicial=input("Dia: ")
hora_inicial=input().split(":")
dia_final=input("Dia: ")
hora_final=input().split(":")
#convertimos los datos ingresador a segundos
seg_inicio = int(Dia_inicial) * 86400 + int(hora_inicial[0]) * 3600 + int(hora_inicial[1]) * 60 + int(hora_inicial[2]) 
seg_fin = int(dia_final) * 86400 + int(hora_final[0]) * 3600 + int(hora_final[1]) * 60 + int(hora_final[2])
#calculamos la diferencia de horas y minutos
dif_seg = seg_fin - seg_inicio
dias = dif_seg // 86400 
dif_seg = dif_seg % 86400 
horas = dif_seg // 3600
dif_seg = dif_seg % 3600 
min = dif_seg // 60 
seg = dif_seg % 60
#salida
print(dias,"dias(s)")
print(horas,"horas(s)")
print(min,"minutos(s)")
print(seg,"segundo(s)")

#se convierte los datos a segundos y luego convertimos a minutos ,horas y dias. para manejar con mayor facilidad y evitar errores en el conteo de los datos
