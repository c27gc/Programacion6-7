#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Primer Examen Parcial

H = int(input("Ingrese altura del pozo: "))
Ld = int(input("Ingrese Ld: "))
Ln = int(input("Ingrese Ln: "))

H_acu = 0
count = 0
if Ld <= Ln:
    print("El caracol nunca sale del pozo.")
else:
    while(True):
        H_acu = H_acu + Ld
        count += 1
        if H_acu >= H:
            break
        H_acu = H_acu - Ln
    print("El caracol sube en {} dias".format(count))
