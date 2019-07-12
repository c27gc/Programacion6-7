#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Primer Examen Parcial

N = int(input("Introduzca un numero N: "))
count = 0
for i in range(1,N):
    val = i
    while(val != 89 and val != 1):
        val = sum([int(w)**2 for w in str(val)])

    if val == 89:
        count += 1


print(count*100/(N-1))
