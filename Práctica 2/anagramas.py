#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Práctica de laboratorio Num 2

str_1 = input("Escriba la primera palabra: ")
str_2 = input("Escriba la segunda palabra: ")

lista_str_1 = list(str_1)
lista_str_2 = list(str_2)

if len(lista_str_1) != len(lista_str_2):
    print("Las palabras no son anagramas, tienen longitudes diferentes")
else:
    count = 0
    for i in lista_str_1:
        if i in lista_str_2:
            count += 1
            lista_str_2.pop(lista_str_2.index(i))

if count == len(lista_str_1):
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")
