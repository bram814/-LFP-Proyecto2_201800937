class MatrizElemento():

    __contador  = None
    __columna = None
    __fila = None
    __etiqueta = None
    __color = None

    def __init__(self,contador,fila,columna,etiqueta,color):
        self.__contador = contador
        self.__columna = columna
        self.__fila = fila
        self.__etiqueta = etiqueta
        self.__color = color
     
    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador = contador

    def getFila(self):
        return self.__fila
    def setFila(self,fila):
        self.__fila = fila

    def getColumna(self):
        return self.__columna
    def setColumna(self,columna):
        self.__columna = columna

    def getEtiqueta(self):
        return self.__etiqueta
    def setEtiqueta(self,etiqueta):
        self.__etiqueta = etiqueta
    
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color

    def __str__(self):
        return f'Contador: {self.__contador}, Fila: {self.__fila}, Columna: {self.__columna}, nombre: {self.__etiqueta}, Color: {self.__color}'