
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import time
class Email:
    def __init__(self,emailEnviado=None):
        self.lbShowMessagem=emailEnviado
        self.lbShowMessagem.setText("email Enviado")
        time.sleep(1)
        self.lbShowMessagem.repaint()
        
        self.lbShowMessagem.setText("")
    
    def EnviaEmail(self,destinatario=None,Assunto=None,caminho=None):
           
            fromaddr = "willow18282@gmail.com"
            toaddr = f'{destinatario}'#destinatario
            msg = MIMEMultipart()

            msg['From'] = fromaddr 
            msg['To'] = toaddr
            msg['Subject'] = f"{Assunto}"

            body = "\nCorpo da mensagem"

            msg.attach(MIMEText(body, 'plain'))

            filename = f'{caminho}'

            attachment = open(f'{caminho}','rb')
            part = MIMEBase('application', 'pdf')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
            msg.attach(part)

            attachment.close()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "wlfxktpnsedhtgih")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            
            server.quit()
           
            
   