from django.db import models


class Shetchik(models.Model):
    otdel = models.CharField(max_length=45)
    quantity = models.IntegerField()
    date = models.DateField()

    class Meta:
        db_table = 'shetchik'