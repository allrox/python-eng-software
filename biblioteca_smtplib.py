# Importando pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Criando objeto de mensagem
msg = MIMEMultipart()
texto = input("Entre com a mensagem: ")

# Parâmetros
senha = input("Informe a senha para envio: ")
msg['From'] = input("Email do remetente: ")
msg['To'] = input("Email do destinatário: ")
msg['Subject'] = input("Assunto: ")

# Criando o corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# Conexão com o servidor
server = smtplib.SMTP('smtp.hostinger.com: 587')
server.starttls()

# Login e envio
server.login(msg['From'], senha)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print('Mensagem enviada com sucesso')