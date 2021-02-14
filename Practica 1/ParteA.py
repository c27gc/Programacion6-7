#Programa desarrollado por Ruben Hernandez y Jeniffer Perez en el Laboratorio de Programacion el dia 05/06/19
#Practica 1-A
#Este programa determina dadas unas coordenadas (x,y) de un punto en el plano, su equivalencia en coordenadas polares (R,θ)

valor_1=float(input("Ingrese la coordenada X: "))

valor_2=float(input("Ingrese la coordenada Y: "))

import math

valor_r = math.sqrt(valor_1**2 + valor_2**2)

if valor_1 ==0:
  
  print("El valor de la coordenada θ es indeterminada")
  
if valor_1>0 and valor_2>0:
  
  valor_θ= math.degrees(math.atan(valor_2/valor_1)) + 0 #Grados
  print("El valor de la coordenada θ es: {}".format(valor_θ))
  
if valor_1<0 and valor_2>0:
  
  valor_θ= abs(math.degrees(math.atan(valor_2/valor_1)) - 90) #Grados
  print("El valor de la coordenada θ es: {}".format(valor_θ))
  
if valor_1<0 and valor_2<0:
  
  valor_θ= math.degrees(math.atan(valor_2/valor_1)) + 180 #Grados
  print("El valor de la coordenada θ es: {}".format(valor_θ))

if valor_1>0 and valor_2<0:
  
  valor_θ= abs(math.degrees(math.atan(valor_2/valor_1)) - 270) #Grados
  print("El valor de la coordenada θ es: {}".format(valor_θ))
  
