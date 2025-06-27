import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookswap_project.settings')

app = Celery('bookswap_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()