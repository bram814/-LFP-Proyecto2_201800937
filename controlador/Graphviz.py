import enum 

from graphviz import Digraph

# DOCUMENTACION DE GRAPHVIZ
# https://graphviz.readthedocs.io/en/stable/examples.html
class Graphviz():

    def __init__(self):
        self.fila_ = 1
        self.columna_ = 1
        self.tem_fila = 1
        self.tem_columna = 1

    def reporte_svg(self,lista_elementos,contador,nombre,forma,doble):

        if (forma.lower() == Forma.circulo.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.circulo.value}')
        
        elif (forma.lower() == Forma.rectangulo.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.rectangulo.value}')

        elif (forma.lower() == Forma.triangulo.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.triangulo.value}')
        
        elif (forma.lower() == Forma.punto.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.punto.value}')
        
        elif (forma.lower() == Forma.hexagono.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.hexagono.value}')
        
        elif (forma.lower() == Forma.diamante.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.diamante.value}')

        for linea in lista_elementos:

            if (linea.getColor().lower() == Color.azul.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.azul.value))
            elif (linea.getColor().lower() == Color.azul2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.azul2.value))
            elif (linea.getColor().lower() == Color.azul3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.azul3.value))
            
            elif (linea.getColor().lower() == Color.rojo.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.rojo.value))
            elif (linea.getColor().lower() == Color.rojo2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.rojo2.value))
            elif (linea.getColor().lower() == Color.rojo3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.rojo3.value))

            elif (linea.getColor().lower() == Color.amarillo.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.amarillo.value))
            elif (linea.getColor().lower() == Color.amarillo2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.amarillo2.value))
            elif (linea.getColor().lower() == Color.amarillo3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.amarillo3.value))
            
            elif (linea.getColor().lower() == Color.anaranjado.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.anaranjado.value))
            elif (linea.getColor().lower() == Color.anaranjado2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.anaranjado2.value))
            elif (linea.getColor().lower() == Color.anaranjado3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.anaranjado3.value))

            elif (linea.getColor().lower() == Color.cafe.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.cafe.value))
            elif (linea.getColor().lower() == Color.cafe2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.cafe2.value))
            elif (linea.getColor().lower() == Color.cafe3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.cafe3.value))
            
            elif (linea.getColor().lower() == Color.gris.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.gris.value))
            elif (linea.getColor().lower() == Color.gris2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.gris2.value))
            elif (linea.getColor().lower() == Color.gris3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.gris3.value))
            
            elif (linea.getColor().lower() == Color.morado.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.morado.value))
            elif (linea.getColor().lower() == Color.morado2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.morado2.value))
            elif (linea.getColor().lower() == Color.morado3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.morado3.value))

            elif (linea.getColor().lower() == Color.verde.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.verde.value)) 
            elif (linea.getColor().lower() == Color.verde2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.verde2.value))  
            elif (linea.getColor().lower() == Color.verde3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.verde3.value))

            elif (linea.getColor().lower() == Color.blanco.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.blanco.value))              

        if (doble.lower() == 'verdadero'):
            x = 0
            while x < len(lista_elementos):
                if (x +1 == len(lista_elementos)):
                    break
                f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'')
                f.edge(f'{lista_elementos[x+1].getEtiqueta()}', f'{lista_elementos[x].getEtiqueta()}', label=f'') 
                x += 1
        elif (doble.lower() == 'falso'):

            x = 0
            while x < len(lista_elementos):
                if (x +1 == len(lista_elementos)):
                    break
                f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
                x += 1
        f.attr(label=nombre)
        f.view()
    




    
    def reporte_matriz(self,lista_elementos,contador,fila,columna,nombre,forma,doble):
        
        if (forma.lower() == Forma.circulo.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.circulo.value}')
        
        elif (forma.lower() == Forma.rectangulo.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5', )    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.rectangulo.value}')

        elif (forma.lower() == Forma.triangulo.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.triangulo.value}')
        
        elif (forma.lower() == Forma.punto.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.punto.value}')
        
        elif (forma.lower() == Forma.hexagono.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.hexagono.value}')
        
        elif (forma.lower() == Forma.diamante.name):
            f = Digraph(format='svg', name='Imagen_Reporte')
            f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
            f.attr('node', shape=f'{Forma.diamante.value}')

        for linea in lista_elementos:

            if (linea.getColor().lower() == Color.azul.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.azul.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.azul2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.azul2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.azul3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.azul3.value), group=f'{linea.getFila()}')
            
            elif (linea.getColor().lower() == Color.rojo.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.rojo.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.rojo2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.rojo2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.rojo3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.rojo3.value), group=f'{linea.getFila()}')

            elif (linea.getColor().lower() == Color.amarillo.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.amarillo.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.amarillo2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.amarillo2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.amarillo3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.amarillo3.value), group=f'{linea.getFila()}')
            
            elif (linea.getColor().lower() == Color.anaranjado.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.anaranjado.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.anaranjado2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.anaranjado2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.anaranjado3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.anaranjado3.value), group=f'{linea.getFila()}')

            elif (linea.getColor().lower() == Color.cafe.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.cafe.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.cafe2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.cafe2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.cafe3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.cafe3.value), group=f'{linea.getFila()}')
            
            elif (linea.getColor().lower() == Color.gris.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.gris.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.gris2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.gris2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.gris3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.gris3.value), group=f'{linea.getFila()}')
            
            elif (linea.getColor().lower() == Color.morado.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.morado.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.morado2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.morado2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.morado3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.morado3.value), group=f'{linea.getFila()}')

            elif (linea.getColor().lower() == Color.verde.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.verde.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.verde2.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.verde2.value), group=f'{linea.getFila()}')
            elif (linea.getColor().lower() == Color.verde3.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.verde3.value), group=f'{linea.getFila()}')

            elif (linea.getColor().lower() == Color.blanco.name):
                f.node(f'{linea.getEtiqueta()}', style='filled',fillcolor=(Color.blanco.value), group=f'{linea.getFila()}')


        if (doble.lower() == 'verdadero'):
            x = 0
            while x < len(lista_elementos):
                if (x +1 == len(lista_elementos)):
                    break
                else:
                    i = 0
                    while i < int(fila):
                        if (int(self.fila_) < int(fila)):  
                            j = 0 
                            self.columna_ = 1
                            while j < int(columna):

                                if (int(self.columna_) < int(columna)):
                                    enviar_nombre = lista_elementos[x].getEtiqueta()
                                    enviar_fila = lista_elementos[x].getFila()
                                    enviar_columna = lista_elementos[x].getColumna()

                                    f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'')
                                    #f.edge(f'{lista_elementos[x+1].getEtiqueta()}',f'{lista_elementos[x].getEtiqueta()}',  label=f'')
                                    #f.attr(rank='same' f';{lista_elementos[x].getEtiqueta()};' f'{lista_elementos[x+1].getEtiqueta()}') 
                                    f.edge(f'{enviar_nombre}',f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}', label='')
                                    f.edge(f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}',f'{enviar_nombre}', label='')
                                    
                                    self.columna_ += 1

                                    x += 1
                                elif (int(self.columna_) == int(columna)):
                                    #f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'')
                                    enviar_nombre = lista_elementos[x].getEtiqueta()
                                    enviar_fila = lista_elementos[x].getFila()
                                    enviar_columna = lista_elementos[x].getColumna()
                                    f.edge(f'{enviar_nombre}',f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}', label='')
                                    f.edge(f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}',f'{enviar_nombre}', label='')
                                    
                                    self.columna_ = 1
                                    x += 1
                                    break
                                    #x += 1
                                    
                                j += 1
                        elif (int(self.fila_) == int(fila)):
                            j = 0 
                            self.columna_ = 1
                            while j < int(columna):

                                if (int(self.columna_) < int(columna)):
                                    enviar_nombre = lista_elementos[x].getEtiqueta()
                                    enviar_fila = lista_elementos[x].getFila()
                                    enviar_columna = lista_elementos[x].getColumna()
                                    f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
                                    #f.edge(f'{nombre}',f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}', label='')
                                    #f.edge(f'{lista_elementos[x+1].getEtiqueta()}', f'{lista_elementos[x].getEtiqueta()}', label=f'') 
                                    self.columna_ += 1

                                    x += 1
                                elif (int(self.columna_) == int(columna)):
                                    
                                    #f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
                                    self.columna_ = 1
                                    #x += 1
                                    break
                                    #x += 1
                                    
                                j += 1


                        self.fila_ += 1
                        i += 1
                x += 1

        elif (doble.lower() == 'falso'):
            x = 0
            while x < len(lista_elementos):
                if (x +1 == len(lista_elementos)):
                    break
                else:
                    i = 0
                    while i < int(fila):
                        if (int(self.fila_) < int(fila)):  
                            j = 0 
                            self.columna_ = 1
                            while j < int(columna):

                                if (int(self.columna_) < int(columna)):
                                    enviar_nombre = lista_elementos[x].getEtiqueta()
                                    enviar_fila = lista_elementos[x].getFila()
                                    enviar_columna = lista_elementos[x].getColumna()
                                    f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'')
                                    #f.attr(rank='same' f';{lista_elementos[x].getEtiqueta()};' f'{lista_elementos[x+1].getEtiqueta()}') 
                                    f.edge(f'{enviar_nombre}',f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}', label='')
                                    self.columna_ += 1

                                    x += 1
                                elif (int(self.columna_) == int(columna)):
                                    #f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'')
                                    enviar_nombre = lista_elementos[x].getEtiqueta()
                                    enviar_fila = lista_elementos[x].getFila()
                                    enviar_columna = lista_elementos[x].getColumna()
                                    f.edge(f'{enviar_nombre}',f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}', label='')
 
                                    self.columna_ = 1
                                    x += 1
                                    break
                                    #x += 1
                                    
                                j += 1
                        elif (int(self.fila_) == int(fila)):
                            j = 0 
                            self.columna_ = 1
                            while j < int(columna):

                                if (int(self.columna_) < int(columna)):
                                    enviar_nombre = lista_elementos[x].getEtiqueta()
                                    enviar_fila = lista_elementos[x].getFila()
                                    enviar_columna = lista_elementos[x].getColumna()
                                    f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
                                    #f.edge(f'{nombre}',f'{self.buscar_nodo(lista_elementos,enviar_fila+1,enviar_columna)}', label='')
                                    self.columna_ += 1

                                    x += 1
                                elif (int(self.columna_) == int(columna)):
                                    #f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
                                    self.columna_ = 1
                                    #x += 1
                                    break
                                    #x += 1
                                    
                                j += 1


                        self.fila_ += 1
                        i += 1
                x += 1
        
        f.attr(label=nombre)
        f.view()

    
    def buscar_nodo(self,lista_elementos,fila,columna):
        x = 0 
        while x <len(lista_elementos):

            if (lista_elementos[x].getFila() == fila and lista_elementos[x].getColumna() == columna):
                return lista_elementos[x].getEtiqueta()
            x += 1
        


