from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    from os import getenv
    print(getenv("envs: ", 'ALLOWED_HOSTS', 'SECRET_KEY'))
    return render(request, 'mainSite/index.html')

def about(request):
    return render(request, 'mainSite/about.html')

def contact(request):
    return render(request, 'mainSite/contact.html')

def plans(request):
    return render(request, 'mainSite/plans.html')

def submit(request):
    from .models import Message

    data_dict = request.POST

    user_name = data_dict.get('nome')
    user_phone = data_dict.get('telefone')
    user_email = data_dict.get('email')
    user_message = data_dict.get('pedido')

    new_message = Message.objects.create(
        user_name = user_name,
        user_phone = user_phone,
        user_email = user_email,
        user_message = user_message,
    )


    return render(request, 'mainSite/index.html')