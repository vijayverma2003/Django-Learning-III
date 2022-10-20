from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message',
                               'from@vijay.com', ['bob@vijay.com'])
        message.attach_file('playground/static/images/1.png')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
