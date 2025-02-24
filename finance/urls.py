from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.CategoryCreateView.as_view(), name='add-category'),
    path('card/', views.CardCreateView.as_view(), name='add-card'),
    path('expense/', views.ExpenseCreateView.as_view(), name='add-expense'),
    path('payment/', views.PaymentCreateView.as_view(), name='add-payment'),
    path('card_transaction/', views.CardTransactionCreateView.as_view(), name='add-card-transaction'),
]