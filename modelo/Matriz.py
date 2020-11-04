class Matriz():
    
    __contador = None
    __fila = None
    __columna = None
    __nombre = None
    __forma = None
    __boolean = None

    def __init__(self,contador,fila,columna,nombre,forma,boolean):
        self.__contador = contador
        self.__fila = fila
        self.__columna = columna
        self.__nombre = nombre
        self.__forma = forma
        self.__boolean = boolean
    
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

    def __str__(self):
        return f'Contador: {self.__contador}, Fila: {self.__fila}, Columna: {self.__columna}, nombre: {self.__nombre}, forma: {self.__forma}, boolean: {self.__boolean}'