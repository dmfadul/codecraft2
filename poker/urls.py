from django.urls import path
from . import views


urlpatterns = [
    path('range/', views.poker_ranges, name='poker_range'),
    path('get_range/<str:position>/', views.get_range, name='get_range'),
    path('save_range/', views.save_range, name='save_range'),
    path('positions/', views.PositionCreateView.as_view(), name='add_position'),
]
