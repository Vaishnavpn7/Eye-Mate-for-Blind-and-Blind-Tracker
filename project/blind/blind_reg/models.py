from django.db import models
from friend.models import Friend


# Create your models here.
class BlindReg(models.Model):
    blind_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    place = models.CharField(max_length=25)
    district = models.CharField(max_length=20)
    pin = models.IntegerField()
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=35)
    image = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'blind_reg'


class Requset(models.Model):
    f_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    place = models.CharField(max_length=15)
    photo = models.CharField(max_length=500)
    pin = models.IntegerField()
    friend = models.ForeignKey(Friend, to_field='friend_id', on_delete=models.CASCADE)
    # friend_id = models.IntegerField()
    phone = models.CharField(max_length=300)
    status = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'requset'
