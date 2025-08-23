from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class AccountSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="owner", write_only=True)
    class Meta:
        model = Account
        fields = ["id", "title", "owner", "owner_id",  "balance", "currency"]