import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nestor Ingles Jr'
email['to'] = 'nestor1ingles@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

# Log into test email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # Encription
    smtp.login('pylostestemail@gmail.com', 'sjunbrfyfjgzukzy')
    smtp.send_message(email)
    print('all good boss!')