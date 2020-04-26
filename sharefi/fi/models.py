from django.db import models


class Stockinfo(models.Model):
    ticker = models.CharField(max_length=70, blank=False, default='')
    price = models.IntegerField()
    volume = models.IntegerField()


