from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mainSite/index.html')

def about(request):
    return render(request, 'mainSite/about.html')

def contact(request):
    return render(request, 'mainSite/contact.html')

def plans(request):
    return render(request, 'mainSite/plans.html')

def submit(request):
    print("TESTE DE SUBMISSÃO")
    return render(request, 'mainSite/about.html')