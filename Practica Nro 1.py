#Programa desarrollado por Jeniffer Perez y Ruben Hernandez en el Lab. de Programacion.
#El estudiante podrá obtener la distancia entre dos puntos en el plano XY asi mismo el punto medio entre ambos.

valor_1=float(input("Ingrese la coordenada X1: "))
valor_2=float(input("Ingrese la coordenada X2: "))
valor_3=float(input("Ingrese la coordenada Y1: "))
valor_4=float(input("Ingrese la coordenada Y2: "))

import math

valor_d = math.sqrt((valor_2 - valor_1)**2 + (valor_4 - valor_3)**2)
print(str("La distancia entre los dos puntos es: {} ".format(int(valor_d))))
valor_m1 = ((valor_1 + valor_2)/2)
valor_m2 = ((valor_3 + valor_4)/2)
print(str("La coordenada del punto medio en X es: {}".format(float(valor_m1))))
print(str("La coordenada del punto medio en Y es: {}".format(float(valor_m2))))
