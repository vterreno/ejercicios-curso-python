""" a = 5
nombre = "Juan"
print(f"Mi nombre es {nombre} y tengo {a} años", a)
 """
# Matriz
""" columnas = 10
filas = 10
matriz = [[int() for i in range(columnas)]for j in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = str(i) + str(j)
        print(matriz[i][j],end=" ")
    print(" ") """
def boolean(cadena):
    if cadena == "SI":
        return True
    else:
        return False

elementos = str
dimension = int(input("Ingrese la dimension de la matriz cuadrada: "))
solucion1 = "SI"
solucion2 = "SI"
matriz = [[int for i in range(dimension)]for j in range(dimension)]

for i in range(dimension):
    elementos = input("Ingrese los elementos de cada fila(la cantidad de elementos=dimensión): ")
    for j in range(dimension):
        matriz[i][j] = elementos[j]

for i in range(dimension):
    for j in range(dimension):
        if i > j and (matriz[i][j] != str(0)):
            solucion1 = "NO"

for i in range(dimension):
    for j in range(dimension):
        if i < j and (matriz[i][j] != str(0)):
            solucion2 = "NO"


solution = boolean(solucion1) or boolean(solucion2)

if solution == True:
    print("SI")
else:
    print("NO")
