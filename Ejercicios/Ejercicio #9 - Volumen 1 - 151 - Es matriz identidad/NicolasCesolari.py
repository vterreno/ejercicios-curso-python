def SepararEntrada(numeros, matriz, filas,f):
    c = 0  
    cantidad = len(numeros)
    numero = ""
    
    for i in range(cantidad):
        if numeros[i] != " ":
            numero += numeros[i]
        else: 
            if -1000<=int(numero)<=1000:
                matriz[f][c] = numero
                numero = ""
                c += 1
            else:
                return None,None
            
    if i == cantidad-1 and -1000<=int(numero)<=1000:
        matriz[f][c] = numero
    else:
        return None,None
    f += 1
    return matriz, f

def MatrizIdentidad(matriz, filas):
    #Abajo
    respuesta_1 = "SI"
    for i in range(1,filas,1):
        for j in range(0,i,1):
            if matriz[i][j] != "0":
                respuesta_1 = "NO" 
    #Arriba
    respuesta_2 = "SI" 
    k=1
    for i in range(0,filas-1,1):
        for j in range(k,filas,1):
            if matriz[i][j]!="0":
                respuesta_2 = "NO"
        k+=1 
    #Diagonal
    respuesta_3 = "SI"
    for i in range(filas):
        for j in range(filas):
            if i == j :
                if  matriz[i][j]!="1":
                    respuesta_3 = "NO"
            
    if respuesta_1 == "SI" and respuesta_2 == "SI" and respuesta_3 == "SI":
        return "SI"
    else: 
        return "NO"
#Algoritmo
bandera = True
while bandera:
    filas = int(input())
    if (filas != 0 and filas < 50):
        matriz = [[""]*filas for i in range(filas)]
        f = 0
        for i in range(filas):
            numeros = input()
            matriz,f = SepararEntrada(numeros, matriz,filas, f)
            if matriz == None:
                print("Error, los numeros deben cumplir las condiciones, seleccione de nuevo las filas y numeros")
                break
        if matriz!= None:
            respuesta =  MatrizIdentidad(matriz, filas)
            print(respuesta)
    else:
        bandera = False
