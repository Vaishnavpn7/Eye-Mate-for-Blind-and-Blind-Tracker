from django.db import models


class Caretaker(models.Model):
    caretak_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    place = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    pin = models.IntegerField()
    image = models.CharField(max_length=300)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=15)
    status = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'caretaker'
