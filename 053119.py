#Programa desarrollado por Jeniffer Perez y Ruben Hernandez en el Lab. de Programación
#Practica 1.Parte A. El estudiante podrá ingresar un punto en el plano XY donde podrá obtener el punto en coordenadas polares (r,Tetha)
valor_1=float(input("Ingrese la coordenada X: ")) 
valor_2=float(input("Ingrese la coordenada Y: ")) 

import math

valor_r = math.sqrt(valor_1**2 + valor_2**2)

print(str("El valor de la coordenada r es: {} ".format(int(valor_r))))

if valor_1 == 0:
  print("El valor de la coordenada Theta es indeterminada")
  
if valor_1>0 and valor_2>0:
  valor_Theta = math.degree(math.atan(valor_2/valor_1)) + 0 #grados
  print("El valor de la coordenada Theta es: {} ".format(valor_Theta))
  
if valor_1<0 and valor_2>0:
  valor_Theta = abs(math.degree(math.atan(valor_2/valor_1)) + 90) #grados
  print("El valor de la coordenada Theta es: {} ".format(valor_Theta))
  
if valor_1<0 and valor_2<0:
  valor_Theta = math.degree(math.atan(valor_2/valor_1)) + 180 #grados
  print("El valor de la coordenada Theta es: {} ".format(valor_Theta))
  
if valor_1>0 and valor_2<0:
  valor_Theta = abs(math.degree(math.atan(valor_2/valor_1)) + 270) #grados
  print("El valor de la coordenada Theta es: {} ".format(valor_Theta))
  
