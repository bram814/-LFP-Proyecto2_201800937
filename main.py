import os
import sys
import msvcrt

from controlador.Archivo import Archivo
class Main():

    __instance = None
    
    @staticmethod
    def getInstance():
        if Main.__instance == None:
            Main()
        return Main.__instance

    def __init__(self):
        if Main.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Main.__instance = self
        
        self.archivo = Archivo()



    def menu_principal(self):
        os.system("cls")
        print("\n**********************************************************")
        print("v***v    #Proyecto #2    v***v")
        print("v***v    Lenguajes Formales y de Programacion -A     v***v")
        print("v***v    Jose Abraham Solorzano Herrera     201800937v***v")
        print("**********************************************************\n")
        try:
            while True:
                m = str(msvcrt.getch(),'utf-8')
                if(m == "\r"):
                    os.system("cls")
                    self.menu_secundario()
                    break
                else:
                    self.menu_principal()
        except UnicodeEncodeError:
            print('¿Desea Salir? e')
            entrada  = str(input())
            if(entrada=='s'):
                sys.exit()



    def menu_secundario(self):

        while True:
            try:
                print("1. Cargar Archivo")
                print("2. Generar Grafica")
                print("3. Salir.")
                print("\n Ingrese un numero: ")
                entrada = int(input())
                if (entrada == 1) :
                    self.archivo.open_File()
                elif (entrada == 2) :
                    print("Generar Grafica")
                elif (entrada == 3) :
                    sys.exit()
            except:
                main.menu_secundario()
main = Main().getInstance()
main.menu_principal()
