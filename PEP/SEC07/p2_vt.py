#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Primer Examen Parcial

M = int(input("Ingrese el numero de terminos para la aproximacion: "))

acu = 0
for i in range(1,M+1):
    acu = acu + (-1)**(i+1) * (1/i**6)

pi = (30240*acu/31)**(1/6)

print(pi)
