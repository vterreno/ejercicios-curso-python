def separar_numeros(numeros,n):
    e = [int(0)]*100
    numbers = [int(0)]*n
    f = 1
    for i in range(len(numeros)):
        if (numeros[i]==' '):
            e[f] = i
            f += 1
    e[f] = len(numeros)
    b = 0
    a = 1
    for i in range(f):
        if i == 0:
            numbers[i] = int(numeros[e[b]:e[a]])
            a += 1
            b += 1
        else:  
            numbers[i] = int(numeros[e[b]+1:e[a]])
            a += 1
            b += 1
    return numbers

n = int(input())
VoF = [str(0)]*1000
indice = 0
k = 0
while n!=0:
    matriz = [[int(0) for i in range(n)]for j in range(n)]
    identidad = 0
    for i in range(n):
        num = str(input())
        filita = separar_numeros(num,n)
        for j in range(n):
            filita[j] = int(filita[j])
        matriz[i] = filita
    for i in range(n):
        for j in range(n):
            if i!=j:
                if matriz[i][j] != 0 :
                    identidad = 1
            if i==j:
                if matriz[i][j] != 1:
                    identidad = 1
    if identidad == 1:
        VoF[indice] = "NO"
        indice += 1
    else:
        VoF[indice] = "SI"
        indice += 1
    k += 1
    n = int(input())
for i in range(k):
    print(VoF[i])
