from django.db import models


# Create your models here.

class Worldcities(models.Model):
    city = models.TextField(blank=True, null=True)
    lat = models.IntegerField(blank=True, null=True)
    lng = models.IntegerField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'worldcities'

    def __str__(self):
        return f"{Worldcities.city}, {Worldcities.lat, Worldcities.lng}"