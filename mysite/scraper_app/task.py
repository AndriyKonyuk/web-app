import os
from scraper_app.scraper import table_body_data
from mysite.models import Currency_index, Currency
# from datetime import datetime
# from celery import Celery
from django.db.utils import IntegrityError
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
# app = Celery('task', broker='redis:://')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#
#
# @app.task(bind=True)
django.setup()
def add_data_to_table():
    for l in table_body_data:
        try:
            cr = Currency_index.objects.get_or_create(name_of_currency=l[1], symbol_of_currency=l[2])

            t = Currency.objects.create(cur_index=cr[0], cur_market_cup=l[3], cur_price=l[4], cur_circul_supply=l[5],
                                        cur_volume=l[6], cur_1h=l[7], cur_24h=l[8], cur_7d=l[9]).save()
            t.save()
        except (IntegrityError, Exception) as e:
            print(e)

add_data_to_table()
