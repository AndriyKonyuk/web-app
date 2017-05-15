from django.db import models
from django.contrib import admin


class Currency_index(models.Model):
    name_of_currency = models.CharField(db_index=True, max_length=50)


class Currency(models.Model):
    cur_name = models.ForeignKey(Currency_index, on_delete=models.CASCADE)
    cur_symbol = models.CharField(max_length=7)
    cur_market_cup = models.CommaSeparatedIntegerField(max_length=15)
    cur_price = models.FloatField()
    cur_circul_supply = models.CommaSeparatedIntegerField(max_length=18)
    cur_volume = models.CommaSeparatedIntegerField(max_length=15)
    cur_1h = models.FloatField()
    cur_24h = models.FloatField()
    cur_7d = models.FloatField()
    cur_update_data = models.DateTimeField(db_index=True, auto_now_add=True)


admin.site.register(Currency_index)
admin.site.register(Currency)
