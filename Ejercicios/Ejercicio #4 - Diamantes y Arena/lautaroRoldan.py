a = int(input())
vector =[0]*a

def sep(palabra):
    vec =[]
    for i in range(len(palabra)):
        vec.append(palabra[i])
    return vec

for i in range(a):
    pal = str(input())
    vec = sep(pal)
    for h in range(len(vec)):
        if vec[h] == "<":
            for m in range(h+1,len(vec)):
                if vec[m] == ">":
                    vector[i] = vector[i] + 1
                    vec[m] = "."                 

for i in range(a):
    print(vector[i])