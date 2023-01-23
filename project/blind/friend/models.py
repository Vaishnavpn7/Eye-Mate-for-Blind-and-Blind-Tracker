from django.db import models


# from blind_reg.models import BlindReg
# Create your models here.
class Friend(models.Model):
    friend_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    place = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    pin = models.IntegerField()
    blind_id = models.IntegerField()
    # blind=models.ForeignKey(BlindReg,to_fields='blind_id',on_delete=models.)
    contact = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    image = models.CharField(max_length=300)

    # status = models.CharField(db_column='Status', max_length=15)

    class Meta:
        managed = False
        db_table = 'friend'

        # class Requset(models.Model):
        #     f_id = models.AutoField(primary_key=True)
        #     name = models.CharField(max_length=15)
        #     place = models.CharField(max_length=15)
        #     photo = models.CharField(max_length=500)
        #     pin = models.IntegerField()
        #     friend=models.ForeignKey(Friend ,to_field='friend_id',on_delete=models.CASCADE)
        #     # friend_id = models.IntegerField()
        #     phone = models.CharField(max_length=300)
        #     status = models.CharField(max_length=25)
        #
        #     class Meta:
        #         managed = False
        #         db_table = 'requset'
