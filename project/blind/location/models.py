from django.db import models

# Create your models here.
class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    blind_id = models.IntegerField()
    name = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'location'
