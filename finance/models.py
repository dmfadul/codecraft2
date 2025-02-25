from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=255, unique=True)
    bank = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    
    number = models.CharField(max_length=16, blank=True, null=True)
    cvv = models.CharField(max_length=3, blank=True, null=True)
    expiry = models.DateField(blank=True, null=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='cards')

    def __str__(self):
        return self.title


class Expense(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    exp_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_fixed = models.BooleanField(default=False)

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='expenses')

    def __str__(self):
        return self.title


class Payment(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="payments")
    month = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    date = models.DateField()
    obs = models.TextField()


class CardTransaction(models.Model):
    card = models.ForeignKey(Card,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='transactions')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name="card_transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    bill_month = models.DateField()
    number_of_stallments = models.IntegerField(default=1) 
