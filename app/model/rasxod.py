from django.db import models


class Rasxod(models.Model):
    otdel = models.CharField(max_length=45)
    register_num = models.IntegerField()
    quantity = models.IntegerField(default=1)
    date = models.DateField()
    name = models.CharField(max_length=45)
    otmen_date = models.CharField(max_length=300)
    otmen_date_a = models.CharField(max_length=300)
    otmen_date_b = models.CharField(max_length=300)
    otmen_date_v = models.CharField(max_length=300)
    otmen_date_c = models.CharField(max_length=300)
    otmen_date_rean = models.CharField(max_length=300)
    otmen_date_golod = models.CharField(max_length=300)

    class Meta:
        db_table = 'rasxod'