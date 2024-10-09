n=int(input())
for i in range(n):
    c=0 #contador "<"
    cd=0 # contador diamantes
    e=str(input())
    for z in range(len(e)):
        #encontramos "<"
        if e[z]=="<":
            c+=1
        #encontramos ">" y si ya encontramos "<" anteriormente entonces encontramos un diamante
        elif e[z]==">" and c>0:
            c-=1
            cd+=1
    print(cd)
