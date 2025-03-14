from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.about, name="about"),
    path("contato/", views.contact, name="contact"),
    path("planos/", views.plans, name="plans"),
    path("submit/", views.submit, name="submit"),
]