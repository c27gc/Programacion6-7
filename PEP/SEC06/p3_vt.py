#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Primer Examen Parcial

#import numpy
N = int(input("ingrese N: "))
M = int(input("ingrese M: "))

matrix = []
K = 1
for j in range(N):
    fila = []
    for i in range(K,M+K):
        fila.append(i)
    K = K + M
    if j % 2 != 0:
        fila = list(reversed(fila))
    matrix.append(fila)

#print(numpy.array(matrix))
