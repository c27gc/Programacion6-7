class Evaluacion:
    def __init__(self,tipo="examen",fecha="01/01/19",pond=0.33):
        self.setTipo(tipo)
        self.setFecha(fecha)
        self.setPond(pond)
        self.__nota=0

    def setTipo(self,val):
        self.__tipo=val
    def setFecha(self,val):
        self.__fecha=val
    def setPond(self,val):
        self.__pond=val
    def setNota(self,val):
        self.__nota=val

    def getTipo(self):
        return self.__tipo
    def getFecha(self):
        return self.__fecha
    def getPond(self):
        return self.__pond
    def getNota(self):
        return self.__nota

class Alumno:
    def __init__(self,nombre="Alumno alum", cedula="20111222",evaluaciones=[], aprob=False):
        self.setNombre(nombre)
        self.setCedula(cedula)
        self.setEvaluaciones(evaluaciones)
        self.setAprob(aprob)

    def setNombre(self,val):
        self.__nombre=val
    def setCedula(self,val):
        self.__cedula=val
    def setEvaluaciones(self,val):
        self.__evaluaciones=val
    def setAprob(self,val):
        self.__aprob=val

    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getEvaluaciones(self):
        return self.__evaluaciones
    def getAprob(self):
        return self.__aprob

    def isApr(self,nma):
        acu=0
        for i in self.__evaluaciones:
            acu += i.getNota()*i.getPond()
        if acu>nma:
            self.setAprob(True)

class ResumenDeNotas:
    def __init__(self,n_alumnos=1, n_evaluaciones=1):
        self.setNalumnos(n_alumnos)
        self.setNevaluaciones(n_evaluaciones)

    def setNalumnos(self,val):
        self.__n_alumnos=val
    def setNevaluaciones(self,val):
        self.__n_evaluaciones=val

    def ingresoManual(self):
        self.__nma=float(input("Ingrese nota minima aprobatoria: "))
        print("A continuación debe definir el Tipo, la Fecha y la Ponderación de cada evaluación: ")
        evaluaciones=[]
        for n,i in enumerate(range(self.__n_evaluaciones)):
            tipo=input("Ingrese el tipo de la evaluación {}: ".format(n+1))
            fecha=input("Ingrese la fecha de la evaluacion {}: ".format(n+1))
            pond=float(input("Ingrese la ponderación de la evaluación {}: ".format(n+1)))
            evaluaciones.append(Evaluacion(tipo,fecha,pond))

        if sum([i.getPond() for i in evaluaciones]) != 1:
            raise ValueError("Las ponderaciones deben sumar 1")
        resumen_alumnos = []
        for n,i in enumerate(range(self.__n_alumnos)):
            nombre = input("Ingrese el nombre del alumno {}: ".format(n+1))
            cedula = input("Ingrese la cedula del alumno {}: ".format(nombre))
            evaluaciones_copy = copy.deepcopy(evaluaciones)
            for w,h in enumerate(evaluaciones_copy):
                nt = float(input("Ingrese la nota de la evaluación {} del alumno {}: ".format(w+1,nombre)))
                h.setNota(nt)
            resumen_alumnos.append(Alumno(nombre,cedula,evaluaciones_copy))
        self.__resumen_alumnos = resumen_alumnos

    def toFile(self,path):
        with open(path,'at') as file:
            for i in self.__resumen_alumnos:
                notas = ""
                for k,j in enumerate(i.getEvaluaciones()):
                    notas += "eval: {} nota: {}".format(k,j.getNota())
                str1 = i.getNombre() + " " + notas + str(i.isApr(self.__nma))
                file.writelines(str1)
