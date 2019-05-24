#Programa desarrollado en clases práctica de la sección 07 de programación UCV
#Este programa determina cual de dos números introducidos por el usuario
#es mayor
num1 = int(input("Introduzca el primer Número: "))
num2 = int(input("Introduzca el segundo Número: "))

if num1 > num2:
    print("El número {} es mayor que {}".format(num1,num2))
else:
    if num1 == num2:
        print("Los número son iguales")
    else:
        print("El número {} es mayor que {}".format(num2,num1))
