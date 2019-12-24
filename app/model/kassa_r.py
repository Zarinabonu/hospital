from django.db import models


class Kassa_r(models.Model):
    register_num = models.IntegerField()
    surname = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    fath_name = models.CharField(max_length=45)
    date_birth = models.IntegerField()
    work_place = models.CharField(max_length=145)
    payment_type = models.CharField(max_length=45)
    book_num = models.IntegerField()
    date = models.DateField()
    summa = models.FloatField()

    class Meta:
        db_table = 'kassa_r'