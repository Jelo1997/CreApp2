from .models import *

from twilio.rest import Client

from holamundo.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

def enviar_mensaje_whatsapp(destinatario, mensaje):
    try:
        # Inicializa el cliente de Twilio con tus credenciales
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Crea el mensaje de WhatsApp
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=mensaje,
            to=destinatario
        )
        
        # Retorna el SID del mensaje si se envía correctamente
        return message.sid
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante el envío del mensaje
        print(f"Error al enviar mensaje de WhatsApp: {str(e)}")
        return None