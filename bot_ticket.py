from dotenv import dotenv_values
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

from formato_fecha import convertir_formato
from crear_pdf import crear_pdf
from ocr_google import detect_text
from ordenar_datos import ordenar
from generar_json import json_actualizado

# Cargar token como variable
env_vars = dotenv_values(".env")
TOKEN = env_vars.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

esperando_respuesta = False
print('ejecutando bot')

# Definir data como una variable global inicializada como None
data = None

@bot.message_handler(content_types=['photo'])
def handle_photo(mensaje):
    global esperando_respuesta, data  # Declarar que estamos usando la variable global
    esperando_respuesta = True
    markUp = InlineKeyboardMarkup()
    btn_si = InlineKeyboardButton('🟢Sí', callback_data='si')
    btn_no = InlineKeyboardButton('🔴No', callback_data='no')
    markUp.add(btn_si, btn_no)
    bot.send_message(mensaje.chat.id,'Archivo recibido')
    # Obtener la foto
    file_info = bot.get_file(mensaje.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    solo_valores = detect_text(downloaded_file)

    # ordenar los valores a un ordern deseado
    array_ordenado = ordenar(solo_valores)
    
    #generar json con los datos a inyectar
    data = json_actualizado(array_ordenado)

    # Enviar mensaje
    precio_recibo = data['monto']
    respuesta = f"¿El valor del recibo es de {precio_recibo}?"
    bot.send_message(mensaje.chat.id, respuesta, reply_markup=markUp)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global esperando_respuesta, data  # Declarar que estamos usando la variable global
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    if call.data == 'si':
        bot.send_message(call.message.chat.id, 'Generando ticket')
        esperando_respuesta = False
        nombre_pdf = crear_pdf(data)
        directorio_script = os.path.dirname(os.path.realpath(__file__))
        ruta_pdf = os.path.join(directorio_script, nombre_pdf)
        with open(ruta_pdf,'rb') as pdf_file:
            bot.send_document(call.message.chat.id,pdf_file)
        print('recibo enviado')
        # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, '¿Cuál es el valor de el pago?')
        # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

@bot.message_handler(func=lambda message: esperando_respuesta)
def handle_message(message):
    global esperando_respuesta, data
    if message.text.isdigit():  # Verificar si el mensaje del usuario es un número
        esperando_respuesta = False
        monto_correcto = int(message.text)
        data["monto"] = monto_correcto
        data["total"] = monto_correcto + data["comision"]
        bot.send_message(message.chat.id, f"El monto ha sido actualizado a {monto_correcto} MXN.")
        bot.send_message(message.chat.id, "creando ticket")
        nombre_pdf = crear_pdf(data)
        directorio_script = os.path.dirname(os.path.realpath(__file__))
        ruta_pdf = os.path.join(directorio_script, nombre_pdf)
        bot.send_message(message.chat.id,'Recibo generado')
        with open(ruta_pdf,'rb') as pdf_file:
            bot.send_document(message.chat.id,pdf_file)
        print('recivo enviado')
    else:
        bot.send_message(message.chat.id, "Por favor, introduce un valor numérico válido.")

bot.infinity_polling()
