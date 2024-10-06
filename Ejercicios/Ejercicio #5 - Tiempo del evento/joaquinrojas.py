def hora_segundo(n):
    hora = int(n[0:2]) * 3600
    minuto = int(n[3:5]) * 60
    segundo = int(n[6:8])
    total_en_segundo = hora + minuto + segundo
    return total_en_segundo
    
def segundo_hora(n):
    w = n // 86400
    r = n  % 86400
    x = r // 3600
    r = r % 3600
    y = r // 60
    z = r % 60
    return w, x, y, z

inicioDia = int(input("Dia del inicio: "))
inicioHora = input("Hora inicial: ")
finalDia = int(input("Dia del final: "))
finalHora = input("hora final: ")
mes = 86400
total_segundo_inicio = (inicioDia - 1) * mes + hora_segundo(inicioHora)
total_segundo_final = (finalDia - 1) * mes + hora_segundo(finalHora)

W, X, Y, Z = segundo_hora(total_segundo_final - total_segundo_inicio)

print(W,'dia(s)')
print(X,'hora(s)')
print(Y,'minuto(s)')
print(Z,'segundo(s)')