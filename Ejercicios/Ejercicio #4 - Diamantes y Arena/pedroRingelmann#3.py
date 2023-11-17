a = int(input())
vector = [0] * a

for i in range(a):
    pal = str(input())
    v = []
    for j in range(len(pal)):
        v.append(pal[j])    
    print(v)
    for h in range(len(v)):
        if v[h] == "<":
            for m in range(h+1, len(v)):
                if v[m] == ">":
                    vector[i] = vector[i] + 1
                    v[m] = "."

for i in range(a):  
    print(vector[i])



