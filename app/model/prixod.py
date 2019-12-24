from django.db import models


class Prixod(models.Model):
    otdel = models.CharField(max_length=45)
    register_num = models.IntegerField()
    quantity = models.IntegerField(default=1)
    date = models.DateField()
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'prixod'