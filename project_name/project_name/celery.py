from __future__ import absolute_import

from celery import Celery
from django.conf import settings

app = Celery('{{ project_name }}', backend=settings.REDIS_URL, 
			 broker=settings.REDIS_URL)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
