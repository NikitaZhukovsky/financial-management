from django.db.models import F
from management.models import Category, Source, Transaction, Income, Balance, UserCategory
from rest_framework.generics import ListAPIView
from management.serializers import (CategorySerializer, TransactionSerializer, BalanceSerializer,
                                    IncomeSerializer, UserCategorySerializer, DeleteCustomCategorySerializer,
                                    SourceSerializer)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BalanceView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        balance = Balance.objects.filter(user=user)
        serializer = BalanceSerializer(balance, many=True)
        return Response(serializer.data)


class IncomesListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        incomes = Income.objects.filter(user=user)
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        income = serializer.save(user=user)

        balance = Balance.objects.get(user=user)
        balance.current_balance += income.amount
        balance.save()

        return Response()


class TransactionListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        transaction = serializer.save(user=user)

        balance = Balance.objects.get(user=user)
        balance.current_balance -= transaction.amount
        balance.save()
        return Response()


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class CustomCategoryView(APIView):

    def get(self, request):
        user = request.user
        custom_categories = UserCategory.objects.filter(user=user)
        serializer = UserCategorySerializer(custom_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        input_serializer = UserCategorySerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        user = request.user
        custom_categories = input_serializer.save(user=user)
        return Response()

    def delete(self, request):
        input_serializer = DeleteCustomCategorySerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        custom_category = UserCategory.objects.get(id=input_serializer.data["custom_category_id"]).delete()
        return Response()


class CategoryTransactionView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, category_id):
        user = request.user
        queryset = Transaction.objects.filter(user=user, category__id=category_id)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)



