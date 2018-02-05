from django.db import models

# Create your models here.
class NasaFiles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, db_index=True) #This allows for fast searching
    numOfDownloads = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, db_index=True)
    file = models.FileField(unique=True)

