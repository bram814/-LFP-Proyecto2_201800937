from modelo.Error import Error
from modelo.Token import Token
from modelo.Lista import Lista
from modelo.Matriz import Matriz

from modelo.MatrizElemento import MatrizElemento
from modelo.MatrizColor import MatrizColor
from modelo.ElementoLista import ElementoLista
from modelo.DefectoLista import DefectoLista

from vista.Reporte import Reporte

class Anazalizador_A():

    def __init__(self):
        self.prueba = 'mensaje prueba'

        # MATRIZ
        self.contador_matriz = 1
        self.matriz = []
        self.elemento_matriz = []
        self.elemento_matriz2 = []
        self.color_matriz = []

        self.tem_fila = ''
        self.tem_columna = ''
        self.tem_nombre = ''
        self.estado_matriz = False
        self.fila_columna_matriz = ''
        self.estado = 0
        self.recursivo_fila = 1
        self.recursivo_columna = 1
        self.columna_matriz = 1
        self.fila_matriz = 1
        self.aceptado = False

        self.reporte_error = Reporte()

        # LISTA
        self.estado_lista = False
        self.lista = []
        self.elemento_lista = []

        self.defecto_lista = []
        

        self.nodo_uno = ''
        self.nodo_dos = ''
        self.nodo_tres = ''

        self.entrada = ''
        self.caracter_actual = ''
        self.lexema_global = ''
        self.tem = ''

        self.contador_lista = 1

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
                                                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),self.entrada[size],'TK_forma')
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
                                                                self.guardar_lista(nombre_lista,forma_lista,enlazada_lista)
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
                                                                                self.guardar_lista_token(lista_token,self.get_fila(x-7),self.get_columna(x-7),"defecto",'TK_defecto')
                                                                            
                                                                                size = self.defecto_nodo(x,lista_error,lista_token)
                                                                                
                                                                                if (self.entrada[size]==self.signos['PUNTOCOMA']):
                                                                                    x = size

                                                                                    self.guardar_defecto_lista(self.nodo_uno,self.nodo_dos)
                                                                                    self.contador_lista += 1
                                                                                    self.estado_lista = True
                                                                                else:
                                                                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir punto y coma')
                                                                                    break
                                                                            else:
                                                                                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir defecto')
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
                    tem = x
                    self.lexema_global += self.entrada[x]
                    x += 1
                    size = self.get_matriz(x)
                    if (self.lexema_global == 'matriz'):
                        self.guardar_lista_token(lista_token,self.get_fila(tem),self.get_columna(tem),"matriz",'TK_matriz')
                        print(f'Tk_matriz ; Lexema: {self.lexema_global}')
                        self.lexema_global =''
                        x = size
                        self.estado = 0
                        size = self.reconocimiento_matriz(x,lista_error,lista_token)
                        x = size
                        if (self.entrada[x]==self.signos['LLAVEC']):
                            self.guardar_lista_token(lista_token,self.get_fila(x),self.get_columna(x),"}",'TK_llave_cerradura')
                            x += 1
                            size  = self.defecto(x)
                            if (self.lexema_global.lower() == 'defecto'):

                                x = size
                                self.guardar_lista_token(lista_token,self.get_fila(x-6),self.get_columna(x-6),"defecto",'TK_defecto')
                            
                                size = self.defecto_nodo(x,lista_error,lista_token)
                                if (self.entrada[size]==self.signos['PUNTOCOMA']):
                                    x = size
                                    self.guardar_defecto_lista(self.nodo_uno,self.nodo_dos)
                                    
                                    self.estado_matriz = True
                                    
                                    j = 0
                                    while j < int(self.fila_matriz):
                                        if (int(self.recursivo_fila) <= int(self.fila_matriz)):
                                            i = 0
                                            self.recursivo_columna = 1
                                            while i < int(self.columna_matriz):
                                                if (int(self.recursivo_columna) <= int(self.columna_matriz)):
                                                    self.guardar_elemento_matriz(int(self.recursivo_fila),int(self.recursivo_columna),'Disponible','defecto')
                                                    self.recursivo_columna += 1
                                                i += 1
                                            self.recursivo_fila += 1

                                        j += 1
                                    
                                    self.contador_matriz += 1
                                else:
                                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir punto y coma')
                                    break
                            else:
                                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un defecto')
                                break

                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(tem),self.get_columna(tem),self.entrada[x],'Se espera *lista, matriz, tabla*')
                        break

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
        self.reporte_error.reporte_html2(lista_token)
        print('\n')
        
        
