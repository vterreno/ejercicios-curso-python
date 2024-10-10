

n=int(input())
guardo=""
guardo2=""
for i in range(n):
    horas=str(input())
    for n in range(len(horas)):

        if horas[n] != ":":
            guardo2 += horas[n]
    
        if horas[n] == ":":
            guardo=guardo2
            guardo2=""
    h=23-int(guardo)
    m=(59-int(guardo2))+1

    j= h * 60 
    suma =j + m
    print(suma)
