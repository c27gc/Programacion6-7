class Tropas:
    def __init__(self, nombre="claf of clans", materiales=[], carne= "roja", record= 0):
        self.setNombre(nombre)
        self.setMateriales(materiales)
        self.setCarne(carne)
        self.setRecord(record)

    def getNombre(self):
        return self.__nombre
    def getMateriales(self):
        return self.__materiales
    def getCarne(self):
        return self.__carne
    def getRecord(self):
        return self.__record
    def setNombre(self,val):
        self.__nombre=val
    def setMateriales(self,val):
        self.__materiales=val
    def setCarne(self,val):
        self.__carne=val
    def setRecord(self,val):
        self.__record=val


class N_Tropas:
    def __init__(self, n_trop=1):
        self.setN_Trop(n_trop)

    def setN_Trop(self,val):
        self.__n_trop=val


    def ingresoManual(self):
        self.__nevel=int(input("Ingrese el mayor record para ganar: "))
        print("A continuacion ingrese los el Nombre, Materiales, Carnes y Record de cada tropa:")
        for n,i in enumerate(range(self.__n_trop)):
            Trop=[]
            nombre=input("Ingrese el nombre de la tropa {}: ".format(n+1))
            materiales=input("Ingrese los materiales de la tropa {}: ".format(n+1))
            carne=input("Ingrese la carne de la tropa {}: ".format(n+1))
            record=input("Ingrese el record de la tropa {}: ".format(n+1))
            Trop.append(Tropas(nombre, materiales, carne, record))
            #return Trop

        #if record>self.__nevel:
            #return True




#Tropas_1=Tropas("Garden of", [1,3,2], "roja", "25")
#print(Tropas_1.getNombre())
#print(Tropas_1.getMateriales())
#print(Tropas_1.getCarne())
#print(Tropas_1.getRecord())
