from django.db.models import F
from management.models import Category, Source, Transaction, Income, Balance
from rest_framework.generics import ListAPIView
from management.serializers import (CategorySerializer, TransactionSerializer, BalanceSerializer,
                                    IncomeSerializer)
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
        sources = Income.objects.filter(user=user)
        serializer = IncomeSerializer(sources, many=True)
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


class CategoryTransactionView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, category_id):
        user = request.user
        queryset = Transaction.objects.filter(user=user, category__id=category_id)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
