n = int(input())
vector = [int(0)]*n

for i in range(n):
    izquierdas = 0
    diamonds = 0
    minar = str(input())

    for j in range(len(minar)):
        if minar[j] == '<':
            izquierdas += 1
        if minar[j] == '>':
            if izquierdas>=1:
                diamonds+=1
                izquierdas-=1
                
    vector[i] = diamonds
for k in range(n):
    print(vector[k])
