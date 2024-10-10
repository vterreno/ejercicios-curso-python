def main():
    cp = int(input('Casos de prueba: '))

    for i in range(cp):
        expresion = input('Expresion: ')

        diamantes = verificar(expresion)
        print(diamantes)

def verificar(expresion):
    cant_diamantes = 0  # Contador de diamantes formados
    cant_a = 0  # Contador de '<'

    for i in range(len(expresion)):
        if expresion[i] == "<":
            cant_a += 1
        elif expresion[i] == ">":
            if cant_a > 0:  # cuento si hay un '<' disponible
                cant_diamantes += 1
                cant_a -= 1

    return cant_diamantes

main()