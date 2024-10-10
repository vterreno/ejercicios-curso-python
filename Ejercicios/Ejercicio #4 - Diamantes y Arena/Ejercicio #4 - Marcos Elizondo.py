n=int(input())
while n!=0:
    cuenta=0
    cuenta2=0
    linea=input()
    for i in range(len(linea)-1):
        if linea[i]=="<":
            cuenta+=1
        if linea[i]==">" and cuenta!=0:
            if cuenta2+1<=cuenta:
                cuenta2+=1
    if linea[len(linea)-1] == '>' and cuenta2+1<=cuenta:
        cuenta2+=1
    
    print (cuenta2)

    n-=1
