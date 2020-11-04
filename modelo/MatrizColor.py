class MatrizColor():

    __contador = None
    __fila = None
    __color = None

    def __init__(self,contador,fila,color):
        self.__contador = contador
        self.__fila = fila
        self.__color = color


    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador = contador

    def getFila(self):
        return self.__fila
    def setFila(self,fila):
        self.__fila = fila

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color

    def __str__(self):
        return f'Contador: {self.__contador}, Fila: {self.__fila}, Color: {self.__color}'