def contar_diamantes(entrada):
    contador = 0 # Contador para verificar los diamantes "<>" encontrados
    diamantes = 0 # Contador para sumar la cantidad de diamantes "<>" encontrados

    for caracter in entrada:
        if caracter == "<":
            contador += 1 # Si se detecta un "<" (que sería el 'inicio' de un diamante), sumamos 1
        # Si se detecta un ">" ('cierre' de un diamante), y existe anteriormente un "<" ('inicio' de un diamante), restamos -1
        elif caracter == ">" and contador > 0:
            contador -= 1 # Reestablecemos la variable en 0
            diamantes += 1 # Indicamos que se encontró un (1) diamante

    return diamantes

N = int(input()) # Leemos la cantidad de casos de prueba
resultado = "" # Creamos una cadena vacía para acumular los resultados

for i in range(N):
    entrada = input()
    diamantes = contar_diamantes(entrada)  # Llamamos a la función
    resultado += str(diamantes) + "\n"  # Acumulamos los resultados en la cadena

print(resultado)