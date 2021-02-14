def vallnt(*args):
    """DocString"""
    if len(args)==1:print("True") if type(args[0])==type(4) else print("False")
    if len(args)==2:
        print("True") if type(args[0])==type(4) and type(args[1])==type([1,2]) and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[0])==type(4) and type(args[1])==type((1,2)) and args[0]>args[1][0] and args[0]<args[1][1] else print("False")
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
        if type(args[1])!=type([1,2]) and type(args[1])!=type((1,2)):raise TypeError("El segundo argumento solo recibe tipo list o tupl y usted ha ingresado un tipo: {}".format(type(args[1])))
    if len(args)>2 or len(args)==0: print("La fauncion vallnt solo acepta 1 o 2 argumentos")
    return args
def valFloat(*args):
    """DocString"""
    if len(args)==1:print("True") if type(args[0])==type(4.1) else print("False")
    if len(args)==2:
        print("True") if type(args[0])==type(4.1) and type(args[1])==type([1,2]) and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[0])==type(4.1) and type(args[1])==type((1,2)) and args[0]>args[1][0] and args[0]<args[1][1] else print("False")
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
        if type(args[1])!=type([1,2]) and type(args[1])!=type((1,2)):raise TypeError("El segundo argumento solo recibe tipo list o tuple y usted ha ingresado un tipo: {}".format(type(args[1])))
    if len(args)>2 or len(args)==0:print("La funcion valFloat solo acepta 1 o 2 argumentos")
    return args
def valComplex(*args):
    """DocString"""
    if len(args)==1:print("True") if type(args[0])==type(4+4j) else print("False")
    if len(args)==2:
        print("True") if type(args[0])==type(4+4j) and type(args[1])==type([1,2]) and abs(args[0])>=args[1][0] and abs(args[0])<=args[1][1] or type(args[0])==type(4+4j) and type(args[1])==type((1,2)) and abs(args[0])>args[1][0] and abs(args[0])<args[1][1] else print("False")
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
        if type(args[1])!=type([1,2]) and type(args[1])!=type((1,2)):raise TypeError("El segundo argumento solo recibe tipo list o tuple y usted ha ingresado un tipo: {}".format(type(args[1])))
    if len(args)>2 or len(args)==0:print("La funcion valFloat solo acepta 1 o 2 argumentos")
    return args
def valList(*args):
    """DocString"""
    if len(args)==1:print("True") if type(args[0])==type([1,2]) else print("False")
    if len(args)==3:
        print("True") if type(args[0])==type([1,2]) and type(args[1])==type([1,2]) and args[2]=="value" and args[0]==args[1] or args[2]=="len" and type(args[0])==type([1,2]) and type(args[1])==type(4) and len(args[0])==args[1] else print("False")
        if type(args[1])==type(2) and type(args[2])==type("str") or type(args[2])==type("str") and type(args[1])==type([1,2]): raise TypeError("La combinacion de los argumentos 2 y 3 son invalidos")
        if args[2]!="len" and args[2]!="value": raise ValueError("El tercer argumento solo admite 2 entradas (len ó value) y usted ingreso: {}".format(args[2]))
    if len(args)==2 or len(args)>3 or len(args)==0: print("La funcion valList solo acepta 1 o 3 argumentos")
    return args
