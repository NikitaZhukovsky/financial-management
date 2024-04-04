from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Source(models.Model):
    STATUSES = (
        ('Main', 'Main'),
        ('Additional', 'Additional')
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUSES, max_length=100, default='Main')

    class Meta:
        verbose_name_plural = "Sources"

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    PAYMENT_METHODS = (
        ('Card', 'Card'),
        ('Cash', 'Cash'),
        ('Online Transfer', 'Online Transfer')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=100, default='Card')

    def __str__(self):
        return f"{self.amount} {self.date_time}"


class Income(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.source} {self.amount} {self.date_time}"


class Balance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name_plural = "Balance"

    def __str__(self):
        return f"{self.current_balance}"

