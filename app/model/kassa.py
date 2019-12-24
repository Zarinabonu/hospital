from django.db import models


class Kassa(models.Model):
    register_num = models.IntegerField()
    surname = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    fath_name = models.CharField(max_length=45)
    date_birth = models.IntegerField()
    work_place = models.CharField(max_length=150)
    payment_type = models.CharField(max_length=45)
    book_num = models.IntegerField()
    date = models.DateField()
    summa = models.FloatField(default=0.00)
    date_finish = models.DateField()
    ras_check = models.IntegerField(default=0)

    class Meta:
        db_table = 'kassa'