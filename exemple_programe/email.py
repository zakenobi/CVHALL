import smtplib, ssl, imghdr
from email.message import EmailMessage

msg = EmailMessage()

# on rentre les renseignements pris sur le site du fournisseur
smtp_adress = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_adress = 'cvhall.epf@gmail.com'
email_password = 'PMFGE3A.23'

# on rentre les informations sur le destinataire
email_receiver = 'zac.gagnou@gmail.com'

# on crée la connexion
context = ssl.create_default_context()

with open(u'Logo_EPF.png','rb') as m:
  file_data = m.read()
  file_type = imghdr.what(m.name)
  file_name = m.name
  

msg.add_attachement(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
  # connexion au compte
  server.login(email_adress, email_password)
  # envoi du mail
  server.sendmail(email_adress, email_receiver, msg)
