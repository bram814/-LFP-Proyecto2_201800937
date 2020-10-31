import enum 

from graphviz import Digraph

class Graphviz():

    def __init__(self):
        pass

    def reporte_png(self,lista_elementos,contador,nombre,forma,doble):

        f = Digraph(format='png', name='Imagen_Reporte')
        f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
        f.attr('node', shape=f'circle')
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


        x = 0
        while x < len(lista_elementos):
            if (x +1 == len(lista_elementos)):
                break
            f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
            x += 1


        f.view()
    
    def reporte_svg(self,lista_elementos,contador,nombre,forma,doble):

        f = Digraph(format='svg', name='Imagen_Reporte')
        f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
        f.attr('node', shape=f'circle')

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


        x = 0
        while x < len(lista_elementos):
            if (x +1 == len(lista_elementos)):
                break
            f.edge(f'{lista_elementos[x].getEtiqueta()}', f'{lista_elementos[x+1].getEtiqueta()}', label=f'') 
            x += 1

        f.view()



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
    pass

    