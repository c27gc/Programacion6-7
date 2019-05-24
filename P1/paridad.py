#Programa desarrollado en clases práctica de la sección 06 de programación UCV
#Este programa determina si un número introducido por el usuario es par o no
num = int(input("Introduzca el Número: "))

k = num % 2
if k == 0:
    print("El número es par")
else:
    print("El número es impar")
