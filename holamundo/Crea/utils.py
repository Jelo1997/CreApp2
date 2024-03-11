from .models import *

from twilio.rest import Client

from holamundo.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

def enviar_mensaje_whatsapp(destinatario, mensaje):
    try:
        # Inicializa el cliente de Twilio con tus credenciales
        account_sid = 'AC5e2d44bfed136b0af07958a7b6a1b36c'
        auth_token = '6ef75c578ab24a6a2ba5699e81ea7f6b'
        client = Client(account_sid, auth_token)
        
        # Crea el mensaje de WhatsApp
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body=mensaje,
            to= 'whatsapp:+593995980319'
        )
        
        # Retorna el SID del mensaje si se envía correctamente
        print(message.sid) 
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante el envío del mensaje
        print(f"Error al enviar mensaje de WhatsApp: {str(e)}")
        return None