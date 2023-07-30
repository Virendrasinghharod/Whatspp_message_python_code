# -*- coding: utf-8 -*-
"""Sending_whatsapp_mess_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ku0_WvhFvh-SSxKY2hu6nf3i5hfSfPd2
"""

from twilio.rest import Client

def send_whatsapp_message(account_sid, auth_token, twilio_phone_number, recipient, message):
    try:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message,
            from_='whatsapp:' + twilio_phone_number,
            to='whatsapp:' + recipient
        )

        print(f"WhatsApp message sent successfully! Message SID: {message.sid}")

    except Exception as e:
        print(f"Error occurred while sending the WhatsApp message: {e}")

# Example usage
if __name__ == "__main__":
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'  # Format: 'whatsapp:+1234567890'
    recipient = 'RECIPIENT_PHONE_NUMBER'  # Format: 'whatsapp:+1234567890'
    message = 'Hello, this is a test WhatsApp message sent using Python and Twilio!'

    send_whatsapp_message(account_sid, auth_token, twilio_phone_number, recipient, message)