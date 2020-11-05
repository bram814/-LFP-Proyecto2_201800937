import os
import sys
import msvcrt

from vista.Reporte import Reporte

from controlador.Archivo import Archivo
from controlador.Graphviz import Graphviz

class Main():

    def __init__(self):
        self.reporte_error = Reporte()
        self.archivo = Archivo()
        self.graph = Graphviz()
        self.salvar = 1

    def menu_principal(self,lista_error,lista_token):
        print("\n**********************************************************")
        print("v***v    #Proyecto #2    v***v")
        print("v***v    Lenguajes Formales y de Programacion -A     v***v")
        print("v***v    Jose Abraham Solorzano Herrera     201800937v***v")
        print("**********************************************************\n")
        while True:
            try:
                print("1. Cargar Archivo")
                print("2. Generar Grafica")
                print("3. Salir.")
                print("\n Ingrese un numero: ")
                entrada = int(input())
                if (entrada == 1) :
                    self.archivo.open_File(lista_error,lista_token)
                elif (entrada == 2) :

                    
                    if (self.archivo.anazalidar_a.estado_lista == True):


                        i = 0
                        print('TITULO')
                        while i < len(self.archivo.anazalidar_a.lista):
                            print(f'{self.archivo.anazalidar_a.lista[i].getContador()} {self.archivo.anazalidar_a.lista[i].getNombre()} {self.archivo.anazalidar_a.lista[i].getForma()} {self.archivo.anazalidar_a.lista[i].getBoolean()}')
                            i += 1  
                        
                        print('ELEMENTOS')
                        j = 0
                        while j < len(self.archivo.anazalidar_a.elemento_lista):
                            print(f'{self.archivo.anazalidar_a.elemento_lista[j].getContador()} {self.archivo.anazalidar_a.elemento_lista[j].getEtiqueta()} {self.archivo.anazalidar_a.elemento_lista[j].getColor()}')
                            j += 1

                        
                        print('')
                        j = 0
                        while j < len(self.archivo.anazalidar_a.elemento_lista):
                            actual = self.archivo.anazalidar_a.elemento_lista[j].getContador()

                            if (self.archivo.anazalidar_a.elemento_lista[j].getEtiqueta()=='#'):
                                self.archivo.anazalidar_a.elemento_lista[j].setEtiqueta(self.retornar_etiqueta(actual))
                                print(self.archivo.anazalidar_a.elemento_lista[j].getEtiqueta())

                                if(self.archivo.anazalidar_a.elemento_lista[j].getColor()=='#'):
                                    self.archivo.anazalidar_a.elemento_lista[j].setColor(self.retornar_color(actual))
                                    print(self.archivo.anazalidar_a.elemento_lista[j].getColor())
                            else:
                                if(self.archivo.anazalidar_a.elemento_lista[j].getColor()=='#'):
                                    self.archivo.anazalidar_a.elemento_lista[j].setColor(self.retornar_color(actual))
                                j += 1  
                        
                        z = 0
                        print('DEFECTO')
                        while z < len(self.archivo.anazalidar_a.defecto_lista):
                            print(f'{self.archivo.anazalidar_a.defecto_lista[z].getContador()} {self.archivo.anazalidar_a.defecto_lista[z].getNombre()} {self.archivo.anazalidar_a.defecto_lista[z].getColor()}')
                            z += 1 
                        print('')
                        p = 0
                        while p < len(self.archivo.anazalidar_a.elemento_lista):
                            print(f'{self.archivo.anazalidar_a.elemento_lista[p].getContador()} {self.archivo.anazalidar_a.elemento_lista[p].getEtiqueta()} {self.archivo.anazalidar_a.elemento_lista[p].getColor()}')
                            p += 1
                        
                        print('\n')

                        i = 0
                        while i < len(self.archivo.anazalidar_a.lista):
                            nombre = self.archivo.anazalidar_a.lista[i].getNombre()
                            self.graph.reporte_svg(self.archivo.anazalidar_a.elemento_lista,self.archivo.anazalidar_a.lista[i].getContador(),self.archivo.anazalidar_a.lista[i].getNombre(),self.archivo.anazalidar_a.lista[i].getForma(),self.archivo.anazalidar_a.lista[i].getBoolean())
                            
                            i += 1  

                        self.reporte_error.reporte_html(lista_token,nombre)
                    
                    elif (self.archivo.anazalidar_a.estado_matriz == True):

                        print('\n')
                        x = 0 
                        while x < len(self.archivo.anazalidar_a.matriz):
                            print(f'{self.archivo.anazalidar_a.matriz[x].__str__()}')
                            x += 1
                        print('\n\tElementos 1')

                        x = 0 
                        while x < len(self.archivo.anazalidar_a.elemento_matriz):
                            print(f'{self.archivo.anazalidar_a.elemento_matriz[x].__str__()}')
                            x += 1
                        print('\n\tElementos2 - Posicion')
                        x = 0 
                        while x < len(self.archivo.anazalidar_a.elemento_matriz2):
                            print(f'{self.archivo.anazalidar_a.elemento_matriz2[x].__str__()}')
                            x += 1
                        print('\nColor por Fila')
                        x = 0 
                        while x < len(self.archivo.anazalidar_a.color_matriz):
                            print(f'{self.archivo.anazalidar_a.color_matriz[x].__str__()}')
                            x += 1

                        x = 0 
                        while x < len(self.archivo.anazalidar_a.elemento_matriz):
                            actual = self.archivo.anazalidar_a.elemento_matriz[x].getContador()
                            if (self.archivo.anazalidar_a.elemento_matriz[x].getColor()=='defecto'):
                                self.archivo.anazalidar_a.elemento_matriz[x].setColor(self.retornar_color(actual))
                            x += 1

                        x = 0 
                        while x < len(self.archivo.anazalidar_a.elemento_matriz):
                            actual = self.archivo.anazalidar_a.elemento_matriz[x].getContador()
                            fila = self.archivo.anazalidar_a.elemento_matriz[x].getFila()
                            if (self.archivo.anazalidar_a.elemento_matriz[x].getColor()=='disponible'):
                                color = self.retornar_color_matriz(actual,fila)
                                self.archivo.anazalidar_a.elemento_matriz[x].setColor(color)
                                
                            x += 1
                        
                        print('\n\tElementos Cambiados')
                        
                        x = 0 
                        while x < len(self.archivo.anazalidar_a.elemento_matriz):
                            print(f'{self.archivo.anazalidar_a.elemento_matriz[x].__str__()}')
                            
                            x += 1
                        
                        x = 0
                        while x < len(self.archivo.anazalidar_a.elemento_matriz2):

                            contador = self.archivo.anazalidar_a.elemento_matriz2[x].getContador()
                            fila = self.archivo.anazalidar_a.elemento_matriz2[x].getFila()
                            columna = self.archivo.anazalidar_a.elemento_matriz2[x].getColumna()
                            nombre = self.archivo.anazalidar_a.elemento_matriz2[x].getEtiqueta()
                            color = self.archivo.anazalidar_a.elemento_matriz2[x].getColor()
                            print(contador,fila,columna,nombre,color)
                            self.enviar_matriz(contador,fila,columna,nombre,color)
                            x += 1
                        j = 0
                        while j < len(self.archivo.anazalidar_a.elemento_matriz):
                            actual = self.archivo.anazalidar_a.elemento_matriz[j].getContador()
                            
                            if (self.archivo.anazalidar_a.elemento_matriz[j].getEtiqueta()=='#'):
                                print(f'{self.retornar_etiqueta(actual)}{str(self.salvar)}')
                                self.archivo.anazalidar_a.elemento_matriz[j].setEtiqueta(f'{self.retornar_etiqueta(actual)}{str(self.salvar)}')
                                self.salvar +=1
                                if(self.archivo.anazalidar_a.elemento_matriz[j].getColor()=='#'):
                                    self.archivo.anazalidar_a.elemento_matriz[j].setColor(self.retornar_color(actual))
                                   
                            else:
                                if(self.archivo.anazalidar_a.elemento_matriz[j].getColor()=='#'):
                                    self.archivo.anazalidar_a.elemento_matriz[j].setColor(self.retornar_color(actual))
                            j += 1  
                        print('\n\tElementos Corregidos')
                        
                        x = 0 
                        while x < len(self.archivo.anazalidar_a.elemento_matriz):
                            print(f'{self.archivo.anazalidar_a.elemento_matriz[x].__str__()}')
                            
                            x += 1
                        

                        x = 0 
                        while x < len(self.archivo.anazalidar_a.matriz):

                            contador = self.archivo.anazalidar_a.matriz[x].getContador()
                            fila = self.archivo.anazalidar_a.matriz[x].getFila()
                            columna = self.archivo.anazalidar_a.matriz[x].getColumna()
                            nombre = self.archivo.anazalidar_a.matriz[x].getNombre()
                            forma = self.archivo.anazalidar_a.matriz[x].getForma()
                            boolean = self.archivo.anazalidar_a.matriz[x].getBoolean()
                            
                            self.graph.reporte_matriz(self.archivo.anazalidar_a.elemento_matriz,contador,fila,columna,nombre,forma,boolean)
                            
                            x += 1

                           
                        self.reporte_error.reporte_html(lista_token,nombre)
                    




                elif (entrada == 3) :
                    break

            except:
                self.menu_principal(lista_error,lista_token)

    # DEFECTO
    def retornar_etiqueta(self,i):
        z = 0
        retornar = ''
        while z < len(self.archivo.anazalidar_a.defecto_lista):
            if ( self.archivo.anazalidar_a.defecto_lista[z].getContador() == i):
                retornar = self.archivo.anazalidar_a.defecto_lista[z].getNombre()
                return  retornar
            z += 1 
        return retornar

    def retornar_color(self,i):
        z = 0
        retornar = ''
        while z < len(self.archivo.anazalidar_a.defecto_lista):
            if ( self.archivo.anazalidar_a.defecto_lista[z].getContador() == i):
                retornar = self.archivo.anazalidar_a.defecto_lista[z].getColor()
                return  retornar
            z += 1 
        return retornar
    
    def retornar_color_matriz(self,contador,fila):
        x = 0 
        retornar = ''
        while x < len(self.archivo.anazalidar_a.color_matriz):
           
            if(self.archivo.anazalidar_a.color_matriz[x].getContador()==contador and self.archivo.anazalidar_a.color_matriz[x].getFila()==fila):
                retornar = self.archivo.anazalidar_a.color_matriz[x].getColor()
                return retornar
            x += 1
        return retornar        
    
    def enviar_matriz(self,contador,fila,columna,nombre,color):
        x = 0
        while x < len(self.archivo.anazalidar_a.elemento_matriz):
            contador_matriz =self.archivo.anazalidar_a.elemento_matriz[x].getContador()
            fila_matriz = self.archivo.anazalidar_a.elemento_matriz[x].getFila()
            columna_matriz = self.archivo.anazalidar_a.elemento_matriz[x].getColumna()
            if (int(contador_matriz) == int(contador) and int(fila_matriz) == int(fila) and int(columna_matriz) == int(columna)):
                print('valido')
                print(nombre)
                print(color)
                self.archivo.anazalidar_a.elemento_matriz[x].setEtiqueta(nombre)
                self.archivo.anazalidar_a.elemento_matriz[x].setColor(color)
            x += 1


lista_error = []
lista_token = []


main = Main()
main.menu_principal(lista_error,lista_token)