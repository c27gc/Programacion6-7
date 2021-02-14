#Programa desarrollado por Ruben Hernandez.
#Este programa determina la distancia entre dos puntos del plano XY, introducidos por el usuario y el punto medio entre ellos.

print("")
valor_1=float(input("Ingrese la coordenada X1: "))
print("")
valor_3=float(input("Ingrese la coordenada Y1: "))
print("")
valor_2=float(input("Ingrese la coordenada X2: "))
print("")
valor_4=float(input("Ingrese la coordenada Y2: "))
print("")

import math

valor_distancia = math.sqrt((valor_2 - valor_1)**2 + (valor_4 - valor_3)**2)

print(str("La distancia entre los dos puntos es: {} ".format(int(valor_distancia))))
print("")

valor_puntomedioX = (valor_1 + valor_2)/2
valor_puntomedioY = (valor_3 + valor_4)/2

print(str("La coordenada del punto medio en X es: {} ".format(float(valor_puntomedioX))))
print("")
print(str("La coordenada del punto medio en Y es: {} ".format(float(valor_puntomedioY))))
