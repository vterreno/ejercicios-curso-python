def fractal(num,c):
    if int(num/(2**(c-1)))==0:
        return 0
    else:
        return(int(num/(2**(c-1)))*(4**c)+fractal(num,c+1))
n=int(input())
for _ in range(n):
    c=1
    num=int(input())
    sum=fractal(num,c)
    print(sum)
