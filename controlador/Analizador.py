class analyzer():
    def __init__(self):
        self.row = 0
        self.column = 0
        self.arrayError = []
        self.arrayTokens = []
        self.arrayR = ['lista', 'matriz', 'tabla']

        self.signos = {"PUNTOCOMA":';', "LLAVEAPERTURA":'{', "LLAVECIERRE":'}', "IGUAL":'=', "PARENTECISA": '(',
                        "PARENTESISC": ')', "COMILLAS": "\'", "COMILLAD": "\"", "ASTERISCO": "*", "SLASH": "/", "SUMA": '+',
                        "NEGATIVO": '-', "DIVICION2": '%', "MAYORQ": '>', "MENORQ": '<', "PUNTO": '.', "COMA": ',',
                        "CONJUNCION":'&', "DISYUNCION": '|', "NEGACION": '!', "CORCHETEA": '[', "CORCHETEC": ']', "GUIONBAJO": '_',
                        "DOSPUNTOS": ':'}

    def analizar(self, content):
        self.row = 1
        self.column = 1
        self.counter = 0
        while self.counter < len(content):
            symbol = content[self.counter]
            if symbol == "\n":
                self.counter += 1
                self.row += 1
                self.column = 1 
            elif symbol =="\t":
                self.counter += 1
                self.column += 1 
            elif symbol ==" ":
                self.counter += 1
                self.column += 1
            elif (symbol.isalpha()):
                sizeLexema = self.getSizeLexema(self.counter, content)

            else:
                isSign = False
                tempSymbol = ""
                #---------- S0 -> s1
                for key in self.signos:
                    valor = self.signos[key]
                    
                #-------------------q0 -> q10
                if not isSign:
                   # self.arrayErrores.append([self.row, self.column, content[self.counter]])
                    self.column += 1
                    self.counter += 1

    def getSizeLexema(self, posInicio, content):
        longitud = 0
        for i in range(posInicio, len(content)):
            if (content[i].isalpha() or content[i] == "_" or content[i].isnumeric()):
                longitud+=1
            else:
                break
        return longitud

    def stateIdentificador(self, sizeLexema, content):
        size = self.counter + sizeLexema
        #self.addToken(self.row, self.column, 'Id', content[self.counter : size])
        self.counter = self.counter + sizeLexema
        self.column = self.column + sizeLexema
    
    #def addToken(self, row, column, content, word):
        #self.arrayTokens.append([row, column, content, word])