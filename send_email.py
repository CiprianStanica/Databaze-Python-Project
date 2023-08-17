import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import date_mail

def trimite_email(adresa_destinatar, subiect, mesaj, atasament=None):
    # Configurați detaliile contului de e-mail
    de_la = date_mail.mail
    parola = date_mail.parola

    # Configurați serverul SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(de_la, parola)

    # Construiți e-mailul
    # adresa_destinatar = 'stanicaciprian01@gmail.com'
    # subiect = 'Salut prietene!'
    e_mail = MIMEMultipart()
    e_mail['From'] = de_la
    e_mail['To'] = adresa_destinatar
    e_mail['Subject'] = subiect
    e_mail.attach(MIMEText(mesaj, 'plain'))

    if atasament:
        with open(atasament, 'rb') as atasament_fisier:
            atasament_mime = MIMEApplication(atasament_fisier.read(), _subtype="pdf")
            atasament_mime.add_header('content-disposition', f'attachment; filename= {atasament}')
            e_mail.attach(atasament_mime)

    # Trimiteți e-mailul
    server.sendmail(de_la, adresa_destinatar, e_mail.as_string())
    server.quit()

# Apelăm funcția pentru a trimite e-mailul
trimite_email(
'corina.ionita58@yahoo.com', 'subiect',
"""Incerc sa vad daca mai merge"""
)
