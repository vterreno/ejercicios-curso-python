
def contardiamantes (diamantes):
    diam = []
    diamantes1 = 0 
    for i in range(len(diamantes)):
        if diamantes[i]=="<":
            diam.append(diamantes[i])
        elif diamantes[i] == ">" and diam:
            diam.pop ()
            diamantes1 += 1
    return diamantes1
    

cantidad= int(input("Cantidad de casos de prueba:"))

for _ in range(cantidad):
    diamantes=str(input("Ingresar diamantes:"))
    resultado = contardiamantes (diamantes)
    print(resultado)




