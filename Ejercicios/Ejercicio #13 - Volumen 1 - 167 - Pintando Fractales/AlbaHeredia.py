Casos = int(input())

for i in range(Casos):
    Longitud = int(input())
    
    Exp_4 = 1  #potencias de 4
    
    Tinta = Longitud * 4  #cuadrado grande
    
    while Longitud != 1: 
        
        Longitud=Longitud//2 #reduzco el cuadrado a la mitad
        
        Tinta = Tinta + (Longitud*4) * (4 ** Exp_4)

        Exp_4 += 1
        
    print(Tinta)
