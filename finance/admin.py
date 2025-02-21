from django.contrib import admin
from .models import Category, Card, Expense, Payment, CardTransaction

# Register your models here.

admin.site.register(Category)
admin.site.register(Card)
admin.site.register(Expense)
admin.site.register(Payment)
admin.site.register(CardTransaction)
