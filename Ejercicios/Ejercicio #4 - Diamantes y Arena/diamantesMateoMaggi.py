casos_de_prueba = int(input())
caracteres_disponibles = '><.'
entrada_correcta = True
while casos_de_prueba != 0:
    diamantes = int(0)
    entrada = input()
    vector = [""]*len(entrada)
    num = int(0)
    for i in entrada:
        vector[num] = i
        num += 1
        if i not in caracteres_disponibles:
            entrada_correcta = False
    if entrada_correcta == True:
        for k in range(0,len(vector)):
            if vector[k] == '<':
                b = int(0)
                for a in range(k,len(vector)):
                    if vector[a] == '>' and b == 0:
                        diamantes += 1
                        vector[a] = '.'
                        b = 1
    print(diamantes)
    casos_de_prueba -= 1