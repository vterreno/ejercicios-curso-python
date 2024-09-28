def inserción(vector,long_vector):

    for i in range(1,long_vector):
        if vector[i] < vector[i-1]:
            auxiliar = vector[i]
            vector[i] = vector[i-1]
            vector[i-1] = auxiliar

            inserción(vector,long_vector)

    return vector

def ascendente(cadena):
    #Metemos cada uno de los números en un vector
    vector_nums = 4 * [0]
    for i in range(4):
        vector_nums[i] = num_aTrabajar[i:i+1]
    
    #Ordenamos con el método de inserción
    inserción(vector_nums,4)

    #Armamos la cadena nuevamente en base al vector ordenado
    ascendente = ""
    for i in range(4):
        ascendente = ascendente + str(vector_nums[i])

    return ascendente


#INICIALIZACIÓN DE VARIABLES
vector_nums = 100*[-1]

#ENTRADAS
repeticiones = int(input())

for i in range(repeticiones):

    #INICIALIZACIÓN DE VARIABLES
    contador = 0
    invalido = 0
    salir = 0

    #ENTRADAS
    num_ingresado = str(input())
    num_aTrabajar = num_ingresado

    #PROCESOS

    #Confirmamos que el número sea de 4 dígitos
    if len(num_aTrabajar) == 4:
        
        if num_aTrabajar == "6174":
            vector_nums[i] = contador
        else:
            #Confirmamos que el número esté formado por al menos 2 dígitos distintos
            if num_aTrabajar[0:1] == num_aTrabajar[1:2] and num_aTrabajar[0:1] == num_aTrabajar[2:3] and num_aTrabajar[0:1] == num_aTrabajar[3:4]:
                invalido = 1

            if invalido == 0:

                while salir == 0:
                    contador = contador + 1
                    #Ahora que verificamos los 4 dígitos los ordenamos en orden ascendente
                    num_ascendente = ascendente(num_aTrabajar)
                    #Invertimos a ascendente para obtener descendente
                    num_descendiente = num_ascendente[::-1]

                    resta = str(int(num_descendiente) - int(num_ascendente))

                    if resta == "6174":
                        vector_nums[i] = contador
                        salir = 1
                    
                    if len(resta) == 3:
                        resta = "0"+resta

                    if len(resta) == 2:
                        resta = "00"+resta
                    
                    if len(resta) == 1:
                        resta = "000"+resta

                    num_aTrabajar = resta

                vector_nums[i] = contador
            else:
                vector_nums[i] = 8
    else:
        print("ERROR: Ingrese un número de 4 dígitos")

#SALIDAS
for i in range(100):
    if vector_nums[i] != -1: 
        print(vector_nums[i])