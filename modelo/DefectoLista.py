class DefectoLista():

    __contador = None
    __nombre   = None
    __color    = None

    def __init__(self,contador,nombre,color):
        self.__contador = contador
        self.__nombre = nombre
        self.__color = color

   
    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador = contador

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color