#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Primer Examen Parcial

#import numpy
N = int(input("Ingrese la dimension de la matriz (PAR): "))

if N % 2 != 0:
    print("Error: el numero debe ser par")
else:
    #Rutina para generar secuencia de ordenamiento de las filas
    #de la matriz deseada
    sec = []
    for i in range(int(N/2)):
        sec.append(2*i)
    for i in reversed(range(int(N/2))):
        sec.append(2*i+1)

    #Rutina para generar una matriz auxiliar, llena de forma "ordenada"
    k = 1
    matrix = []
    for i in range(N):
        fila = []
        for j in range(N):
            fila.append(k)
            k += 1
        matrix.append(fila)

    matrix_aux = matrix.copy()

    #Reordenamiento de la matriz siguiende la secuencia deseada
    for i,j in enumerate(sec):
        matrix[i] = matrix_aux[j]

    #print(numpy.array(matrix))
