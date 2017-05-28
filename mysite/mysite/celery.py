import os, celery
from django.conf import settings


# встановлюємо стандартні Django налаштування для celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = celery.Celery('table.tasks')

# Використвуємо строку для того, щоб воркер не приховав об'єкт при використанні Windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)