from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=2, decimal_places=2)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title} -- {self.owner}"