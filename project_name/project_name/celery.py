import os 

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

app = Celery('{{ project_name }}', backend=settings.REDIS_URL, 
			 broker=settings.REDIS_URL)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
