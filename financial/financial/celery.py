import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financial.settings')

app = Celery("financial")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {

    'check_transactions': {
        'task': 'management.tasks.check_orders_and_send_mails',
        'schedule': crontab(day_of_month='1', hour='0', minute='0')

    }
}