from django.contrib import admin
from management.models import Category, Source, Transaction, Income, Balance


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'date_time')
    search_fields = ('source', 'amount')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date_time')
    search_fields = ('category', 'amount')


admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Balance)

