from django.test import TestCase
from transactions.models import Category, Initiator, Transaction
from accounts.models import Account
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title="Продукты",
            type="expense"
        )

    def test_create_category_and_str(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(self.category.title, "Продукты")
        self.assertEqual(self.category.type, "expense")
        self.assertEqual(str(self.category), "Продукты -- expense")


class InitiatorModelTest(TestCase):
    def setUp(self):
        self.initiator = Initiator.objects.create(
            name="Maryna",
        )

    def test_create_initiator_and_str(self):
        self.assertEqual(Initiator.objects.count(), 1)
        self.assertEqual(self.initiator.name, "Maryna")
        self.assertEqual(str(self.initiator), "Maryna")
        self.assertEqual(self.initiator.description, "")


class TransactionModelTest(TestCase):
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
        self.category = Category.objects.create(
            title="Продукты",
            type="expense"
        )
        self.initiator = Initiator.objects.create(
            name="Maryna",
        )
        self.transaction = Transaction.objects.create(
            date=date(2025, 8, 13),
            amount=215,
            category=self.category,
            account=self.account,
            initiator=self.initiator
        )

    def test_create_transaction_and_str(self):
        self.assertEqual(self.transaction.date, date.today())
        self.assertEqual(self.transaction.amount, Decimal("215"))
        self.assertEqual(self.transaction.category.title, "Продукты")
        self.assertEqual(self.transaction.account.title, "Mono M")
        self.assertEqual(self.transaction.initiator.name, "Maryna")
        self.assertEqual(str(self.transaction), f"{date.today()} -- {215} -- {self.category}")
