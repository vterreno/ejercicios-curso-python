#inicializo contadores
contador_camas_ocupadas=0
DistanciaMáxima=0

cadena=str(input())

#compruebo que cumpla con tener menos de 50mil caracteres
if len(cadena) < 500000:

    entrada=True
    
    #si cumple, verifico que solo sea de puntos y x
    for i in range(len(cadena)):
        if cadena[i] != "." and cadena[i] != "x":
            entrada=False 
            break
     
    #si cumple que sea de puntos y x    
    if entrada==True:
        
        #creo una subcadena para guardar las pos de las x (indices)
        subcadena=[0]*len(cadena)
        
        #verifico que los extremos sean x (por si la distancia max está en un extremo)
        
        if cadena[0] != "x":  #si el 1er elemento no es "x"
            cadena = "x" + cadena[1:]  #concateno "x" al inicio de la cadena 
        if cadena[-1] != "x":  #si el último elemento no es "x"
            cadena = cadena[:-1] + "x"  #concateno "x" al final de la cadena

        #recorro y cuento la cantidad de camas ocupadas    
        for i in range(len(cadena)):
            
            if cadena[i] == "x":
                subcadena[contador_camas_ocupadas] = i
                contador_camas_ocupadas += 1 

            
        subcadena=subcadena[:contador_camas_ocupadas]  #me quedo únicamente con la cantidad de camas ocupadas

        #print(subcadena)
        #print(contador_camas_ocupadas)
        
        
        for j in range(contador_camas_ocupadas-1):
            Distancia=subcadena[j+1]-subcadena[j] #calculo distancia

            Distancia -= 1 #resto uno para ajustar
            
            if Distancia % 2 == 0: #si es par
                DistanciaActual = (Distancia // 2) -1
            
            if Distancia == 1:
                DistanciaActual = 0
            
            if Distancia % 2 != 0 and DistanciaActual != 1: 
                DistanciaActual = Distancia//2
                

            if DistanciaActual > DistanciaMáxima:
                DistanciaMáxima = DistanciaActual

        print(DistanciaMáxima)
