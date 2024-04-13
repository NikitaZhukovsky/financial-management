from django.urls import path
from management.views import (CategoryListView, CategoryTransactionView, TransactionListView,
                              BalanceView, IncomesListView, CustomCategoryView)

urlpatterns = [
    path('balance/', BalanceView.as_view(), name='balance'),
    path('incomes/', IncomesListView.as_view(), name='incomes'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('custom-categories/', CustomCategoryView.as_view(), name='custom_categories'),
    path('categories/<int:category_id>/', CategoryTransactionView.as_view(), name='category-transactions'),
    path('transactions/', TransactionListView.as_view(), name='transactions'),
]