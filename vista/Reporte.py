# Instalar la libreria con el comando $ pip install pdfkit

import pdfkit
#from tkinter import filedialog
#from io import open

class Reporte():

    def __init__(self):
        pass

    def html_error(self):

        document = open("Reporte_Error.html",'w')

        message = """<!DOCTYPE html>
        <html> 
            <head>
                <tile> Errores</title>
            </head>
            <body>
                <h1> Tabla Errores </h1>

                <table border="1">
                    <tr> 
                        <td bgcolor="99FF99"> No.           </td>
                        <td bgcolor="99FF99"> Fila          </td>
                        <td bgcolor="99FF99"> Columna       </td>
                        <td bgcolor="99FF99"> Caracter      </td>
                        <td bgcolor="99FF99"> Descripcion   </td>
                    </tr>

                    <tr> 
                        <td> 1</td>
                        <td> 22</td>
                        <td> 20000</td>
                        <td> # </td>
                        <td> No se muestra</td>
                        
                    </tr>

                </table>
            </body>
        </html>
        """
        
        print('prueba2')
        document.write(message)
        document.close()

        try:
            path_wkhtmltopdf = "C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe"
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            pdfkit.from_file("Reporte_Error.html", "Reporte_Error_pdf.pdf",configuration=config)
        except Exception as e:
            print(e)
         
prueba = Reporte()
prueba.html_error()