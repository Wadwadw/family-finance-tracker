from django.test import TestCase
from accounts.models import Account, InitialBalance
from datetime import date
from decimal import Decimal
from django.contrib.auth.models import User


class AccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Maryna",
            first_name="Maryna",
            is_active=True,
            is_superuser=True,
        )
        self.account = Account.objects.create(
            title="Mono M",
            owner=self.user,
            balance=1000,
            currency="UAH"

        )

    def test_create_account_and_str(self):
        self.assertEqual(self.account.title, "Mono M")
        self.assertEqual(self.account.owner, self.user)
        self.assertEqual(self.account.balance, Decimal("1000"))
        self.assertEqual(self.account.currency, "UAH")
        self.assertEqual(str(self.account), f"Mono M -- {self.user}")


class InitialBalanceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Maryna",
            first_name="Maryna",
            is_active=True,
            is_superuser=True,
        )
        self.account = Account.objects.create(
            title="Mono M",
            owner=self.user,
            balance=1000,
            currency="UAH"

        )
        self.initial_balance = InitialBalance.objects.create(
            account=self.account,
            amount=250,
            date_create=date(2025, 3, 29)
        )

    def test_create_initial_balance_and_str(self):
        self.assertEqual(self.initial_balance.account, self.account)
        self.assertEqual(self.initial_balance.amount, Decimal("250"))
        self.assertEqual(self.initial_balance.date_create, date(2025, 3, 29))
        self.assertEqual(str(self.initial_balance), f"{self.account} -- {self.initial_balance.amount}")