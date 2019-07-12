#Universidad Central de Venezuela
#Facultad de Ingeniería
#Departamento de Investigación de Operaciones y Computación
#Programación, Python
#Programa realizado por:
#Prof. Carlos E. González C.
#Primer Examen Parcial

for n in range(0,3):
    num = input("Ingrese numero: ")
    if len(list(str(num))) >= 4:
        Val = True
        break
    else:
        print("Error, el número debe poseer al menos 4 digitos")
        Val = False


if Val:
    lenN = len(str(num))
    numsAl = []
    print("N\t N**2\t NumAl")
    for i in range(0,20):
        num_quad_str = str(int(num)**2)
        while(len(num_quad_str) < 2*lenN):
            num_quad_str = '0'+num_quad_str

        Al = float("0." + num_quad_str)
        print("{}\t {}\t {}".format(num,num_quad_str,Al))
        num = num_quad_str[int(len(num)/2):int(len(num)/2)+len(num)]
