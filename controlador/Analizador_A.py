from modelo.Error import Error
from modelo.Token import Token

from vista.Reporte import Reporte

class Anazalizador_A():

    def __init__(self):
        self.reporte_error = Reporte()
        self.entrada = ''
        self.caracter_actual = ''
        self.lexema_global = ''
        self.tem = ''
        self.contador_error = 1
        self.contador_token = 1
        self.tokens = ['lista','matriz','tabla','nodo','nodos']
        self.lista_doble = ['verdadero','falso']
        self.lista_color = [
            'azul'         ,'azul2'        ,'azul3',
            'rojo'         ,'rojo2'        ,'rojo3',
            'amarillo'     ,'amarillo2'    ,'amarillo3',
            'anaranjado'   ,'anaranjado2'  ,'anaranjado3',
            'cafe'         ,'cafe2'        ,'cafe3',
            'gris'         ,'gris2'        ,'gris3',
            'morado'       ,'morado2'      ,'morado3',
            'verde'        ,'verde2'       ,'verde3',
            'blanco'
            
            ]
        self.signos = {
            "PUNTOCOMA"     : ';',
            "LLAVEA"        : '{',
            "LLAVEC"        : '}',
            "IGUAL"         : '=', 
            "PARENTESISA"   : '(',
            "PARENTESISC"   : ')', 
            "COMILLAS"      : "'",
            "DOBLECOMILLA"  : '"',
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
            "SALTODELINEA"  : '\n',
            "NUMERAL"       : '#'
            }

        self.formas = ['circulo','rectangulo','triangulo','punto','hexagono','diamante']


    def __inicio__(self,texto,lista_error,lista_token):
        for linea in texto:
            self.entrada += linea
        t = 0   # Guarda la primera posicion del token
        x = 0
        
        while x < len(self.entrada):
            #   INICIO DE LISTA
            
            if(self.entrada[x].isalpha()):
                if (self.entrada[x].lower()=='l'):
                    print(f'lista       Fila: {self.get_fila(x)} Columna:{self.get_columna(x)}')
                    t = x
                    x += 1
                    if(self.entrada[x].lower()=='i'):
                        x += 1
                        if(self.entrada[x].lower()=='s'):
                            x += 1
                            if(self.entrada[x].lower()=='t'):
                                x += 1
                                if (self.entrada[x].lower()=='a'):
                                    x += 1
                                    self.guardar_lista_token(lista_token,self.get_fila(t),self.get_columna(t),'lista','TK_lista')

                                    if(self.entrada[self.parentesis_abierto(x)]==self.signos['PARENTESISA']):
                                        self.guardar_lista_token(lista_token,self.get_fila(self.parentesis_abierto(x)),self.get_columna(self.parentesis_abierto(x)),'(','TK_parentesis_abierto')
                                        x = self.parentesis_abierto(x)
                                        x += 1 # Tiene la posicion de la comilla simple '
                                        if (self.entrada[self.comilla_(x)]==self.signos['COMILLAS'] or self.entrada[self.comilla_(x)]==self.signos['DOBLECOMILLA']):
                                            self.tem = self.entrada[self.comilla_(x)]
                                            x = self.comilla_(x)
                                            x += 1
                                            size = self.get_size_nombre_lista(x)
                                            if(self.entrada[size]==self.tem):
                                                nombre_lista = self.lexema_global.lower()
                                                self.guardar_lista_token(lista_token,self.get_fila(x),self.get_columna(x),self.tem+self.lexema_global+self.tem,'TK_nombre_lista')
                                                x = size
                                                x += 1
                                                size = self.get_coma(x)
                                                if(self.entrada[self.get_coma(x)]==self.signos['COMA']):
                                                    x = self.get_coma(x)
                                                    self.guardar_lista_token(lista_token,self.get_fila(x),self.get_columna(x),",",'TK_coma')
                                                    x += 1
                                                    self.lexema_global = ''
                                                    size = self.get_forma(x)
                                                    if (self.lexema_global.lower() in self.formas):
                                                        forma_lista = self.lexema_global.lower()
                                                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(x),self.lexema_global.lower(),'TK_forma')
                                                        x = size
                                                        size = self.get_coma(x)
                                                        if (self.entrada[size]==self.signos['COMA']):
                                                            self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),",",'TK_coma')
                                                            x = size
                                                            x += 1
                                                            self.lexema_global = ''
                                                            size = self.get_forma(x)
                                                            if (self.lexema_global.lower() in self.lista_doble):
                                                                enlazada_lista = self.lexema_global.lower()
                                                                self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(x),self.lexema_global.lower(),'TK_lista_doble')
                                                                x = size
                                                                size = self.parentesis_cerrado(x)
                                                                if (self.entrada[size]==self.signos['PARENTESISC']):
                                                                    x = size
                                                                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),")",'TK_parentesis_cerrado')
                                                                    x += 1
                                                                    size = self.llave_abierta(x)
                                                                    if (self.entrada[size]==self.signos['LLAVEA']):
                                                                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),"{",'TK_llave_abierta')
                                                                        x = size
                                                                        x += 1
                                                                        self.tem = ''
                                                                        self.lexema_global = ''
                                                                        size = self.valores_lista(x,lista_error,lista_token)
                                                                        x = size
                                                                        if( self.entrada[x]==self.signos['LLAVEC']):
                                                                            self.guardar_lista_token(lista_token,self.get_fila(x),self.get_columna(x),"}",'TK_llave_cerrada')
                                                                            x += 1
                                                                            size  = self.defecto(x)

                                                                            if (self.lexema_global.lower() == 'defecto'):
                                                                                x = size
                                                                                size = self.defecto_nodo(x,lista_error,lista_token)
                                                                                
                                                                                if (self.entrada[size]==self.signos['PUNTOCOMA']):
                                                                                    x = size
                                                                                else:
                                                                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir punto y coma')
                                                                                    break



                                                                        else:
                                                                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir una llave de apertura {')
                                                                            break 
                                                                    else:
                                                                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir una llave de apertura {')
                                                                        break 
                                                                else:
                                                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Falta el parentesis )')
                                                                    break 
                                                            

                                                            else:
                                                                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[x],'Debe ser Verdadero o Falso ')
                                                                break 
                                                            
                                                        else:
                                                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'No encontro una coma. ')
                                                            break 

                                                    else:
                                                        self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),'<forma>','No se encontro esta forma. ')
                                                        break
                                                else:
                                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Se Espera una coma , . ')
                                                    break
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
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),self.entrada[x],'Se espera *lista, matriz, tabla*')
                    break
            else:
                        # COMENTARIO AL INCICIO
                if (self.entrada[x]==self.signos['SLASH']):
                    size = self.comentario_slash(x)
                    if (self.entrada[size]==self.signos['SALTODELINEA']):
                        print('entro al salto de linea')
                        x = size
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(x),self.get_columna(x),'//','Falta un slash.')
                        break
                

                        
            x += 1
            
        self.reporte_error.html_error(lista_error)
        self.reporte_error.reporte_html(lista_token)

    # METODO DE COMENTARIO

    def comentario_slash(self,actual):
        boolean = False
        while actual < len(self.entrada):
            c = self.entrada[actual]
            p = self.entrada[actual+1]
            if (c == self.signos['SLASH'] and p == self.signos['SLASH']):
                boolean = True
                actual += 2
                break
            else:
                return actual
            actual += 1
        if (boolean == True):
            while actual < len(self.entrada):
                c = self.entrada[actual]
                if(c == self.signos['SALTODELINEA']):
                    return actual
                actual += 1
        return actual
    
    #def comentario_slah(self,actual):
        #boolean = False
      #  pass
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

        # Este metodo obtiene                           Tk_PARENTESIS_ABIERTO ( 
    def parentesis_abierto(self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c==self.signos['PARENTESISA']):
                return actual
            elif (self.entrada[actual].isnumeric()):
                return actual
            elif (self.entrada[actual]==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
            actual += 1
        return actual

        # Este metodo otiene                            TK_COMILLA '
    def comilla_ (self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c == self.signos['COMILLAS'] or c == self.signos['DOBLECOMILLA']):
                return actual
            else:
                if (c == ' ' or c==self.signos['TABULACION'] or c==self.signos['SALTODELINEA']):
                    pass
                elif (self.entrada[actual]==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
                else:
                    return actual

            actual += 1
        return actual

        # obtiene la cantidad del TITULO                TK_nombre_lista
    def get_size_nombre_lista(self,actual):
        self.lexema_global = ''
        while actual < len(self.entrada):
            #print(self.entrada[actual])
            c = self.entrada[actual]
            if (c == self.tem):
                return actual
            elif(c==self.signos['SALTODELINEA']):
                return actual
            else:
                self.lexema_global += c
            actual += 1
        return actual

        # Este metod obtiene                                TK_COMA ,
    def get_coma(self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (c==self.signos['COMA']):
                return actual
            else: 
                if (c == ' ' or c==self.signos['TABULACION'] or c==self.signos['SALTODELINEA']):
                    pass
                elif (self.entrada[actual]==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
                else:
                    return actual
            actual += 1
        return actual

        # ESTE METODO OBTIENE LA FORMA                     TK_Forma o TK_LISTA_DOBLE
    def get_forma(self,actual):
        estado = False
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (c.isalpha()): 
                estado = True
                self.lexema_global += c
                actual += 1
                break
            elif (self.entrada[actual]==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
            
            actual += 1 

        
        if(estado == True):
            while actual < len(self.entrada):
                c = self.entrada[actual]
                if (c.isalpha()):
                    self.lexema_global += c
                else:
                    if ( c == ' ' or c == self.signos['TABULACION'] or c== self.signos['SALTODELINEA'] or c == self.signos['COMA']):
                        return actual
                    else: 
                        return actual
                actual += 1

        return actual

        # Este metodo obtiene parentesis cerrado                        TK_PARENTESIS_CERRADO
    def parentesis_cerrado(self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c==self.signos['PARENTESISC']):
                return actual
            elif (self.entrada[actual].isnumeric()):
                return actual
            elif (self.entrada[actual]==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
            actual += 1
        return actual

        # Este metodo obtiene llave abierta                             TK_LLAVE_ABIERTA
    def llave_abierta(self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c==self.signos['LLAVEA']):
                return actual
            elif (self.entrada[actual].isnumeric()):
                return actual
            elif (self.entrada[actual]==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
            actual += 1
        return actual

           # Este metodo obtiene llave abierta                             TK_LLAVE_CERRADA
    def llave_cerrada(self,actual):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if(c==self.signos['LLAVEC']):
                return actual
            elif (self.entrada[actual].isnumeric()):
                return actual
            elif (self.entrada[actual]==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
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
        columna = 2
        x = 0
        while x < actual:
            c = self.entrada[x]
            if (c=='\n'):
                columna = 1
            elif ((x+1)==actual):
                return columna
          #  else:
                #if(c==self.signos['TABULACION']):
                 #   print(columna)
                  #  columna += 3 
                   # print(columna)
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

    # Este metodo obtiene la primera letra que encuentre, luego retorna la posicion hasta el punto y coma ;
    def valores_lista(self,actual,lista_error,lista_token):
        while actual < len(self.entrada):
            c = self.entrada[actual]
            self.lexema_global = ''
            if (c.isalpha()):
                self.lexema_global += self.entrada[actual]
                actual += 1 # esta en O de          n O do (nodo)
                size = self.elemento(actual,lista_error,lista_token)
                if (self.entrada[size]==self.signos['PUNTOCOMA']):
                    print(self.entrada[size])
                    actual = size
                    
                else:
                    return actual

            elif (c==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            elif (c==self.signos['LLAVEC']):
                return actual
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(actual),self.get_columna(actual),c,'Debe de ir la palabra reservada nodo/nodos') 
                    return actual
            actual += 1

        return actual

    def elemento(self,actual,lista_error,lista_token):

        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (c.isalpha()):
                self.lexema_global += c
            else:
                if (self.lexema_global.lower()=='nodos'):
                    self.guardar_lista_token(lista_token,self.get_fila(actual-5),self.get_columna(actual-6),"nodos",'TK_elemento_nodos')
                    self.lexema_global =''   
                    size = self.nodos(actual,lista_error,lista_token)  
                    actual = size
                    if (self.entrada[size]==self.signos['PUNTOCOMA']):
                        return actual
                    else:
                        return actual 
                                                   
                elif (self.lexema_global.lower()=='nodo'):
                    self.guardar_lista_token(lista_token,self.get_fila(actual-4),self.get_columna(actual-5),"nodo",'TK_elemento_nodo')
                    self.lexema_global =''   
                    size = self.nodo(actual,lista_error,lista_token)  
                    actual = size
                    if (self.entrada[size]==self.signos['PUNTOCOMA']):
                        return actual
                    else:
                        return actual
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(actual),self.get_columna(actual),c,'Debe de ir la palabra reservada nodo/nodos') 
                    return actual

            actual += 1
        return actual

    def nodo(self,actual,lista_error,lista_token):

        while actual < len(self.entrada):
            size = self.parentesis_abierto(actual)
            if (self.entrada[size]==self.signos['PARENTESISA']):
                self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),'(','TK_parentesis_abierto')
                actual = size
                actual += 1
                #self.tem = ''
                size = self.comilla_(actual)
                numeral = self.buscar_numeral(actual)
                if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA'] or self.entrada[numeral] == self.signos['NUMERAL']):
                    
                    if (self.entrada[numeral] == self.signos['NUMERAL']):
                        actual = numeral
                        nombre_nodo = self.entrada[actual]
                        self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),nombre_nodo,'TK_etiqueta_lista')     
                            
                        actual += 1
                        size = self.parentesis_cerrado(actual)
                        if (self.entrada[size]==self.signos['PARENTESISC']):
                            self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.entrada[actual],'TK_parentesis_cerrado')     
                            actual = size
                            actual += 1
                            size = self.nodo_color(actual,lista_error,lista_token)
                            if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                                actual = size  
                                return actual
                            else:
                                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar un punto y coma') 
                                return actual
                        else:
                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de parentesis de cierre') 
                            return actual
                        
                    else:
                        self.tem = self.entrada[size]
                        actual = size
                        actual += 1
                        size = self.get_size_nombre_lista(actual)
                        if(self.entrada[size]==self.tem):
                            
                            self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem + self.lexema_global + self.tem,'TK_etiqueta_lista')     
                            actual = size
                            actual += 1
                            size = self.parentesis_cerrado(actual)
                            if (self.entrada[size]==self.signos['PARENTESISC']):
                                self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.entrada[actual],'TK_parentesis_cerrado')     
                                actual = size
                                actual += 1
                                size = self.nodo_color(actual,lista_error,lista_token)
                                if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                                    actual = size  
                                    return actual
                                else:
                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar un punto y coma') 
                                    return actual
                            else:
                                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de parentesis de cierre') 
                                return actual

                        else:
                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de etiqueta') 
                            return actual
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de etiqueta') 
                    return actual

            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un (') 
                return actual
            actual += 1
        return actual
    
    def nodo_color(self,actual,lista_error,lista_token):
        estado = 0
        caracter = ''
        lexema = ''
        contador = 0
        while actual < len(self.entrada):
            caracter = self.entrada[actual]
            if (caracter.isalpha()):
                estado = 1
                actual += 1
                contador = actual
                lexema += caracter
                break
            elif (caracter == self.signos['NUMERAL']):
                contador = actual
                break
            elif (caracter==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (caracter==' '  or caracter==self.signos['TABULACION'] or caracter == self.signos['SALTODELINEA']):
                        pass
                else:
                    break


            actual += 1

        if (estado != 0):
            while actual < len(self.entrada):
                caracter = self.entrada[actual]
                if (estado==1 and caracter.isalpha()):
                    lexema += caracter
                else:
                    if(caracter.isnumeric()):
                        lexema += str(caracter)
                        actual+=1
                        break
                    break
                actual += 1

        if (lexema.lower() in self.lista_color):
            self.guardar_lista_token(lista_token,self.get_fila(contador),self.get_columna(contador),lexema,'TK_color_elemento')     
            while actual < len(self.entrada):
                c = self.entrada[actual]

                if (self.entrada[actual]==self.signos['PUNTOCOMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.signos['PUNTOCOMA'],'TK_punto_coma')     
                    return actual
                elif (c==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
                else:
                    if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                        pass
                    else:
                        return actual
                actual += 1
        elif (self.entrada[actual]==self.signos['NUMERAL']):
            self.guardar_lista_token(lista_token,self.get_fila(contador),self.get_columna(contador),'#','TK_color_elemento')     
            actual += 1
            while actual < len(self.entrada):
                c = self.entrada[actual]

                if (self.entrada[actual]==self.signos['PUNTOCOMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.signos['PUNTOCOMA'],'TK_punto_coma')     
                    return actual
                elif (c==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
                else:
                    if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                        pass
                    else:
                        return actual
                actual += 1

        else:
            self.guardar_lista_error(lista_error,self.get_fila(actual),self.get_columna(actual),self.entrada[actual],'El color esta incorrecto') 
            return actual
        return actual

    def nodos(self,actual,lista_error,lista_token):
        while actual < len(self.entrada):
            size = self.parentesis_abierto(actual)
            if (self.entrada[size]==self.signos['PARENTESISA']):
                self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),'(','TK_parentesis_abierto')
                actual = size
                actual += 1

                size = self.get_size_elemento(actual) # retornar el valor despues del numero
                if (0 < int(self.numero_elemento)):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.numero_elemento,'TK_contador_elemento')
                    actual = size
                    size = self.get_coma(actual)

                    if (self.entrada[size]==self.signos['COMA']):
                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma')
                        actual = size
                        actual += 1
                        
                        size = self.comilla_(actual)
                        numeral = self.buscar_numeral(actual)
                        
                        if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA'] or self.entrada[numeral] == self.signos['NUMERAL']):
                           
                            if (self.entrada[numeral] == self.signos['NUMERAL']):
                                actual = numeral
                                nombre_nodo = self.entrada[actual]

                                self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),nombre_nodo,'TK_etiqueta_lista')     
                                    
                                actual += 1
                                size = self.parentesis_cerrado(actual)
                               
                                if (self.entrada[size]==self.signos['PARENTESISC']):
                                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.entrada[actual],'TK_parentesis_cerrado')     
                                    actual = size
                                    actual += 1
                                    size = self.nodo_color(actual,lista_error,lista_token)
                                    if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                                        actual = size  
                                        return actual
                                    else:
                                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar un punto y coma') 
                                        return actual
                                else:
                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de parentesis de cierre') 
                                    return actual
                                
                            else:
                                self.tem = self.entrada[size]
                               
                                actual = size
                                actual += 1
                                size = self.get_size_nombre_lista(actual)
                                if(self.entrada[size]==self.tem):
                                    
                                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem + self.lexema_global + self.tem,'TK_etiqueta_lista')     
                                    actual = size
                                    actual += 1
                                    size = self.parentesis_cerrado(actual)
                                    if (self.entrada[size]==self.signos['PARENTESISC']):
                                        
                                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.entrada[actual],'TK_parentesis_cerrado')     
                                        actual = size
                                        actual += 1
                                        size = self.nodo_color(actual,lista_error,lista_token)
                                        if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                                            actual = size  
                                            return actual
                                        else:
                                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar un punto y coma') 
                                            return actual
                                    else:
                                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de parentesis de cierre') 
                                        return actual

                                else:
                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de etiqueta') 
                                    return actual
                        else:
                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de etiqueta') 
                            return actual

                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir una coma.') 
                        return actual

                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.numero_elemento,'No es un numero entero positivo') 
                    return actual

            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un (') 
                return actual
            actual += 1
        return actual

    def get_size_elemento(self,actual):
        self.numero_elemento = ''
        estado = 0
        while actual < len(self.entrada):
            caracter = self.entrada[actual]
            if (self.entrada[actual].isnumeric()):
                self.numero_elemento += self.entrada[actual]
                actual += 1
                estado = 1
                break
            elif (caracter==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (caracter==' ' or caracter==self.signos['TABULACION'] or caracter == self.signos['SALTODELINEA']):
                        pass
                else:
                    break

        if(estado== 1):
            while actual < len(self.entrada):
                if (self.entrada[actual].isnumeric()):
                    self.numero_elemento += self.entrada[actual]
                else:
                    break
                actual += 1
        return actual
    

    def buscar_numeral(self,actual):

        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (c==self.signos['NUMERAL']):
                return actual
            elif (c==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
            actual += 1 

        return actual


    def defecto(self,actual):
        self.lexema_global = ''
        boolean = False
        while actual < len(self.entrada):

            caracter = self.entrada[actual]

            if (caracter.isalpha()):
                self.lexema_global += caracter
                actual += 1
                boolean = True
                break
            elif (caracter==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (caracter==' '  or caracter==self.signos['TABULACION'] or caracter== self.signos['SALTODELINEA']):
                    pass
                else:
                    return actual
            actual += 1

        if (boolean == True):

            while actual < len(self.entrada):
                caracter = self.entrada[actual]
                if (caracter.isalpha()):
                    self.lexema_global += caracter
                else:
                    return actual
                actual += 1
        
        return actual


    def defecto_nodo(self,actual,lista_error,lista_token):
        while actual < len(self.entrada):
            size = self.parentesis_abierto(actual)
            if (self.entrada[size]==self.signos['PARENTESISA']):
                self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),'(','TK_parentesis_abierto')
                actual = size
                actual += 1
                #self.tem = ''
                size = self.comilla_(actual)
                if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA']):
                    
                    self.tem = self.entrada[size]
                    actual = size
                    actual += 1
                    size = self.get_size_nombre_lista(actual)
                    if(self.entrada[size]==self.tem):
                            
                        self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem + self.lexema_global + self.tem,'TK_etiqueta_lista')     
                        actual = size
                        actual += 1
                        size = self.parentesis_cerrado(actual)
                        if (self.entrada[size]==self.signos['PARENTESISC']):
                            self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.entrada[actual],'TK_parentesis_cerrado')     
                            actual = size
                            actual += 1
                            size = self.defecto_color(actual,lista_error,lista_token)
                            if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                                actual = size  
                                return actual
                            else:
                                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar un punto y coma') 
                                return actual
                        else:
                            self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de parentesis de cierre') 
                            return actual

                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de etiqueta') 
                        return actual
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Uso incorrecto de etiqueta') 
                    return actual

            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un (') 
                return actual
            actual += 1
        return actual
    

    def defecto_color(self,actual,lista_error,lista_token):
        estado = 0
        caracter = ''
        lexema = ''
        contador = 0
        while actual < len(self.entrada):
            caracter = self.entrada[actual]
            if (caracter.isalpha()):
                estado = 1
                actual += 1
                contador = actual
                lexema += caracter
                break
            elif (caracter==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (caracter==' '  or caracter==self.signos['TABULACION'] or caracter == self.signos['SALTODELINEA']):
                        pass
                else:
                    break


            actual += 1

        if (estado != 0):
            while actual < len(self.entrada):
                caracter = self.entrada[actual]
                if (estado==1 and caracter.isalpha()):
                    lexema += caracter
                else:
                    if(caracter.isnumeric()):
                        lexema += str(caracter)
                        actual+=1
                        break
                    break
                actual += 1

        if (lexema.lower() in self.lista_color):
            self.guardar_lista_token(lista_token,self.get_fila(contador),self.get_columna(contador),lexema,'TK_color_elemento')     
            while actual < len(self.entrada):
                c = self.entrada[actual]

                if (self.entrada[actual]==self.signos['PUNTOCOMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.signos['PUNTOCOMA'],'TK_punto_coma')     
                    return actual
                elif (c==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
                else:
                    if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                        pass
                    else:
                        return actual
                actual += 1
        else:
            self.guardar_lista_error(lista_error,self.get_fila(actual),self.get_columna(actual),self.entrada[actual],'El color esta incorrecto') 
            return actual
        return actual