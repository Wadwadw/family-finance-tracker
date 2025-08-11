from django.contrib import admin
from .models import Account, InitialBalance


admin.site.register(Account)
admin.site.register(InitialBalance)