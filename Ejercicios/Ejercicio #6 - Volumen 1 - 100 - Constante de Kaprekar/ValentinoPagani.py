n = int(input())
for _ in range(n):
    num = input()
    cont = 0
    while num != '6174':
        aux = [''] * 4
        mayor = ''
        menor = ''
        for i in range(4):
            aux[i] = num[i]

        aux.sort(reverse=True)
        for may in range(4):
            mayor += aux[may]

        aux.reverse()
        for men in range(4):
            menor += aux[men]

        num = str(int(mayor) - int(menor))

        cont += 1

    print(cont)
