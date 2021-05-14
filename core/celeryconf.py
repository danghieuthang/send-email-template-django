import os

from celery import Celery
from django.conf import settings
from typing import List

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("EmailSerivce")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
