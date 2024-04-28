from rest_framework import serializers
from management.models import Category, Source, Transaction, Income, Balance, UserCategory
from datetime import date


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('current_balance', )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'status']


class DeleteSourceSerializer(serializers.Serializer):
    source_id = serializers.IntegerField()


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ('id', 'source', 'amount', 'date_time', 'description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'category', 'amount', 'date', 'time', 'description', 'payment_method')


class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = ('id', 'name', 'description')


class DeleteCustomCategorySerializer(serializers.Serializer):
    custom_category_id = serializers.IntegerField()
