# Instalar la libreria con el comando $ pip install pdfkit

import pdfkit

class Reporte():

    def __init__(self):
        pass

    def html_error(self):

        document = open("Reporte_Error.html",'w')

        message = """
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
                        <td> 43</td>
                        <td> @ </td>
                        <td> No se muestra</td>
                        
                    </tr>

                </table>
            </body>
        </html>
        """
        document.write(message)
        document.close()
        #with open('file.html') as f:
         #   pdfkit.from_file(f, 'out.pdf')
        #pdfkit.from_file("Reporte_Error.html", 'Reporte_E.pdf')


    def html_token(self):
        pass

prueba = Reporte()
prueba.html_error()