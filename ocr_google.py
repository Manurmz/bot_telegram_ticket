import os
from PIL import Image
import io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'permisos-personales.json'

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    
    imagen = io.BytesIO(path)

    content = recortar_imagen(imagen)

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    ocr = []
    # print("Texts:")
    arrayExeption = ['TRANSACCION', 'EXITOSA','Whatsapp', 'Compartir', 'Imprimir']

    for text in texts:
        # print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        # print("bounds: {}".format(",".join(vertices)))
        if text.description not in arrayExeption:
            ocr.append(text.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return ocr[1:]

def recortar_imagen(imagen):
    imagen = Image.open(imagen)
    # print(f'las dimensiones son: {imagen.size[1]}\n')
    if imagen.size[1] < 1100:
        coordenadas = (0,80,imagen.size[0],560)
    else:
        coordenadas = (0,100,imagen.size[0],860)
    imagen_recortada = imagen.crop(coordenadas)
    with io.BytesIO() as output:
        imagen_recortada.save(output, format='JPEG')
        imagen_recortada = output.getvalue()
    return imagen_recortada

# image_path = 'imagen4.jpg'

# text = detect_text(image_path)

# print(text)