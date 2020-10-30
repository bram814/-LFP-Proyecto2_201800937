import os
import sys
import msvcrt

from controlador.Archivo import Archivo

class Main():

    def __init__(self):
        self.archivo = Archivo()

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

                    print("Generar Grafica")
                    x = 0
                    while x < len(lista_token):
                        print(f'{lista_token[x].getContador()} {lista_token[x].getToken()}')
                        x += 1
                    i = 0
                    print('TITULO')
                    while i < len(self.archivo.anazalidar_a.lista):
                        print(f'{self.archivo.anazalidar_a.lista[i].getContador()} {self.archivo.anazalidar_a.lista[i].getNombre()} {self.archivo.anazalidar_a.lista[i].getForma()} {self.archivo.anazalidar_a.lista[i].getBoolean()}')
                        i += 1  
                    j = 0
                    print('ELEMENTOS')
                    while j < len(self.archivo.anazalidar_a.elemento_lista):
                        print(f'{self.archivo.anazalidar_a.elemento_lista[j].getContador()} {self.archivo.anazalidar_a.elemento_lista[j].getEtiqueta()} {self.archivo.anazalidar_a.elemento_lista[j].getColor()}')
                        j += 1  
                    
                    z = 0
                    print('DEFECTO')
                    while z < len(self.archivo.anazalidar_a.defecto_lista):
                        print(f'{self.archivo.anazalidar_a.defecto_lista[z].getContador()} {self.archivo.anazalidar_a.defecto_lista[z].getNombre()} {self.archivo.anazalidar_a.defecto_lista[z].getColor()}')
                        z += 1 
                    
                    print('\n')
                elif (entrada == 3) :
                    break

            except:
                self.menu_principal(lista_error,lista_token)

lista_error = []
lista_token = []


main = Main()
main.menu_principal(lista_error,lista_token)