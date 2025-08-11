from django.contrib import admin
from .models import Category, Initiator, Transaction, InitialBalance


admin.site.register(Category)
admin.site.register(Initiator)
admin.site.register(Transaction)
admin.site.register(InitialBalance)


