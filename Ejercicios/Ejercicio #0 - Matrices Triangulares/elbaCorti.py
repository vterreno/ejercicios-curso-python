secuencia = input("Ingrese la secuencia de caracteres: ")

vocal_natural = ""
vocal_inverso = ""


for letra in secuencia:
    if letra in "aeiou":
        
        vocal_natural += letra
        vocal_inverso = letra + vocal_inverso

if vocal_natural == vocal_inverso:

    print ("S")
else:
    print ("N")