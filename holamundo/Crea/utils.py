from .models import *

# utils.py
from twilio.rest import Client

def enviar_mensaje_whatsapp(account_sid, auth_token, whatsapp_number, destinatario, mensaje):
    try:
        # Inicializa el cliente de Twilio con las credenciales proporcionadas
        client = Client(account_sid, auth_token)
        
        # Crea el mensaje de WhatsApp
        message = client.messages.create(
            from_=whatsapp_number,
            body=mensaje,
            to=destinatario
        )
        
        # Retorna el SID del mensaje si se envía correctamente
        return message.sid
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante el envío del mensaje
        print(f"Error al enviar mensaje de WhatsApp: {str(e)}")
        return None