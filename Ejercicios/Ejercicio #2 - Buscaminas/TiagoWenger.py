f=1
c=1
while f!=0 and c!=0:
    f=int(input())
    c=int(input())
    if  f!=0 and c!=0:
        mat = [[" " for _ in range(c)] for _ in range(f)]
        for i in range(f):
            fila=input()
            for j in range(c):
                mat[i][j]=fila[j]
        tab = [["0" for _ in range(c+2)] for _ in range(f+2)]
        for i in range(1,f+1):
            for j in range(1,c+1):
                tab[i][j]=mat[i-1][j-1]
    seisminas=0
    for i in range(1,f+1):
        for j in range(1,c+1):
            cont=0
            if tab[i][j]=="-":
                for y in range(i-1,i+2):
                    for x in range(j-1,j+2):
                        if tab[y][x]=="*":
                            cont+=1
                if cont>=6:
                    seisminas+=1
    print(seisminas)