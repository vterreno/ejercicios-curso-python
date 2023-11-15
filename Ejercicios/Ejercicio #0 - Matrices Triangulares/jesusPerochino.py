


salidas = [None] * 50
pos = 0
rango = int(input())
while rango > 0 and rango <= 50:
	
	matriz = [None]*rango
	for x in range(rango):
		linea = input().split()
		matriz[x] = linea

	entre = True
	salidas[pos] = True  # Matriz triangular
	if int(matriz[0][1]) == 0:
		inicio = 1
		for i in range(0,rango-1):
			for j in range(inicio,rango-1):
				if (int(matriz[i][j]) != 0):
					salidas[pos] = False
					inicio += 1
		entre = False
	else:
		for i in range(1,rango):
			fin = rango - i
			for j in range(0,rango-1):
				if (int(matriz[i][j]) != 0) :
					salidas[pos] = False
		entre = False
	if entre:
		salidas[pos] = False

			
	pos += 1
	rango = int(input())

for i in range(pos):
	if salidas[i]:
		print("SI")
	else:
		print("NO")