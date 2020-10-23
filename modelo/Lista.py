class Lista():

    __contador = None
    __nombre    = None
    __forma     = None
    __boolean   = None

    def __init__(self,contador,nombre,forma,boolean):
        self.__contador = contador
        self.__nombre = nombre
        self.__forma = forma
        self.__boolean = boolean

    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador = contador
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getForma(self):
        return self.__forma
    def setForma(self,forma):
        self.__forma = forma
    
    def getBoolean(self):
        return self.__boolean
    def setBoolean(self,boolean):
        self.__boolean = boolean