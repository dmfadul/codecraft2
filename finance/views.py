from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Category, Card, Expense, Payment, CardTransaction


def index(request):
    from os import getenv
    from codecraft.settings import STATICFILES_DIRS
    print(getenv("IS_DEVELOPMENT") == "True")
    print(STATICFILES_DIRS)
    return HttpResponse("Hello from finances mod")


class CategoryCreateView(CreateView):
    model = Category
    fields = ['title', 'description']
    template_name = 'finance/category_form.html'
    success_url = reverse_lazy('add-category')  # or wherever you want to redirect

class CardCreateView(CreateView):
    model = Card
    fields = ['title', 'bank', 'banner', 'limit', 'number', 'cvv', 'expiry', 'category']
    template_name = 'expense_app/card_form.html'
    success_url = reverse_lazy('add-card')

class ExpenseCreateView(CreateView):
    model = Expense
    fields = ['title', 'description', 'due_date', 'exp_amount', 'is_fixed', 'category']
    template_name = 'expense_app/expense_form.html'
    success_url = reverse_lazy('add-expense')

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['expense', 'month', 'amount', 'is_paid', 'date', 'obs']
    template_name = 'expense_app/payment_form.html'
    success_url = reverse_lazy('add-payment')

class CardTransactionCreateView(CreateView):
    model = CardTransaction
    fields = ['card', 'description', 'category', 'amount', 'date', 'bill_month', 'number_of_stallments']
    template_name = 'expense_app/card_transaction_form.html'
    success_url = reverse_lazy('add-card-transaction')
