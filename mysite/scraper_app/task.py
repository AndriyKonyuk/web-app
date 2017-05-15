import os
from .scraper import table_body_data
from mysite.models import Currency_index, Currency
from datetime import datetime
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
app = Celery('task', broker='redis:://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def add_data_to_table():
    for l in table_body_data:
        Currency_index(l[2]).save()

        Currency(cur_name=l[1], cur_symbol=l[2], cur_market_cup=l[3], cur_price=l[4], cur_circul_supply=l[5],
                 cur_volume=l[6], cur_1h=l[7], cur_24h=l[8], cur_7d=l[9]).save()
