N = int(input())
casos = "" #acumulador para los resultados
contador = 0 #para el número de casos procesados

while contador < N: 
    caso = input()
    diamantes = 0
    contador_diamantes = 0
        
    for caracter in caso:
        if caracter == "<":
            contador_diamantes += 1  #encontramos un "<"
        else:
            if caracter == ">":
                if contador_diamantes > 0:  #si hay un "<", formamos el diamante
                    diamantes += 1
                    contador_diamantes -= 1  
            
    casos += str(diamantes)
    contador += 1 
print(casos)             
       
        