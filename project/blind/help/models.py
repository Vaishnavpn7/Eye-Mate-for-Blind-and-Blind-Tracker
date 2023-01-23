from django.db import models

# Create your models here.
class Help(models.Model):
    help_id = models.AutoField(primary_key=True)
    blind_id = models.IntegerField()
    # name = models.CharField(max_length=20)
    # contact = models.CharField(max_length=12)
    # image = models.CharField(max_length=20)
    latitude = models.CharField(max_length=11)
    longitude = models.CharField(max_length=11)
    date = models.CharField(max_length=11)
    time = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'help'
