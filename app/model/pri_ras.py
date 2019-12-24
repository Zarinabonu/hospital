from django.db import models


class Pri_ras(models.Model):
    from_him = models.CharField(max_length=45)
    to_him = models.CharField(max_length=45)
    quantity = models.IntegerField(default=1)
    date = models.DateField()
    register_num = models.IntegerField(default=0)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'pri_ras'