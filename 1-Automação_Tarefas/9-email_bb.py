from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha', 'r').read()
from_email = 'ddamasceno288@gmail.com'
to_email = 'damascenod788@gmail.com'
subject = 'Informes BB'
body = open('files/corpo_bb.txt', 'r', encoding='utf-8').read()

# 1 - Montando a estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 - Adicionar Anexo

anexo = 'bb_preco.png'
# print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = anexo
    )
    
# 2 - Envio de e-mail

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )