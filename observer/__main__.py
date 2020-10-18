from .classes import EmailAddress, WhatsAppAddress, Alert


email_address = EmailAddress("+55 011 9999-9999")

whatsapp_address = WhatsAppAddress("address@email.com")

alert = Alert()
alert.add_address(email_address)
alert.add_address(whatsapp_address)

alert.trigger_alert()

alert.remove_address(email_address)
alert.remove_address(whatsapp_address)

alert.trigger_alert()
