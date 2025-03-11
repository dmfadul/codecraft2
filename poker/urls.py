from django.urls import path
from . import views


urlpatterns = [
    path('range/', views.poker_ranges, name='poker_range'),
    path("save_range/", views.save_range, name="save_range"),
]
