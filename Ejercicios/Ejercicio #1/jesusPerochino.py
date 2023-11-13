n = 3
estrellas = [0] *100
indice = 0

while n%2 == 1:
	n = int ( input())
	if n%2 == 1:

		matriz = [[int for i in range(n)]for x in range(n)]
		for i in range(n):
			carga = input(). split()
			for j in range(n):
				matriz[i][j] = int(carga[j])
		
		contpos = 1
		paso = -1
		posini = n // 2
		posinj = n // 2
		ciclo = 0
		
		while contpos <= n:
			if contpos <= n and ciclo == 0:
				i = 0
				while posini > -1 and i != contpos: 
					estrellas[indice] += matriz[posini][posinj]
					

					i += 1
					posini -= 1
				
				contpos += 1
				ciclo = 1
			elif contpos <= n and ciclo == 1:
				j = 0
				while  posinj < n and j != contpos: 
					
					estrellas[indice] += matriz[posini][posinj]

					posinj += 1
					j += 1
				contpos += 1
				
				ciclo = 2
				
			elif contpos <= n and ciclo == 2 and posinj < n:
				i = 0

				while  posini < n  and i != contpos: 
					
					estrellas[indice] += matriz[posini][posinj]
					posini += 1
					i += 1
				contpos += 1
				
				 
				
				ciclo = 3
			elif contpos <= n and ciclo == 3:
				j = 0
				while posinj > -1 and j != contpos: 
					
					estrellas[indice] += matriz[posini][posinj]

					posinj -= 1
					j += 1
				contpos += 1
				

				
				ciclo = 0
			else:
				contpos += 1
		indice += 1


for i in range(indice):
	print(estrellas[i])