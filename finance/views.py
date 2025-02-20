from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    from os import getenv
    from codecraft.settings import STATICFILES_DIRS
    print(getenv("IS_DEVELOPMENT") == "True")
    print(STATICFILES_DIRS)
    return HttpResponse("Hello from finances mod")
