class ElementoLista():

    __contador      = None
    __etiqueta      = None
    __color         = None

    def __init__(self,contador,etiqueta,color):
        self.__contador = contador
        self.__etiqueta = etiqueta
        self.__color = color

    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador = contador

    def getEtiqueta(self):
        return self.__etiqueta
    def setEtiqueta(self,etiqueta):
        self.__etiqueta = etiqueta

    def getColor(self):
        return self.__color
    def setColo(self,color):
        self.__color = color