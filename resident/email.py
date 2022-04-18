from cgitb import html
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(name,receiver):
    subject = 'Welcome to Our neighborhood'
    sender = 'melodytowett992gmail.com'

    text_content = render_to_string('email/residentemail.txt',{"name":name})
    html_content = render_to_string('email/resident.html',{"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()