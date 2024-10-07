def main():
    cp = int(input('Ingrese casos de prueba: '))

    for i in range(cp):
        camas = input('Camas: ')
        if len(camas) > 500000:
            break
        else:
            total_izq = leer_izq(camas)
            total_der = leer_der(camas)
            total_medio = leer_medio(camas)

            resultado = menor(total_der,total_izq,total_medio)
            if resultado == None:
                resultado = 0

            print(resultado)

def leer_izq(camas): # .....x
    total_izq = -1
    for i in range(len(camas)):
        if camas[i] == ".":
            total_izq += 1
        if camas[i] == "x":
            return total_izq
    return total_izq

def leer_der(camas): # x.....
    total_der = -1
    for i in range(len(camas) - 1, -1, -1):
        if camas[i] == ".":
            total_der += 1
        if camas[i] == "x":
            return total_der
    return total_der

def leer_medio(camas): # x....x
    distancia_actual = 0
    hay_x = False
    max_distancia_medio = 0

    for i in range(len(camas)):
        if camas[i] == "x":
            if hay_x:  # Si ya encontramos una 'x' antes, verificamos la distancia
                if distancia_actual % 2 == 0:  # Par
                    distancia_calculada = (distancia_actual // 2) - 1
                else:  # Impar
                    distancia_calculada = distancia_actual // 2

                # Asignamos el valor mayor entre lo que ya tenemos y la nueva distancia
                if distancia_calculada > max_distancia_medio:
                    max_distancia_medio = distancia_calculada
            hay_x = True  # Marcamos que hemos encontrado la primera 'x'
            distancia_actual = 0  # Reiniciamos el contador de distancia

        elif hay_x:  # Contamos las camas vacías entre 'x'
            distancia_actual += 1

    return max_distancia_medio

def menor(total_der,total_izq,total_medio):
    # Inicializamos una variable para almacenar el menor valor
    men = None

    # Comprobamos cada valor y actualizamos 'men' si es válido
    if total_der > 0:
        men = total_der
    if total_izq > 0:
        if men is None or total_izq > men:
            men = total_izq
    if total_medio > 0:
        if men is None or total_medio > men:
            men = total_medio

    return men

main()
