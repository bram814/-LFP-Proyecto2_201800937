from tkinter import filedialog
from io import open
from controlador.Analizador_A import Anazalizador_A

class Archivo():

    def __init__(self):
       self.anazalidar_a = Anazalizador_A()

    def open_File(self,lista_error,lista_token):
            try:
                #root = Tk()
                ruta =  ""
                filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.txt"),("TXT files","*.lfp"),("all files","*.*")))
                ruta = filename
                if ruta != "":
                    self.cargar_Archivo(ruta,lista_error,lista_token)
                    return ruta
                else:
                    
                    return None

            except IndexError as e:
                print(e)   

    def cargar_Archivo(self,ruta,lista_error,lista_token):
        print(f"Ruta: {ruta}")
        try:
        
            archivo = open(f"{ruta}","r", encoding="utf-8")
            texto = archivo.readlines()
            archivo.close()
            #print(f"Texto:{texto}\n")
            self.anazalidar_a.__inicio__(texto,lista_error,lista_token)

            
        except (FileNotFoundError):
            print("Error")


    