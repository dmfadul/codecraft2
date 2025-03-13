from django.shortcuts import redirect
from django.urls import path
from . import views


urlpatterns = [
    path("", lambda request: redirect("poker_range", permanent=True)),
    path('range/', views.poker_ranges, name='poker_range'),
    path('get_range/<str:position>/<str:context>/<int:stack_id>/', views.get_range, name='get_range'),
    path('save_range/', views.save_range, name='save_range'),
    path('positions/', views.PositionCreateView.as_view(), name='add_position'),
    path('stacks/', views.StackDepthCreateView.as_view(), name='add_stack'),
    path('context/', views.ContextCreateView.as_view(), name='add_context'),
]
