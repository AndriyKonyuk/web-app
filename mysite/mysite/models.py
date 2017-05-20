from django.db import models


class Currency_index(models.Model):
    class Meta:
        unique_together = (('name_of_currency', 'symbol_of_currency'))

    name_of_currency = models.CharField(db_index=True, max_length=30)
    symbol_of_currency = models.CharField(db_index=True, max_length=30)

    def __str__(self):
        return self.name_of_currency


class Currency(models.Model):
    class Meta:
        ordering = ['-cur_update_date']
        verbose_name = 'Currency'

    cur_index = models.ForeignKey(Currency_index, related_name='coins_index', on_delete=models.CASCADE)
    cur_market_cup = models.CommaSeparatedIntegerField(max_length=15)
    cur_price = models.FloatField()
    cur_circul_supply = models.CommaSeparatedIntegerField(max_length=18)
    cur_volume = models.CommaSeparatedIntegerField(max_length=15)
    cur_1h = models.FloatField()
    cur_24h = models.FloatField()
    cur_7d = models.FloatField()
    cur_update_date = models.DateTimeField(db_index=True, auto_now_add=True)
