def resultado():
    disp = input()
    if disp == "":
        return "cortar"
    for i in disp:
        if i != "." and i != "x" and i == 0 or i == " ":
            return "cortar"
    equis = [-1] * 500000
    indice = 0
    for eq in range(len(disp)):
        if disp[eq] == "x":
            equis[indice] = eq
            indice+=1
    equis_indices = [0] * indice
    for i in range(indice):
        equis_indices[i] = equis[i]
    for izquierda in range(len(disp)):
        if disp[izquierda] == "x":
            lugares_izquierda = izquierda
            break
    for derecha in range(len(disp)-1,-1,-1):
        if disp[derecha] == "x":
            lugares_derecha = len(disp)-derecha-1
            break
    if lugares_izquierda >= lugares_derecha:
        mayor_esquina = lugares_izquierda
        mayor_indice = 0
    else: 
        mayor_esquina = lugares_derecha
        mayor_indice = -1
    mayor_cant_esquina = mayor_esquina-1
    diferencia = 0
    for lugares_disp in range(len(equis_indices)-1):
        inicio = equis_indices[lugares_disp]
        final = equis_indices[lugares_disp+1]
        dif_moment = final - inicio - 1
        if dif_moment > diferencia:
            empieza = equis_indices[lugares_disp]
            termina = equis_indices[lugares_disp+1]
            diferencia = dif_moment
    if diferencia%2 == 0: espacio_mas_grande = (diferencia/2)-1
    else: espacio_mas_grande = (diferencia//2)
    if espacio_mas_grande > mayor_cant_esquina: return(int(espacio_mas_grande))
    else:return(int(mayor_cant_esquina))
total = ""
termina = 0
while True:
    sumar  = resultado()
    if sumar == "cortar":
        break
    total+=str(sumar)
for r in total:
    print(r)