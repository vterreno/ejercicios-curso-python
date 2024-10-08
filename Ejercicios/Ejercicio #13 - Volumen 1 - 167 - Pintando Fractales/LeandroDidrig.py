try:
    n = int(input())
    arr = [int(0)]*100
    f = 0
    while n!=-1:
        acumulador = 0
        contador = 1
        while n!=1:
            acumulador += contador*(n*4)
            n //= 2
            if contador == 1:
                contador = 4
            else:
                contador *= 4
        acumulador += contador*4
        arr[f] = acumulador
        f += 1
        n = int(input())
    
except ValueError:
    for k in range(f):
        print(arr[k])
