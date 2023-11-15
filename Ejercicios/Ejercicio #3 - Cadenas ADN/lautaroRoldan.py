indice = int(input())
vec = []

def cond(vec,vec2):
    for j in range(len(vec)):
        if vec[j] == vec2[j] or vec[j] == "-" or vec2[j] == "-":
            return True

def cond2(vec,vec2):
    comp = "-"
    letra=["A","T","G","C"]
    cond = True
    for i in range(len(letra)):
        if (str(letra[i]) in vec) == True:
            comp = letra[i]
            break
    if comp != "-":
        for h in range(len(letra)):
            if comp != letra[h]:
                if (str(letra[h]) in vec2) == True:
                    cond = False
    return cond
    

if indice != 1:
    for i in range(indice):
        pal = str(input())
        prueba=[" "]*len(pal)
        for m in range(len(pal)):
            prueba[m] = pal[m]
        vec.append(prueba)

    res=[0]*indice
    cont = 0
    
    for i in range(len(vec)):
        for m in range(len(vec)):
            if i != m:
                cod1 = cond(vec[i],vec[m])
                cod2 = cond2(vec[i],vec[m])    
                if cod1 == True and cod2 == True:
                    res[i] = res[i] + 1                 
                                           
else:
    for i in range(indice):
        pal = str(input())
        prueba=[" "]*len(pal)
        for m in range(len(pal)):
            prueba[m] = pal[m]
        vec.append(prueba)
    res = 0

print(res)