# 
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
    
    def get_matriz(self,actual):
        while actual < len(self.entrada):
            if (self.entrada[actual].isalpha()):
                self.lexema_global += self.entrada[actual]
            else:
                return actual
            actual += 1
        return actual
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
        self.temporal_global = 0
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (c.isalpha()): 
                estado = True
                self.lexema_global += c
                self.temporal_global = actual
                actual += 1
                break
            elif (self.entrada[actual]==self.signos['SLASH']):
                    size = self.comentario_slash(actual)
                    actual = size
            else:
                if ( c == ' ' or c == self.signos['TABULACION'] or c== self.signos['SALTODELINEA'] or c == self.signos['COMA']):
                    pass
                else:
                    return actual
            
            actual += 1 

        
        if(estado == True):
            while actual < len(self.entrada):
                c = self.entrada[actual]
                if (c.isalpha()):
                    self.lexema_global += c
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
        columna = 1
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
                    i = 0
                    suma = 1
                    while i < self.nodo_tres:
                        nombre = f'{self.nodo_uno} {suma}' 
                        self.guardar_elemento(nombre,self.nodo_dos)
                        suma += 1
                        i += 1

                    if (self.entrada[size]==self.signos['PUNTOCOMA']):
                        return actual
                    else:
                        return actual 
                                                   
                elif (self.lexema_global.lower()=='nodo'):
                    self.guardar_lista_token(lista_token,self.get_fila(actual-4),self.get_columna(actual-5),"nodo",'TK_elemento_nodo')
                    self.lexema_global =''   
                    size = self.nodo(actual,lista_error,lista_token)  
                    actual = size
                    self.guardar_elemento(self.nodo_uno,self.nodo_dos)
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
                        self.nodo_uno = nombre_nodo
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
                            
                            self.nodo_uno = self.lexema_global
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
            self.nodo_dos = lexema.lower()
            self.matriz_color(int(self.recursivo_fila),lexema.lower()) 
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
            self.nodo_dos = '#'
            self.matriz_color(int(self.recursivo_fila),'#') 
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
                    self.nodo_tres = int(self.numero_elemento)
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
                                self.nodo_uno = nombre_nodo
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
                                    self.nodo_uno = self.lexema_global
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
                        self.nodo_uno = self.lexema_global
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
            self.nodo_dos = lexema
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


    def guardar_lista(self,nombre,forma,boolean):
        almacenado = Lista(self.contador_lista,nombre,forma,boolean)
        self.lista.append(almacenado) 

    def guardar_elemento(self,etiqueta,color):
        almacenado = ElementoLista(self.contador_lista,etiqueta,color)
        self.elemento_lista.append(almacenado)

    def guardar_defecto_lista(self,nombre,color):
        almacenado = DefectoLista(self.contador_lista,nombre,color)
        self.defecto_lista.append(almacenado)

    def matriz_fila_columna(self,actual):
        self.temporal_global = 0
        self.fila_columna_matriz = ''
        self.lexema_global = ''

        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (self.entrada[actual].isnumeric()):
                self.fila_columna_matriz += self.entrada[actual]
                self.temporal_global = actual
                actual += 1
                break
            elif (self.entrada[actual]==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    self.lexema_global += self.entrada[actual]
                    return actual
            actual += 1

        while actual < len(self.entrada):

            if (self.entrada[actual].isnumeric()):
                self.fila_columna_matriz += self.entrada[actual]
            else:
                self.lexema_global += self.entrada[actual]
                return actual
            actual += 1
        return actual
    
    def reconocimiento_matriz(self,actual,lista_error,lista_token):
        
        while actual < len(self.entrada):
            if (self.estado == 0): # Obtiene Tk_parentesisi_abierto (
                print(f'Estado actual: {self.estado} - Aceptado 0%') 
                size = self.parentesis_abierto(actual)
                if (self.entrada[size]==self.signos['PARENTESISA']):
                    
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),'(','TK_parentesis_abierto')
                    actual = size
                    self.estado = 1
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Se espera un parentesis abierto (')
                    break
            elif (self.estado == 1): # obtiene Tk_fila_,matriz          f
                print(f'Estado actual: {self.estado} - Aceptado 10%') 
                size = self.matriz_fila_columna(actual)

                if (0 < int(self.fila_columna_matriz)):
                    self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.fila_columna_matriz,'TK_fila_matriz')
                    fila = self.fila_columna_matriz
                    actual = size
                    actual -= 1
                    self.estado = 2
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.lexema_global,'Error de Fila, debe ser un entero positivo*')
                    break
            
            elif (self.estado == 2):    # obtiene TK_coma               ,
                print(f'Estado actual: {self.estado} - Aceptado 20%')  
                size = self.get_coma(actual)
                actual = size

                if (self.entrada[actual]==self.signos['COMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    self.estado = 3
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma')
                    break
            
            elif (self.estado == 3): # obtiene TK_columna_matriz
                print(f'Estado actual: {self.estado} - Aceptado 30%')  
                size = self.matriz_fila_columna(actual)

                if (0 < int(self.fila_columna_matriz)):
                    columna = self.fila_columna_matriz
                    self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.fila_columna_matriz,'TK_columna_matriz')
                    actual = size
                    actual -= 1
                    self.estado = 4
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.lexema_global,'Error Columna, debe ser un entero positivo')
                    break
            elif (self.estado == 4): # obtiene Tk_coma
                print(f'Estado actual: {self.estado} - Aceptado 40%')  
                size = self.get_coma(actual)
                actual = size

                if (self.entrada[actual]==self.signos['COMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    self.estado = 5
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma*')
                    break
            elif (self.estado == 5): #Tk_nombre_matriz
                print(f'Estado actual: {self.estado} - Aceptado 50%') 
                size = self.comilla_(actual)
                if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA']):
                    self.tem = self.entrada[size]
                    actual = size
                    actual += 1
                    size = self.get_size_nombre_lista(actual)
                    if(self.entrada[size]==self.tem):
                        nombre_matriz = self.lexema_global
                        self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem+self.lexema_global+self.tem,'TK_nombre_matriz')
                        actual = size
                        self.estado = 6
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Debe de ingresar una Comilla '")
                        break
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Debe de ingresar una Comilla '")
                    break
            elif (self.estado == 6): # Tk_coma
                print(f'Estado actual: {self.estado} - Aceptado 60%')   
                size = self.get_coma(actual)
                actual = size

                if (self.entrada[actual]==self.signos['COMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    self.estado = 7
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma*')
                    break
            elif (self.estado == 7): # Tk_forma_matriz
                print(f'Estado actual: {self.estado} - Aceptado 70%')
                self.lexema_global = ''
                size = self.get_forma(actual) 
                if (self.lexema_global.lower() in self.formas):
                    forma = self.lexema_global.lower()
                    self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.lexema_global,'TK_forma_matriz')
                    self.lexema_global = ''
                    self.estado = 8
                    actual = size
                    actual -= 1
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'La forma de la matriz no es correcta.')
                    break
            elif (self.estado == 8): # Tk_coma
                print(f'Estado actual: {self.estado} - Aceptado 80%')   
                size = self.get_coma(actual)
                actual = size

                if (self.entrada[actual]==self.signos['COMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    self.estado = 9
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma*')
                    break
            elif (self.estado == 9): #Tk_Doble_enlazada
                print(f'Estado actual: {self.estado} - Aceptado 90%')
                self.lexema_global = ''
                size = self.get_forma(actual) 
                if (self.lexema_global.lower() == 'verdadero' or self.lexema_global.lower() == 'falso'):
                    boolean = self.lexema_global.lower() 
                    self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.lexema_global,'TK_doble_enlace_matriz')
                    self.lexema_global = ''
                    self.estado = 10
                    actual = size
                    actual -= 1
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe ser Verdadero o falso.')
                    break
            elif (self.estado == 10): # Tk_parentesis_cerrado
                print(f'Estado actual: {self.estado} - Aceptado 100')
                size = self.parentesis_cerrado(actual)
                if (self.entrada[size]==self.signos['PARENTESISC']):
                    
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),')','TK_parentesis_cerrado')
                    actual = size
                    self.estado = 11
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Se espera un parentesis cerrado  )')
                    break
            elif (self.estado == 11): # Tk_llave_abierta
                    size = self.llave_abierta(actual)
                    if (self.entrada[size]==self.signos['LLAVEA']):
                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),'{','TK_llave_abierta')
                        actual = size
                        self.estado = 12
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir una llave abierta {')
                        break
            elif (self.estado == 12):
                self.estado = 13
                self.fila_matriz = fila
                self.columna_matriz = columna
                size = self.elemento_matriz_(actual,lista_error,lista_token)
                actual = size
                self.guardar_matriz(fila,columna,nombre_matriz,forma,boolean)
                return actual # aqui retorna la llave de cerradura
            actual += 1

        return actual

    # Este metodo sirve para encontrar fila, nodo
    def elemento_matriz_(self,actual,lista_error,lista_token):
        self.lexema_global = ''
        self.temporal_global = 0


        '''if (self.aceptado == False):
            print('aceptado')
        else:
            print('no aceptado')'''
        
        while actual < len(self.entrada):
            c = self.entrada[actual]
            if (self.entrada[actual].isalpha()):
                self.lexema_global += self.entrada[actual]
                self.temporal_global = actual
                actual += 1
                break
            elif (self.entrada[actual]==self.signos['SLASH'] and self.entrada[actual+1]==self.signos['SLASH']):
                size = self.comentario_slash(actual)
                actual = size
            elif (self.entrada[actual]==self.signos['LLAVEC']):
                return actual
            else:
                if (c==' '  or c==self.signos['TABULACION'] or c == self.signos['SALTODELINEA']):
                    pass
                else:
                    self.lexema_global += self.entrada[actual]
                    return actual
            actual += 1
        
        while actual < len(self.entrada):
            if(self.entrada[actual].isalpha()):
                self.lexema_global += self.entrada[actual]
            else:
                break
            actual += 1

        


        if (self.lexema_global.lower() == 'fila'):
            if (int(self.recursivo_fila) <= int(self.fila_matriz)):
                print('fila aceptada')
            else:
                self.guardar_lista_error(lista_error,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.lexema_global,'Se Excedio la fila')
                return actual
            self.lexema_global = ''
            self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),'fila','TK_fila_elemento')
            size = self.parentesis_abierto(actual)
            actual = size
            if (self.entrada[actual]==self.signos['PARENTESISA']):
                self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),'(','TK_parentesis_abierto')
                actual += 1
                self.recursivo_columna = 1
                size = self.recursivo_fila_matriz(actual,lista_error,lista_token)
                actual = size
                if (self.entrada[actual]==self.signos['PARENTESISC']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),')','TK_parentesis_cerrado')
                    actual += 1
                    size = self.nodo_color(actual,lista_error,lista_token)
                    if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                        actual = size  
                        actual += 1
                        self.recursivo_fila += 1
                        self.recursivo_columna = 1
                        size = self.elemento_matriz_(actual,lista_error,lista_token)
                        return size
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un parentesis de apertura (')
                        return size
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un parentesis de apertura (')
                    return actual 
            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un parentesis de apertura (')
                return actual
                        
        elif (self.lexema_global.lower() == 'nodo'):
            self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),'nodo','TK_nodo_elemento')
            size = self.nodo_matriz(actual,lista_error,lista_token)
            actual = size
            
            if (self.entrada[actual]==self.signos['PARENTESISC']):
                #self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),')','TK_parentesis_cerrado')
                actual += 1
                size = self.nodo_color_matriz(actual,lista_error,lista_token)
                if (self.entrada[size]==self.signos['PUNTOCOMA']):   
                    actual = size  
                    actual += 1
                    
                    size = self.elemento_matriz_(actual,lista_error,lista_token)
                    return size
                else:
                    #self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un parentesis de apertura (')
                    return size
            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ir un parentesis de apertura (')
                return actual
        else:
            return actual
            
        return actual


    def recursivo_fila_matriz(self,actual,lista_error,lista_token):
        self.lexema_global = ''
        
        if (int(self.recursivo_columna) < int(self.columna_matriz)):
            size = self.comilla_(actual)
            size_numeral = self.buscar_numeral(actual)
            if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA']):
                self.tem = self.entrada[size]
                actual = size
                actual += 1
                size = self.get_size_nombre_lista(actual)
                if(self.entrada[size]==self.tem):
                    etiqueta_matriz = self.lexema_global

                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem+self.lexema_global+self.tem,'TK_nombre_matriz')
                    actual = size
                    actual += 1
                    size = self.get_coma(actual)
                    size2 = self.parentesis_cerrado(actual)    
                    self.guardar_elemento_matriz(int(self.recursivo_fila),int(self.recursivo_columna),etiqueta_matriz,'disponible')
                    if (self.entrada[size]==self.signos['COMA']):
                        actual = size
                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                        actual += 1
                        self.recursivo_columna += 1

                        size = self.recursivo_fila_matriz(actual,lista_error,lista_token)
                        return size

                    elif (self.entrada[size2]==self.signos['PARENTESISC']):
                        actual = size2
                        x = 0
                        while x < int(self.columna_matriz):

                            if (int(self.recursivo_columna) < int(self.columna_matriz)):
                                self.recursivo_columna += 1
                                self.guardar_elemento_matriz(int(self.recursivo_fila),int(self.recursivo_columna),'Disponible','defecto')
                                print(f'disponible {self.recursivo_columna}')
                            x += 1
                        
                        
                        return actual
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma*')
                        return size
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Debe de ingresar una Comilla '")
                    return size
            elif (self.entrada[size_numeral]==self.signos['NUMERAL']):
                actual = size_numeral
                self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),'#','TK_etiqueta_elemento')
                actual += 1
                size = self.get_coma(actual)
                size2 = self.parentesis_cerrado(actual)    
                self.guardar_elemento_matriz(int(self.recursivo_fila),int(self.recursivo_columna),'#','disponible')
                if (self.entrada[size]==self.signos['COMA']):
                    actual = size
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    actual += 1
                    self.recursivo_columna += 1

                    size = self.recursivo_fila_matriz(actual,lista_error,lista_token)
                    return size

                elif (self.entrada[size2]==self.signos['PARENTESISC']):
                    actual = size2
                    x = 0
                    while x < int(self.columna_matriz):

                        if (int(self.recursivo_columna) < int(self.columna_matriz)):
                            print(f'disponible {self.recursivo_columna}')
                            self.recursivo_columna += 1
                        x += 1
                    return actual
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma*')
                    return size    
                
            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Uso incorrecto de la comilla una Comilla '")
                return size
               
            

        elif (self.recursivo_columna == self.columna_matriz):
            size = self.comilla_(actual)
            if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA']):
                self.tem = self.entrada[size]
                actual = size
                actual += 1
                size = self.get_size_nombre_lista(actual)
                if(self.entrada[size]==self.tem):
                    etiqueta_matriz = self.lexema_global.lower()
                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem+self.lexema_global+self.tem,'TK_nombre_matriz')
                    actual = size
                    actual += 1

                    size = self.parentesis_cerrado(actual)
                    if (self.entrada[size]==self.signos['PARENTESISC']):
                        
                        self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),')','TK_parentesis_cerrado')
                        actual = size
                        self.recursivo_columna = 1
                        return actual
                        
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Se espera un parentesis cerrado  )')
                        return size
            else:
                self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Uso incorrecto de la comilla una Comilla '")
                return size
            
        return actual


    def nodo_matriz(self,actual,lista_error,lista_token):
        self.estado = 0
        while actual < len(self.entrada):
            if (self.estado == 0): # Obtiene Tk_parentesisi_abierto (
                 
                size = self.parentesis_abierto(actual)
                if (self.entrada[size]==self.signos['PARENTESISA']):
                    
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),'(','TK_parentesis_abierto')
                    actual = size
                    self.estado = 1
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Se espera un parentesis abierto (')
                    break
            elif (self.estado == 1): # obtiene Tk_fila_,matriz          f 
                size = self.matriz_fila_columna(actual)

                if (0 < int(self.fila_columna_matriz) and int(self.fila_columna_matriz)<=int(self.fila_matriz)):
                    self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.fila_columna_matriz,'TK_fila_matriz')
                    fila = self.fila_columna_matriz
                    self.tem_fila = fila
                    actual = size
                    actual -= 1
                    self.estado = 2
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.lexema_global,'Error de Fila, debe ser un entero positivo*')
                    break
            
            elif (self.estado == 2):    # obtiene TK_coma               ,
                size = self.get_coma(actual)
                actual = size

                if (self.entrada[actual]==self.signos['COMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    self.estado = 3
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma')
                    break
            
            elif (self.estado == 3): # obtiene TK_columna_matriz
                size = self.matriz_fila_columna(actual)

                if (0 < int(self.fila_columna_matriz) and int(self.fila_columna_matriz) <= int(self.columna_matriz)):
                    columna = self.fila_columna_matriz
                    self.tem_columna = columna
                    self.guardar_lista_token(lista_token,self.get_fila(self.temporal_global),self.get_columna(self.temporal_global),self.fila_columna_matriz,'TK_columna_matriz')
                    actual = size
                    actual -= 1
                    self.estado = 4
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.lexema_global,'Error Columna, debe ser un entero positivo')
                    break
            elif (self.estado == 4): # obtiene Tk_coma
                size = self.get_coma(actual)
                actual = size

                if (self.entrada[actual]==self.signos['COMA']):
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),',','TK_coma_matriz')
                    self.estado = 5
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Debe de ingresar una coma*')
                    break
            elif (self.estado == 5): #Tk_nombre_matriz 
                size = self.comilla_(actual)
                size2 = self.buscar_numeral(actual)
                if (self.entrada[size]==self.signos['COMILLAS'] or self.entrada[size]==self.signos['DOBLECOMILLA']):
                    self.tem = self.entrada[size]
                    actual = size
                    actual += 1
                    size = self.get_size_nombre_lista(actual)
                    if(self.entrada[size]==self.tem):
                        nombre_lista = self.lexema_global.lower()
                        self.tem_nombre = nombre_lista
                        self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),self.tem+self.lexema_global+self.tem,'TK_nombre_matriz')
                        actual = size
                        self.estado = 6
                    else:
                        self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Debe de ingresar una Comilla o Doble Comilla")
                        break
                elif (self.entrada[size2]==self.signos['NUMERAL']):
                    actual = size2
                    self.guardar_lista_token(lista_token,self.get_fila(actual),self.get_columna(actual),'#','TK_etiqueta_matriz')
                    self.estado = 6

                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[actual],"Etiqueta incorrecta'")
                    break
            elif (self.estado == 6): # Tk_parentesis_cerrado
                print(f'Estado actual: {self.estado} - Aceptado 100')
                size = self.parentesis_cerrado(actual)
                if (self.entrada[size]==self.signos['PARENTESISC']):
                    
                    self.guardar_lista_token(lista_token,self.get_fila(size),self.get_columna(size),')','TK_parentesis_cerrado')
                    actual = size
                    self.estado = 0
                    return actual
                else:
                    self.guardar_lista_error(lista_error,self.get_fila(size),self.get_columna(size),self.entrada[size],'Se espera un parentesis cerrado  )')
                    break

            actual += 1

        return actual

    def guardar_matriz(self,fila,columna,nombre,forma,boolean):
        almacenado = Matriz(self.contador_matriz,fila,columna,nombre,forma,boolean)
        self.matriz.append(almacenado)

    def guardar_elemento_matriz(self,fila,columna,etiqueta,color):
        almacenado = MatrizElemento(self.contador_matriz,fila,columna,etiqueta,color)
        self.elemento_matriz.append(almacenado)

    def guardar_elemento_matriz2(self,fila,columna,etiqueta,color):
        almacenado = MatrizElemento(self.contador_matriz,fila,columna,etiqueta,color)
        self.elemento_matriz2.append(almacenado)

    def matriz_color(self,fila,color):
        almacenado = MatrizColor(self.contador_matriz,fila,color)
        self.color_matriz.append(almacenado)

    def nodo_color_matriz(self,actual,lista_error,lista_token):
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
            self.nodo_dos = lexema.lower()
            self.guardar_elemento_matriz2(int(self.tem_fila),(self.tem_columna),self.tem_nombre,lexema)
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
            self.nodo_dos = '#'
            self.guardar_elemento_matriz2(int(self.tem_fila),(self.tem_columna),self.tem_nombre,'#')
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