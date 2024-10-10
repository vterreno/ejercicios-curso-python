n=int(input())
for _ in range(n):
    #verificar ingreso valido
    while True:
        t=True
        e=str(input()).upper()
        if len(e)<500000:
            for i in range(len(e)):
                if e[i]!="." and e[i]!="X":
                    t=False
            if t==True:
                break
    max=0
    c=0
    t=True
    for i in range(len(e)):
        if e[i]=="X":
            #distancia extremo izquierdo
            if t==True:
                c=c-1
                t=False
            #distancia medio impar
            elif c%2!=0:
                c=int(c/2)
            else:
            #distancia medio par
                c=int(c/2)-1
            if c>max:
                max=c
            c=0
        else:
            c+=1
    #distancia extremo derecho
    c=c-1
    if c>max:
        max=c
    print(max)
