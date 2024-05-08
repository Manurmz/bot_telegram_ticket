import jinja2
import pdfkit
import os


def crear_pdf(info):
    nombre_html = "ticket.html"  # Solo el nombre del archivo
    nombre_css = "estilos.css"   # Solo el nombre del archivo
    # Obtener la ruta del directorio del script
    directorio_script = os.path.dirname(os.path.realpath(__file__))

    # Construir las rutas completas a los archivos HTML y CSS
    ruta_html_completa = os.path.join(directorio_script, nombre_html)
    ruta_css_completa = os.path.join(directorio_script, nombre_css)

    loader = jinja2.FileSystemLoader(os.path.dirname(ruta_html_completa))  # Usar solo el directorio del archivo
    env = jinja2.Environment(loader=loader)

    template = env.get_template(nombre_html)  # Pasar solo el nombre del archivo
    html = template.render(info)

    options = {
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'page-width': '2in',
        'page-height': '3.2in'
    }

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    nombre_pdf = 'ticket.pdf'
    ruta_salida = os.path.join(directorio_script, nombre_pdf)

    pdfkit.from_string(html, ruta_salida, configuration=config, options=options, css=ruta_css_completa)

    return nombre_pdf

# data = {
#     "servicio": "CFE",
#     "referencia": "REF123456789",
#     "monto": 150.75,
#     "comision": 10.25,
#     "total": 161,
#     "folio": "FOLIO987654321",
#     "hora": "2024-04-24 15:30:00"
# }
# dir = crear_pdf(data)

# print(dir)
