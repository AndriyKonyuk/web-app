from celery.schedules import crontab
from table.scraper import Scraper
from celery.utils.log import get_task_logger
from django.db.utils import IntegrityError
from table.models import Coins, Currency
from mysite.celery import app
logger = get_task_logger(__name__)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/2'), insert_crypt_table())

@app.task
def insert_crypt_table():
    scrap_dic = Scraper().return_data()
    for name, symbol, market_cap, price, circulating_supply, volume, h1, h24, d7 in zip(
            scrap_dic['Name'], scrap_dic['Symbol'],
            scrap_dic['market_cap'], scrap_dic['Price'], scrap_dic['Circulating supply'],
            scrap_dic['Volume'], scrap_dic['h1'], scrap_dic['h24'], scrap_dic['d7']):
        try:
            cr = Currency.objects.get_or_create(name_of_currency=name, symbol_of_currency=symbol)
            t = Coins.objects.create \
                    (
                    coin_name=cr[0],
                    marcet_cap=market_cap,
                    price=price,
                    circul_supply=circulating_supply,
                    volume=volume,
                    hour=h1,
                    day=h24,
                    week=d7
                )
            print(cr)
            t.save()
        except (IntegrityError, Exception) as e:
            print(e)


logger.info("Saved image from Flickr")
