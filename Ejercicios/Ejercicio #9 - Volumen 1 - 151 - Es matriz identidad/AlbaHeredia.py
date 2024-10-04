#creo una VB para comparar los índices y otra para el ingreso
Ingreso=True


while Ingreso==True:
    
    #Ingreso la cantidad de filas
    f=int(input())
    
    #Si f es 0, se deja de ingresar
    if f==0:
        Ingreso=False
        break #sale del bucle
    
    #igualo c a f ya que debe ser una matriz cuadrada
    c=f
    
    #creo la matriz
    Matriz=[[0 for j in range(c)] for i in range(f)]
    
    #cargo los valores de la matriz en una misma línea
    for i in range(f):
        fila = input() 
        
        
        #inicializo una variable para ajustar el ind de la columna
        j = 0 
        
        #recorro la fila
        for k in range(len(fila)):
            if fila[k] != ' ':  #Si el elemento en la fila no es un espacio...
                Matriz[i][j] = int(fila[k])  #convierto a entero y asigno a la matriz
                j += 1  #incremento a la siguiente columna (ya que la que sigue sería un espacio)
            
    #creo una VB para verificar si es M.I
    VB=True 
            
    #recorro la matriz y verifico si los valores de la DP son 1 y el resto 0
    for i in range(f):
        for j in range(c):
            
            #confirmo que la DP sea de valores 1
            if i == j:
                if Matriz[i][j] != 1:
                    VB=False
                    
            #confirmo que el resto de la matriz esté llena de 0
            else:
                if Matriz[i][j] != 0:
                    VB=True
    
    if VB==True:
        print("SI")
    else:
        print("NO")
