#funcion para contar diamantes
def contar_diamantes(casos, N):
    for i in range(N):
        aperturas = 0
        diamantes = 0
        
        for caracter in casos[i]:
            if caracter == "<":
                aperturas += 1  
            elif caracter == ">" and aperturas > 0:
                diamantes += 1  
                aperturas -= 1  
        
        print(diamantes)  

#leer número de casos de prueba
N = int(input("Ingresa el número de casos de prueba: "))
casos = [input() for i in range(N)]

#procesar y mostrar los resultados
contar_diamantes(casos, N)
