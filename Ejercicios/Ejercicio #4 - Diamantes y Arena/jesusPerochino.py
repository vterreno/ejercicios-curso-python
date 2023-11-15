

ent = int (input())
vector=[int for i in range(ent)]
for j in range(ent):
    
    en = input()
    cont1 = 0
    
    
    for i in range(len(en)):
        if en[i] == "<":

            x= i
            encontrado = True
            while encontrado and x < len(en):   
              
                if en[x] == ">":
                    en = en[0:x] + "." +en[x+1:]
                    cont1 += 1
                    encontrado = False
                    
                x += 1
    vector[j] = cont1


for i in range(ent):
    print(vector[i])