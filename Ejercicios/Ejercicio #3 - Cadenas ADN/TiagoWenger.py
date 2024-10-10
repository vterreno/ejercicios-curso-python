adn=1
while adn!=0 and adn<40000:
    adn=int(input())
    if adn!=0 and adn<40000:
        vec=[" "]*adn
        vec[0]=input()
        long=len(vec[0])
        if long<50:
            for i in range(1,adn):
                vec[i]=input()
                if long!=len(vec[i]):
                    print("Escribiste una ADN con diferente longitud")
                    break
            matriz = [[' ' for _ in range(long)] for _ in range(adn)]
            for i in range(adn):
                cadena = vec[i]
                for j in range(long):
                    matriz[i][j] = cadena[j]
            igual=[0]*adn
            for i in range(adn):
                cont=-1
                for x in range(adn):
                    resul=True
                    for j in range(long):
                        if matriz[x][j]!="-" and matriz[x][j]!=matriz[i][j] and matriz[i][j]!="-":
                            resul=False
                            break
                    if resul==True:
                        cont+=1
                igual[i]=cont
            for i in range(adn):
                print(igual[i], end=" ")
                
