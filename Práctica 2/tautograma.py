#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Carlos E. González C.
#Práctica de laboratorio Num 2

str_1 = input("Ingrese la Oración: ")
lista_str_1 = list(str_1)
tauto = True
flag = True
#Rutina para borrar caracteres en blanco al principio de la cadena
while(True):
    if lista_str_1[0] == " ":
        lista_str_1.pop(0)
    else:
        break
#Rutina para verificar que la cadena sea un tautograma
for letra in lista_str_1:
    if  letra == " ":
        index = lista_str_1.index(" ")
        if flag:
            letra_tau = lista_str_1[index + 1]
            flag = not flag
        else:
            tauto = letra_tau == lista_str_1[index + 1]
    if not tauto:
        break

print(tauto)
