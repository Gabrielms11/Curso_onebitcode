import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# 1-Dados do E-mail
password = open("senha", "r").read()
from_email = "gabrielmartinssantos11@gmail.com"
to_email = "gabrielmartinssantos11@gmail.com"
subject = "Automação Planilha"
body = """
Olá. Segue em anexo a automação da planilha 
para a empresa XYZ Automação.

Qualquer dúvida estou a disposição!
"""

# 2-Montando a estrutura do e-mail
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 3-Adicionar Anexo
anexo = "test.xlsx"
print(mimetypes.guess_type(anexo)[0].split("/"))
# mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
