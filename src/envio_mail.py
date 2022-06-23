import smtplib
from password import password_gmail
from verificacion import codigo_generado
'''
Clase que tiene como objetivo enviar email.
'''

class SendEMail():
    def send_email_test(self, para):

        #dirección desde dónde se envian los correos
        gmail_user = 'unaventonunal@gmail.com'
        gmail_password = password_gmail
        from_address = gmail_user

        #para quien va destinado
        to_address = para
        
        #asunto y mensaje
        asunto = "Codigo de verificacion UN Aventon"
        mensaje=  f'Hola, bienvenido. Para continuar con el proceso de registro ingresa el siguiente codigo en la pagina de registro \n {codigo_generado}'
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        	    """ % (from_address,  to_address, asunto, mensaje)

        #proceso de login sobre el servidor. Smtp únicamente, imap o pop no
        #porque no queremos recivirlos, unicamente enviar
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(from_address, to_address, message)
        server.close()