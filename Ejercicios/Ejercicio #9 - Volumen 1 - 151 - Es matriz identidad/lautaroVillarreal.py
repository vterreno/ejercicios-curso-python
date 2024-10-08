tamaño,result = int(input()),""
def carga_matriz():
    #definimos la matriz
    matriz = [[0 for c in range(tamaño)]for f in range(tamaño)]
    for filas in range(tamaño):
        #pedimos que se ingrese "palabra" (sea la fila de la matriz)
        palabra = input()
        
        #si la palabra tiene un espacio al final, se lo quitamos
        if palabra[-1] == " ": palabra = palabra[0:len(palabra)-1]
        
        
        numero,col = "",0
        for i in range(len(palabra)):
            #recorremos la palabra mientras sea distinta a un espacio y la guardamos en "num"
            if palabra[i] != " ": numero+=palabra[i]
            
            #si el caracter es un espacio, hacemos entero a la variable num y la incertamos en la matriz
            else:
                matriz[filas][col] = int(numero)
                col+=1
                numero = ""
        #Incertamos lo que quedó de la palabra el final de la matriz
        matriz[filas][col] = int(numero)
        
    return matriz

def resultado():
    #iniciamos la variable en la que vamos a sumar, y a la que usamos para controlar la diagonal
        suma,esquina = 0,0
        for f in range(tamaño):
            if f == esquina:
                #verificamos lo que hay en la esquina, si es distinto de 1, entonces la matriz no es D.
                if matriz[esquina][esquina] != 1:
                    esquina+=1
                    return "NO"
            for c in range(tamaño):
                #sumamos toda la diagonal, suma la cual (en la mat. identidad) debe ser si o si igual al rango.
                suma+=matriz[f][c]
                
                #vemos si la suma de la diagonal es igual al rango, si es mayor quiere decir que en la misma hay algo destinto de 1.
                if suma > tamaño: return "NO"
        #si la suma es igual al tamaño, entonces es diagonal
        if suma == tamaño: return "SI"
        suma,esquina = 0,0
while tamaño != 0:
    matriz = carga_matriz()
    result+=resultado()
    tamaño = int(input())

#imprimimos la cadena de resulado utilizandola como subcadena
for i in range(0,len(result),2): print(result[i:i+2])