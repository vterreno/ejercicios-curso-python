intentos = int(input())
cadenas = [0] * intentos
for i in range(intentos):
    cadenas[i] = input()
result = [0] * intentos
cant = 0
for cantidad in range(intentos):
    cadena = cadenas[cantidad]
    for i in range(len(cadena)):
        if cadena[i] == "<":
            cadena = cadena[0:i] + "0" + cadena[i+1:len(cadena)]
            for j in range(i,len(cadena)):
                if cadena[j] == ">":
                    cadena = cadena[0:j] + "0" + cadena[j+1:len(cadena)]  
                    cant+=1 
                    break
    result[cantidad] = cant
    cant = 0
for i in result:
    print(i)
