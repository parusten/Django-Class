from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def hello(req):
    return HttpResponse("dohjjj")
def hello1(req):
    return HttpResponse("PARAS")
def hello2(req):
    return HttpResponse("djhgf")

def greet(req, name):
    return HttpResponse(f"hello:{name}")

def index(request):
    return render(request, 'index.html')

def index(request):
    context={
        'name':'ram',
        'roll':19,

    }
    return render(request, 'index.html',context)



from django.core.mail import send_mail
def send(request):
    to_email = "promisenepal222@gmail.com"
    subject = 'Hello from Your Django App'
    message = 'This is a test email sent from your Django app.'
    from_email = "parusten20@gmail.com" # Sender's email address
    recipient_list = [to_email]  # Recipient's email address

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully!')






