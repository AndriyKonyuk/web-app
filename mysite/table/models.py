from django.db import models


class Coins(models.Model):
    class Meta:
        unique_together = (('name_of_currency', 'symbol_of_currency'))

    name_of_currency = models.CharField(db_index=True, max_length=30)
    symbol_of_currency = models.CharField(db_index=True, max_length=30)

    def __str__(self):
        return self.name_of_currency


class Currency(models.Model):
    class Meta:
        ordering = ['-update_date']
        verbose_name = 'Currency'

    coinName = models.ForeignKey(Coins, related_name='coins_index', on_delete=models.CASCADE)
    market_cup = models.DecimalField(max_digits=16, decimal_places=2)
    price = models.DecimalField(max_digits=16, decimal_places=2, )
    circul_supply = models.DecimalField(max_digits=18, decimal_places=2)
    volume = models.DecimalField(max_digits=16, decimal_places=2, )
    hour = models.DecimalField(max_digits=16, decimal_places=2, )
    day = models.DecimalField(max_digits=16, decimal_places=2, )
    week = models.DecimalField(max_digits=16, decimal_places=2, )
    update_date = models.DateTimeField(db_index=True, auto_now_add=True)
