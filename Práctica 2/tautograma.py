#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Práctica de laboratorio Num 2

#Rutina para leer el numero, valida que la oración tenga más de una palabra.
count = 3
while(count != 0):
    str_1 = input("Ingrese la Oración: ")
    if (" " in str_1) and (str_1.index(" ") != len(str_1)):
        break
    else:
        print("Debe ingresar una oración (al menos dos palabras), le restan {} intentos".format(count-1))
        count -= 1

#Rutina para eliminar espacios en blanco entre las palabras
for i in reversed(range(2,len(str_1))):
    if i*" " in str_1:
        while(i*" " in str_1):
            ind = str_1.index(i*" ")
            str_1 = str_1[0:ind] + " " + str_1[ind+i:]
            
lista_str_1 = list(str_1.lower())
tauto = True
#Rutina para borrar caracteres en blanco al principio de la cadena
while(True):
    if lista_str_1[0] == " ":
        lista_str_1.pop(0)
    else:
        break

#Rutina para verificar que la cadena sea un tautograma
letra_tau = lista_str_1[0]
for letra in lista_str_1:
    if  letra == " ":
        index = lista_str_1.index(" ")
        lista_str_1[index] = "*"
        tauto = letra_tau == lista_str_1[index + 1]
    if not tauto:
        break

if count == 0:
    tauto = "[Error]: El programa requiere como entrada al menos dos palabras. "
print(tauto)
