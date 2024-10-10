Casos=int(input())

for i in range(Casos):
    Cadena=str(input("Entrada: "))
    
    if len(Cadena) <= 1000:
        
        Ingreso=True
        
        for j in range(len(Cadena)):
            if Cadena[j] != "<" and Cadena[j] != ">" and Cadena[j] != ".":
                Ingreso=False
                break
         
        #Contador de diamantes
        Diamantes=0
        #Contador de picos abiertos
        Diamante_izq=0
    
        if Ingreso:
            for k in range(len(Cadena)):
                if Cadena[k] == "<": #inicio de diamante
                    Diamante_izq+=1
                    
                if Cadena[k] == ">" and Diamante_izq > 0: 
                    Diamantes+=1
                    Diamante_izq-=1
        print(Diamantes)
