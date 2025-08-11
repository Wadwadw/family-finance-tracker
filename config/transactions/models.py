from django.db import models
from accounts.models import Account


class Category(models.Model):
    types = (
        ("income", "Income"),
        ("expense", "Expense")
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=types)

    def __str__(self):
        return f"{self.title} -- {self.type}"


class Initiator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    initiator = models.ForeignKey(Initiator, on_delete=models.SET_NULL, null=True)


