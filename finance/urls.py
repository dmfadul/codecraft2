from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.CategoryCreateView.as_view()),
    path('card/add/', views.CardCreateView.as_view(), name='add-card'),
    path('expense/add/', views.ExpenseCreateView.as_view(), name='add-expense'),
    path('payment/add/', views.PaymentCreateView.as_view(), name='add-payment'),
    path('card_transaction/add/', views.CardTransactionCreateView.as_view(), name='add-card-transaction'),
]