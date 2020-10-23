from modelo.Error import Error
from modelo.Token import Token

from vista.Reporte import Reporte

class Anazalizador_A():

    def __init__(self):
        self.reporte_error = Reporte()
        self.entrada = ''
        self.caracter_actual = ''
        self.lexema_global = ''
        self.contador_error = 1
        self.contador_token = 1
        self.tokens = ['lista','matriz','tabla','nodo','nodos']
        self.signos = {
            "PUNTOCOMA"     : ';',
            "LLAVEAPERTURA" : '{',
            "LLAVECIERRE"   : '}',
            "IGUAL"         : '=', 
            "PARENTECISA"   : '(',
            "PARENTESISC"   : ')', 
            "COMILLAS"      : "'", 
            "COMILLAD"      : "\"", 
            "ASTERISCO"     : "*", 
            "SLASH"         : "/", 
            "SUMA"          : '+', 
            "NEGATIVO"      : '-', 
            "DIVICION2"     : '%', 
            "MAYORQ"        : '>', 
            "MENORQ"        : '<',
            "PUNTO"         : '.', 
            "COMA"          : ',', 
            "CONJUNCION"    : '&', 
            "DISYUNCION"    : '|', 
            "NEGACION"      : '!',
            "CORCHETEA"     : '[', 
            "CORCHETEC"     : ']', 
            "GUIONBAJO"     : '_', 
            "DOSPUNTOS"     : ':',
            "TABULACION"    : '\t',
            "SALTODELINEA"  : '\n'
            }


    def __inicio__(self,texto,lista_error,lista_token):
        for linea in texto:
            self.entrada += linea
        t = 0   # Guarda la primera posicion del token
        x = 0
        while x < len(self.entrada):
            #   INICIO DE LISTA
            
            if(self.entrada[x].isalpha()):
                if (self.entrada[x]=='l'):
                    print(f'lista       Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                    t = x
                    x += 1
                    if(self.entrada[x]=='i'):
                        x += 1
                        if(self.entrada[x]=='s'):
                            x += 1
                            if(self.entrada[x]=='t'):
                                x += 1
                                if (self.entrada[x]=='a'):
                                    x += 1
                                    self.guardar_lista_token(lista_token,self.get_fila(t),self.get_columna(t),'lista','TK_lista')

                                    if(self.entrada[self.parentesis_abierto(x)]==self.signos['PARENTECISA']):
                                        self.guardar_lista_token(lista_token,self.get_fila(self.parentesis_abierto(x)),self.get_columna(self.parentesis_abierto(x)),'(','TK_parentesis_abierto')
                                        x = self.parentesis_abierto(x)
                                        x += 1 # Tiene la posicion de la comilla simple '
                                        if (self.entrada[self.comilla_(x)]==self.signos['COMILLAS']):
                                            self.guardar_lista_token(lista_token,self.get_fila(self.comilla_(x)),self.get_columna(self.comilla_(x)),"'",'TK_comilla')
                                            x = self.comilla_(x)
                                            x += 1
                                            
                                            if(self.entrada[self.get_size_nombre_lista(x)]==self.signos['COMILLAS']):
                                                self.guardar_lista_token(lista_token,self.get_fila(x),self.get_columna(x),self.lexema_global,'TK_nombre_lista')
                                                print(self.lexema_global)
                                                print(self.entrada[x+1])
                                                print(self.lexema_global)
                                            else:
                                                print(f'encontro error {self.entrada[self.get_size_nombre_lista(x)]}')
                                                self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Sintaxis Error, uso incorrecto de la comilla. ')
                                                break
                                        else:
                                            self.guardar_lista_error(lista_error,self.get_fila(self.comilla_(x)),self.get_columna(self.comilla_(x)),self.entrada[self.comilla_(x)],"Debe de ir una comilla *'*")
                                            break
                                    else:
                                        self.guardar_lista_error(lista_error,self.get_fila(self.parentesis_abierto(x)),self.get_columna(self.parentesis_abierto(x)),self.entrada[self.parentesis_abierto(x)],'Debe de ir un Parentesis Abierto *(*')
                                        break
                                else:
                                    self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Debe de ingresar la letra *a*')
                                    break
                            else:
                                self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Debe de ingresar la letra *t*')
                                break
                        else:
                            self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Debe de ingresar la letra *s*')
                            break
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Debe de ingresar la letra *i*') 
                        break

                        # INICIO DE MATRIZ
                elif (self.entrada[x]=='m'):
                    print(f'matriz      Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                        # INICIO DE TABLA
                elif (self.entrada[x]=='t'):
                    print(f'tabla       Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                    
                        #REPORTE DEL ERROR
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Se espera *lista, matriz, tabla*')
                    break
            x += 1
            
        self.reporte_error.html_error(lista_error)
        self.reporte_error.reporte_html(lista_token)


     # obtiene TK_LISTA
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

        # Este metodo obtiene TL_PARENTESIS_ABIERTO ( 
    def parentesis_abierto(self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c==self.signos['PARENTECISA']):
                return actual
            elif (self.entrada[actual].isnumeric()):
                return actual
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
            actual += 1
        return actual

        # Este metodo otiene TK_COMILLA '
    def comilla_ (self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c == self.signos['COMILLAS']):
                return actual
            else:
                if (c == ' ' or c==self.signos['TABULACION'] or c==self.signos['SALTODELINEA']):
                    print('')
                else:
                    return actual

            actual += 1
        return actual

        # obtiene la cantidad del TITULO TK_nombre_lista
    def get_size_nombre_lista(self,actual):
        #self.lexema_global = ''
        while actual < len(self.entrada):
            #print(self.entrada[actual])
            c = self.entrada[actual]
            if (c==')' or c =="'" or c=="," or c=="(" or c=="{" or c=="}" or c==";"):
                return actual
            else:
                self.lexema_global += c
            actual += 1
        return actual

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
                if(c==self.signos['TABULACION']):
                    columna = columna + 2 
                else:
                    columna += 1
            x += 1
        return columna

    def guardar_lista_error(self,lista_error,fila,columna,caracter,descripcion):
        almacenado = Error(self.contador_error,fila,columna,caracter,descripcion)
        lista_error.append(almacenado)
        self.contador_error += 1

    def guardar_lista_token(self,lista_token,fila,columna,lexema,token):
        almacenado = Token(self.contador_token,fila,columna,lexema,token)
        lista_token.append(almacenado)
        self.contador_token += 1

    