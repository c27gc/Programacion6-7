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
    matrix_aux = [[i+N*j for i in range(1,N+1)] for j in range(N)]
    sec = [2*i for i in range(int(N/2))] + [2*i+1 for i in reversed(range(int(N/2)))]
    matrix = [matrix_aux[j] for j in sec]
    #print(numpy.array(matrix))
