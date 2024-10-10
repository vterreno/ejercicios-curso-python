def main():
    cp = int(input('Casos de prueba: '))

    for i in range(cp):
        n = int(input('Numeros: '))
        if n == 1:
            print(4)
        else:
            total = fractal(n)
            print(total)

def fractal(n):
    exponente = 1
    total = 4 * n
    while n != 1:
        n = n // 2
        total += (4 * n) * (4 ** exponente)
        exponente += 1
    return total
main()
