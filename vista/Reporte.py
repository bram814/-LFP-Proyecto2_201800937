# Instalar la libreria con el comando $ pip install pdfkit

import pdfkit
#from tkinter import filedialog
#from io import open

class Reporte():

    def __init__(self):
        pass

    def html_error(self,lista_error):

        document = open("Reporte_Error.html",'w')

        message = f"""<!DOCTYPE html>
        <html> 
            <head>
                <tile> Errores</title>
            </head>
            <body>
                <div style="text-align:center;">
                    <h1> Tabla Errores </h1>

                    <table border="1" align="center">
                        <tr> 
                            <td bgcolor="99FF99"> No.           </td>
                            <td bgcolor="99FF99"> Fila          </td>
                            <td bgcolor="99FF99"> Columna       </td>
                            <td bgcolor="99FF99"> Caracter      </td>
                            <td bgcolor="99FF99"> Descripcion   </td>
                        </tr>
                </div>
                    {self.retornar_error(lista_error)}

                </table>
            </body>
        </html>
        """

        document.write(message)
        document.close()

        
        #path_wkhtmltopdf = "C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe"
        #config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        #pdfkit.from_file("Reporte_Error.html", "Reporte_Error.pdf",configuration=config)
        
         

    def reporte_html(self,lista_token):

        document = open("Reporte.html",'w')

        message = f"""<!DOCTYPE html>
        <html> 
            <head>
                <tile> Reporte Final </title>
            </head>
            <body>
                
                <div style="text-align:center;">
                    <h1> Tabla Tokens</h1>
                    
                    <table border="1" align="center">
                        <tr> 
                            <td bgcolor="33ffda"> No.       </td>
                            <td bgcolor="33ffda"> Fila      </td>
                            <td bgcolor="33ffda"> Columna   </td>
                            <td bgcolor="33ffda"> Lexema    </td>
                            <td bgcolor="33ffda"> Token     </td>
                        </tr>
                </div>
                    {self.retornar_token(lista_token)}

                </table>
            </body>
        </html>
        """
        
        document.write(message)
        document.close()

        
        #path_wkhtmltopdf = "C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe"
        #config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        #pdfkit.from_file("Reporte.html", "Reporte.pdf",configuration=config)
        
         

         
    def retornar_error(self,lista_error):
        variable = ''
        x = 0

        while x < len (lista_error):

            variable += f""" 
            <tr> 
                <td> {lista_error[x].getContador()}</td>
                <td> {lista_error[x].getFila()}</td>
                <td> {lista_error[x].getColumna()}</td>
                <td> {lista_error[x].getCaracter()}</td>
                <td> {lista_error[x].getDescripcion()}</td>
            </tr>
            """

            x += 1
        return variable

    def retornar_token(self,lista_token):
        variable = ''
        x = 0 
        while x < len(lista_token):

            variable += f""" 
            <tr> 
                <td> {lista_token[x].getContador()}</td>
                <td> {lista_token[x].getFila()}</td>
                <td> {lista_token[x].getColumna()}</td>
                <td> {lista_token[x].getLexema()}</td>
                <td> {lista_token[x].getToken()}</td>
            </tr>
            
            """
            x += 1
        return variable