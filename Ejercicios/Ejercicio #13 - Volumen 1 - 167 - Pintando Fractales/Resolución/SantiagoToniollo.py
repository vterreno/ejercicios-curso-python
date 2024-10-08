casos = int(input())
resultados = ""

for i in range(casos):
    contador = 1
    longitud = int(input())
    perimetro = longitud * 4
    
    while longitud > 1:
        perimetro += (4**contador) * (int(longitud/2)) * 4
        contador += 1
        longitud //= 2
        
    resultados += "\n" + str(perimetro)
    
print(resultados)