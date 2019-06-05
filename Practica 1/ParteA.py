#Programa desarrollado por Ruben Hernandez.
#Este programa determina dadas unas coordenadas (x,y) de un punto en el plano, su equivalencia en coordenadas polares (R,θ).

valor_1=float(input("Ingrese la coordenada X: "))
valor_2=float(input("Ingrese la coordenada Y: "))
import math
valor_r = math.sqrt(valor_1**2 + valor_2**2)
print(str("El valor de la coordenada r es: {} ".format(int(valor_r))))
valor_θ = math.atan(valor_2/valor_1)
print(str("El valor de la coordenada θ es: {} ".format(float(valor_θ))))