class Color(enum.Enum):
    azul        = '#8bc6f1'
    azul2       = '#376ce6'
    azul3       = '#082b7b'

    rojo        = '#f09392'
    rojo2       = '#df0b09'
    rojo3       = '#860100'

    amarillo    = '#f9f79e'
    amarillo2   = '#e8e300'
    amarillo3   = '#b3af02'

    anaranjado  = '#f1bc96'
    anaranjado2 = '#e6660a'
    anaranjado3 = '#c85300'

    cafe        = '#ad8466'
    cafe2       = '#85532f'
    cafe3       = '#843700'

    gris        = '#cdcdcc'
    gris2       = '#b1b1b1'
    gris3       = '#7a7a7a'

    morado      = '#d598ec'
    morado2     = '#ba44e6'
    morado3     = '#9900d2'

    verde       = '#8bd896'
    verde2      = '#13da30'
    verde3      = '#009315'
    blanco      = '#ffffff'

class Forma(enum.Enum):
    circulo     = 'circle'
    rectangulo  = 'rectangle'
    triangulo   = 'triangle'
    punto       = 'point'
    hexagono    = 'hexagon'
    diamante    = 'diamond'

# EJEMPLO DE UN ARBOL

"""

from graphviz import Digraph, nohtml

g = Digraph('g', filename='btree.gv',
            node_attr={'shape': 'record', 'height': '.1'})

g.node('node0', nohtml('<f0> |<f1> G|<f2>'))
g.node('node1', nohtml('<f0> |<f1> E|<f2>'))
g.node('node2', nohtml('<f0> |<f1> B|<f2>'))
g.node('node3', nohtml('<f0> |<f1> F|<f2>'))
g.node('node4', nohtml('<f0> |<f1> R|<f2>'))
g.node('node5', nohtml('<f0> |<f1> H|<f2>'))
g.node('node6', nohtml('<f0> |<f1> Y|<f2>'))
g.node('node7', nohtml('<f0> |<f1> A|<f2>'))
g.node('node8', nohtml('<f0> |<f1> C|<f2>'))

g.edge('node0:f2', 'node4:f1')
g.edge('node0:f0', 'node1:f1')
g.edge('node1:f0', 'node2:f1')
g.edge('node1:f2', 'node3:f1')
g.edge('node2:f2', 'node8:f1')
g.edge('node2:f0', 'node7:f1')
g.edge('node4:f2', 'node6:f1')
g.edge('node4:f0', 'node5:f1')

g.view()
"""