entrada = int(input())

while (entrada% 2) != 0:

    matriz = [[str() for ind0 in range(1*entrada)]for ind1 in range(1*entrada)]

    for i in range(entrada):
        pal = str(input())
        vec = pal.split(" ")
        for h in range(entrada):
            matriz[i][h] = int(vec[h])

    i = round((entrada-1)/2)
    h = round((entrada-1)/2)

    suma = matriz[i][h] 


    if entrada > 1 :
        suma = suma + matriz[i-1][h]
        i = i - 1


    cont = 3
    cond = True
    a = 1

    while cond == True:
        for j in range(1,cont):
            if (h+j) <= (entrada-1):
                suma = suma + matriz[i][h+j]
                a = a + 1

        if a == cont:
            h = h + j
            a = 1
            cont = cont + 1
        else:
            a = 1
            cond = False

        for j in range(1,cont):
            if (i+j) <= (entrada-1):
                suma = suma + matriz[i+j][h]
                a = a + 1
        if a == cont:
            i = i + j
            a = 1
            cont = cont + 1
        else:
            a = 1
            cond = False

        if cond == True:
            for j in range(1,cont):
                if (h-j) >= (0):
                    suma = suma + matriz[i][h-j]
                    a = a + 1
            if a == cont:
                h = h - j
                a = 1
                cont = cont + 1
            else:
                a = 1
                cond = False

        if cond == True:
            for j in range(1,cont):
                if (i-j) >= (0):
                    suma = suma + matriz[i-j][h]
                    a = a + 1
            if a == cont:
                i = i - j
                a = 1
                cont = cont + 1
            else:
                a = 1
                cond = False

    print(suma)
    entrada = int(input())


