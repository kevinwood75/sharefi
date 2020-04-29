from django.utils.timezone import now
from django.db import models


class Stockinfo(models.Model):
    ticker = models.CharField(max_length=70, blank=False, default='')
    price = models.FloatField()
    volume = models.IntegerField()
    stock_date = models.DateTimeField(default=now, blank=True)




