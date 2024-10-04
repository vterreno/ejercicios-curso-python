i = j = filxcol = f = f2 = fr = numerito = 0
mat = [[0 for _ in range(50)] for _ in range(50)]
resultados = [0.0 for _ in range(100)]

while True:
    filxcol = int(input("Dimension: ")) 
    if 0 < filxcol <= 50:
        f = f2 = 0
        #en el for ahora trato cada fila como cadena para poder poner por ejemplo : 1 0 0 (enter)
        #asi evito poner un numero por linea
        for i in range(filxcol):
            fila_input = input(f"Fila {i + 1}: ")  
            j = 0
            numcadena = ""  

            for caracter in fila_input:
                if caracter != " ":  
                    numcadena += caracter  
                else:
                    if numcadena:  
                        numerito = int(numcadena)  
                        if not (-1000 <= numerito <= 1000):
                            f = f2 = 1
                        else:
                            mat[i][j] = numerito  
                            j += 1
                        numcadena = ""  
            
            
            if numcadena:
                numerito = int(numcadena)
                if not (-1000 <= numerito <= 1000):
                    f = f2 = 1
                else:
                    mat[i][j] = numerito
            
        if not f:
            for i in range(filxcol):
                for j in range(filxcol):
                    if (i == j and mat[i][j] != 1) or (i != j and mat[i][j] != 0):
                        f2 = 1
        
        resultados[fr] = 1 if not f2 else 0
        fr += 1
    else:
        if filxcol != 0:
            resultados[fr] = -1
            fr += 1
    
    if filxcol == 0:
        break

for i in range(fr):
    if resultados[i] == 1:
        print("SI")
    elif resultados[i] == 0:
        print("NO")
    elif resultados[i] == -1:
        print("INVALIDO") #por si ingreso un valor para la dimension fuera del rango (0 a 50)
