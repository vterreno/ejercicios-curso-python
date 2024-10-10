gral=input()
camas=[0]*1000
cont=0
may=0
for i in range(len(gral)):
    if gral[i]=="X":
        camas[cont]=i
        cont+=1
for i in range(1,cont):
    dif=(camas[i]-camas[i-1])-1
    if (dif%2)==0:
        dist=(dif/2)-1
    else:
        dist=dif//2
    if dist>may:
        may=dist
if (camas[0]-1)>may:
    may=(camas[0]-1)
bord=len(gral)-camas[cont-1]- 1
if bord>may:
    may=bord
print(may)
