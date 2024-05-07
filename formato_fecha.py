import datetime

def convertir_formato(fecha_original=""):
    # Dividir el string en partes relevantes
    fecha_original = fecha_original.replace(" ","")
    dia = fecha_original[0:2]
    mes = fecha_original[3:5]
    anio = fecha_original[6:10]
    hora = fecha_original[10:12]
    minutos = fecha_original[13:15]

    # Convertir a datetime
    fecha = datetime.datetime(int(anio), int(mes), int(dia), int(hora), int(minutos))

    # Formatear en el nuevo formato
    fecha_formateada = fecha.strftime("%d-%m-%Y %H:%M")

    return fecha_formateada

# Ejemplo de uso:
# fecha_original = '20/04/202408.54.13'
# fecha_formateada = convertir_formato(fecha_original)
# print(fecha_formateada)  # Salida: 20-04-2024 08:54
