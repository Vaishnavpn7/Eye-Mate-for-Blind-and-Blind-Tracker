from django.db import models

# Create your models here.
class Complaint(models.Model):
    comp_id = models.AutoField(primary_key=True)
    caretak_id = models.IntegerField()
    complaint = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'