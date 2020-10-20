class Anazalizador_A():

    def __init__(self):
        self.entrada = ''
        self.caracter_actual = ''


    def __inicio__(self,texto):
        for linea in texto:
            self.entrada += linea
        
        
        x = 0
        while x < len(self.entrada):
            #   INICIO DE LISTA
            if(self.entrada[x].isalpha()):
                if (self.entrada[x]=='l'):
                    print(f'lista       Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                    x += 1
                    if(self.entrada[x]=='i'):
                        x += 1
                        if(self.entrada[x]=='s'):
                            x += 1
                            if(self.entrada[x]=='t'):
                                x += 1
                                if (self.entrada[x]=='a'):
                                    x += 1

                                else:
                                    print(f'Error: *{self.entrada[x]}*        Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                                    break
                            else:
                                print(f'Error: *{self.entrada[x]}*  Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                                break
                        else:
                            print(f'Error: *{self.entrada[x]}*  Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                            break
                    else:
                        print(f'Error: *{self.entrada[x]}*  Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                        break

                        # INICIO DE MATRIZ
                elif (self.entrada[x]=='m'):
                    print(f'matriz      Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                        # INICIO DE TABLA
                elif (self.entrada[x]=='t'):
                    print(f'tabla       Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                    
                        #REPORTE DEL ERROR
                else:
                    print(f'Error: *{self.entrada[x]}*  Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                    break
            x += 1

    def obtener_longitud(self):
        pass

    def obtener_lista(self,actual):
        valor = ''
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if   (c.isalpha()):
                valor += valor
            elif (c==' '):
                pass
            else:
                print(f'encontro error: {c}')


            actual += 1

    def get_fila(self,actual):
        x = 0
        longitud = 1
        while x < actual:
            c = self.entrada[x]
            if (c =='\n'):
                longitud += 1
            x += 1
        return longitud

    def get_columna(self,actual):
        columna = 1
        x = 0
        while x < actual:
            c = self.entrada[x]
            if(c=='\n'):
                columna == 1
            else:
                columna += 1
            x += 1
        return columna