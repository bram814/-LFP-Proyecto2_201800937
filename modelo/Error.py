class Error():

    __contador = None
    __fila = None
    __columna = None
    __caracter = None
    __descripcion = None
    
    def __init__(self,contador,fila,columna,caracter,descripcion):
        self.__contador = contador
        self.__fila = fila
        self.__columna = columna
        self.__caracter = caracter
        self.__descripcion = descripcion
    
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

    def getCaracter(self):
        return self.__caracter
    def setCaracter(self,caracter):
        self.__caracter = caracter
    
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self,descripcion):
        self.__descripcion = descripcion

    
