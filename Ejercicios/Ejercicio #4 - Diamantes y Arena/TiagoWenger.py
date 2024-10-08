pruebas=int(input())
for i in range(pruebas):
    dya=input()
    bandera=False
    abrio=0
    dia=0
    while bandera==False:
        bandera=True
        for i in range(len(dya)):
            if dya[i]=="<":
                abrio=1
                indabrio=i
            if dya[i]==">" and abrio==1:
                dia+=1
                abrio=0
                bandera=False
                dya= dya[0:indabrio] + "D" + dya[indabrio+1:len(dya)]
                dya=dya[0:i] + "D" + dya[i:len(dya)]
                break
    print(dia)
