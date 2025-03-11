from django.urls import path
from . import views


urlpatterns = [
    path('range/', views.range, name='poker_range'),
]
