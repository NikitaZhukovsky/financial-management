from django.contrib import admin
from management.models import Category, Source, Transaction, Income, Balance


class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'status')


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'date_time')
    search_fields = ('source', 'amount')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date', 'time', 'payment_method')
    search_fields = ('category', 'amount', 'payment_method')


admin.site.register(Category)
admin.site.register(Source, SourceAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Balance)
