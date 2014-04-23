from __future__ import absolute_import

from celery import Celery
from django.conf import settings

app = Celery('{{ project_name }}', broker=settings.REDIS_URL)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)