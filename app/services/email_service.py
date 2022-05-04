from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# service to send an email to a user
def send_email(email_to, workspace_name, owner_name) -> None:
    email_from = getenv('EMAIL_FROM') # falecom@split.com
    password = getenv('PASS_EMAIL') # split@123
    
    try:
        subject = f"Você foi convidado para o workspace {workspace_name}"
        message = f"Usuário {owner_name} convidou você para o workspace {workspace_name}"

        email = MIMENonMultipart()
        email['From'] = email_from
        email['To'] = email_to
        email['Subject'] = subject
        
        email.attach(MIMEText(message, 'plain'))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
            server.login(email_from, password)
            server.sendmail(email['From'], email['To'], email.as_string())
            
    except FileNotFoundError:
        print('Gere o arquivo json com os email')