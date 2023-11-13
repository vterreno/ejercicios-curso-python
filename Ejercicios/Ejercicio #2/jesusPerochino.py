en = input().split()
respuestas = [0]*100
pos = 0
while int(en[0]) != 0 and int(en[1]) != 0:
	matriz = [[""]*int(en[0])]*int(en[1])
	for i in range(int(en[1])):
		en2 = input()
		for j in range(int(en[0])):
			matriz[i][j] = en2[j]
	
	for i in range(1,int(en[1])-1):
		rodeando = 0
		for j in range(1, int(en[0])-1):
			if matriz[i][j] == "-":
				rodeando += int(matriz[i-1][j] == "*")
				rodeando += int(matriz[i+1][j] == "*")
				rodeando += int(matriz[i+1][j+1] == "*") 
				rodeando += int(matriz[i+1][j-1] == "*" )
				rodeando += int(matriz[i-1][j-1] == "*" )
				rodeando += int(matriz[i-1][j+1] == "*" )
				rodeando += int(matriz[i][j+1] == "*" )
				rodeando += int(matriz[i][j-1] == "*")
				if rodeando >= 6:
					respuestas[pos] += 1
	pos += 1
	en = input().split()
for i in range(pos):
	print(respuestas[i]) 