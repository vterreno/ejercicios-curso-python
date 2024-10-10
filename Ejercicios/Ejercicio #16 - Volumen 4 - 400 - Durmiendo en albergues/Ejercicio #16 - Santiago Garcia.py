def camasdisp(prueba,situacion):
    espacios=-1
    bandera2=0
    espaciostotales=0
    if situacion==0:
        for i in range(len(prueba)):
            if prueba[i]==".":
                espacios+=1
            if prueba[i]=="x" or i==(len(prueba))-1:
                if espacios>espaciostotales and (bandera2==0 or i==(len(prueba))-1):
                    espaciostotales=espacios
                elif espacios/2>espaciostotales and espacios%2==0:
                    espaciostotales=int(espacios/2)
                elif espacios//2>espaciostotales:
                    espaciostotales=int(espacios/2)
                espacios=-1
                bandera2=1
    elif situacion==1:
        for i in range(len(prueba)):
            if prueba[i]==".":
                espacios+=1
            if prueba[i]=="x":
                if espacios/2>espaciostotales and espacios%2==0:
                    espaciostotales=int(espacios/2)
                elif espacios//2>espaciostotales:
                    espaciostotales=int(espacios/2)
                espacios=-1
    elif situacion==2:
        for i in range(len(prueba)):
            if prueba[i]==".":
                espacios+=1
            if prueba[i]=="x" or i==(len(prueba))-1:
                if espacios>espaciostotales and i==(len(prueba))-1:
                    espaciostotales=espacios
                elif espacios/2>espaciostotales and espacios%2==0:
                    espaciostotales=int(espacios/2)
                elif espacios//2>espaciostotales:
                    espaciostotales=int(espacios/2)
                espacios=-1
    else:
        for i in range(len(prueba)):
            if prueba[i]==".":
                espacios+=1
            if prueba[i]=="x":
                if espacios>espaciostotales and bandera2==0 :
                    espaciostotales=espacios
                elif espacios/2>espaciostotales and espacios%2==0:
                    espaciostotales=int(espacios/2)
                elif espacios//2>espaciostotales:
                    espaciostotales=int(espacios/2)
                espacios=-1
                bandera2=1
    return espaciostotales
caso=str(input()).lower()
resultados = [0] * 10000
i = 0
while caso!="":
    bandera=0
    if caso[0]=="x" and caso[len(caso)-1]=="x": bandera=1
    elif caso[0]=="x": bandera=2
    elif caso[len(caso)-1]=="x": bandera=3
    resultados[i] = camasdisp(caso,bandera)
    i += 1
    caso=str(input()).lower()
for i in range(i):
    print(resultados[i])
