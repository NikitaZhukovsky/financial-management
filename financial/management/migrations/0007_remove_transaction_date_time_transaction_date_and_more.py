# Generated by Django 5.0.3 on 2024-04-12 18:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_alter_balance_current_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date_time',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
