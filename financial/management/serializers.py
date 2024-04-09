from rest_framework import serializers
from management.models import Category, Source, Transaction, Income, Balance
from datetime import date


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('current_balance', )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'status']


class IncomeSerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)

    class Meta:
        model = Income
        fields = ('source', 'amount', 'date_time', 'description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'date_time', 'description', 'payment_method')
