n = int(input())
while n!=0:
    matriz = [[int(0) for i in range(n)]for j in range(n)]
    inferior = 0
    superior = 0
    for i in range(n):
        num = str(input())
        filita = num.split()
        for j in range(n):
            filita[j] = int(filita[j])
        matriz[i] = filita
    for i in range(n):
        for j in range(n):
            if i!=j and i>j:
                if matriz[i][j] != 0 :
                    inferior =1
    for i in range(n):
        for j in range(n):
            if i!=j and i<j:
                if matriz[i][j] != 0:
                    superior = 1
    if inferior == 1 and superior == 1:
        print('NO')
    else:
        print('SI')
    n = int(input())
