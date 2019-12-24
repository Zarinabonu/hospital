from django.db import models


class Menu(models.Model):
    obed = models.FloatField(default=0.00)
    polnik = models.FloatField(default=0.00)
    ujen = models.FloatField(default=0.00)
    obshi = models.FloatField(default=0.00)
    date = models.DateField()
    zavtrak = models.FloatField(default=0.00)
    obed_a = models.FloatField(default=0.00)
    polnik_a = models.FloatField(default=0.00)
    ujen_a = models.FloatField(default=0.00)
    obshi_a = models.FloatField(default=0.00)
    zavtrak_a = models.FloatField(default=0.00)
    obed_b = models.FloatField(default=0.00)
    polnik_b = models.FloatField(default=0.00)
    ujen_b = models.FloatField(default=0.00)
    obshi_b = models.FloatField(default=0.00)
    zavtrak_b = models.FloatField(default=0.00)
    obed_v = models.FloatField(default=0.00)
    polnik_v = models.FloatField(default=0.00)
    ujen_v = models.FloatField(default=0.00)
    obshi_v = models.FloatField(default=0.00)
    zavtrak_v = models.FloatField(default=0.00)
    obed_c = models.FloatField(default=0.00)
    polnik_c = models.FloatField(default=0.00)
    ujen_c = models.FloatField(default=0.00)
    obshi_c = models.FloatField(default=0.00)
    zavtrak_c = models.FloatField(default=0.00)

    class Meta:
        db_table = 'menu'